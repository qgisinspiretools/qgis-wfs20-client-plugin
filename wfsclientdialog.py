# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WfsClientDialog
                                 A QGIS plugin
 WFS 2.0 Client
                             -------------------
        begin                : 2012-05-17
        copyright            : (C) 2012 by Juergen Weichand
        email                : juergen@weichand.de
        website              : http://www.weichand.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import os.path
import re
import logging
import tempfile
import random
import string
from xml.etree import ElementTree

from qgis.PyQt import QtCore, QtGui, QtWidgets, uic
from qgis.PyQt.QtNetwork import (
    QNetworkAccessManager,
    QNetworkReply,
    QNetworkRequest,
    QNetworkProxy,
)
try:
    from qgis.PyQt import QtXmlPatterns
    HAS_XMLPATTERNS = True
except Exception:
    HAS_XMLPATTERNS = False

from qgis.core import *
from osgeo import gdal
from osgeo import ogr
from urllib.parse import quote as urlquote  # Ersatz für urllib2.quote

from .epsglib import *
from .wfs20lib import *
from .metadataclientdialog import MetadataClientDialog

plugin_path = os.path.abspath(os.path.dirname(__file__))
UI_WFS_PATH = os.path.join(os.path.dirname(__file__), "ui_wfsclient.ui")

# ---- Qt5/Qt6 compatibility helper for QIODevice open modes ----
def _iodev_flag(name: str):
    # Qt6: QIODevice.OpenModeFlag.NAME
    try:
        return getattr(QtCore.QIODevice.OpenModeFlag, name)
    except Exception:
        # Qt5: QIODevice.NAME
        return getattr(QtCore.QIODevice, name)

def _iodev_mode(flag):
    try:
        return QtCore.QIODevice.OpenMode(flag)  # Qt6
    except Exception:
        return flag  # Qt5

# ---- Qt5/Qt6 compatibility helper for QNetworkProxy types ----
from qgis.PyQt.QtNetwork import QNetworkProxy

def _nproxy_type(name: str):
    try:
        # Qt6
        return getattr(QNetworkProxy.ProxyType, name)
    except Exception:
        # Qt5
        return getattr(QNetworkProxy, name)

# ---- Qt5/Qt6 compatibility helpers for QNetwork enums ----
def _nr_attr(name):
    # QNetworkRequest attribute enum (Qt6) vs flat (Qt5)
    try:
        from qgis.PyQt.QtNetwork import QNetworkRequest
        return getattr(QNetworkRequest.Attribute, name)
    except Exception:
        from qgis.PyQt.QtNetwork import QNetworkRequest
        return getattr(QNetworkRequest, name)


def _nrep_err(name):
    # QNetworkReply.NetworkError (Qt6) vs flat (Qt5)
    try:
        from qgis.PyQt.QtNetwork import QNetworkReply
        return getattr(QNetworkReply.NetworkError, name)
    except Exception:
        from qgis.PyQt.QtNetwork import QNetworkReply
        return getattr(QNetworkReply, name)


class _UiProxy:
    """Leitet self.ui.<name> auf Widgets auf self weiter, damit bestehender Code unverändert bleibt."""
    def __init__(self, owner):
        self._o = owner

    def __getattr__(self, name):
        return getattr(self._o, name)


class WfsClientDialog(QtWidgets.QDialog):


    def __init__(self, parent: QtWidgets.QWidget | None = None, plugin=None, url=None):
        # Parent ist ein echtes QWidget (z. B. iface.mainWindow())
        super().__init__(parent)
        self.plugin = plugin
        self.url = url

        # UI zur Laufzeit laden (Qt5/Qt6-kompatibel)
        uic.loadUi(UI_WFS_PATH, self)
        self.ui = _UiProxy(self)

        self.settings = QgsSettings()
        self.qnam = QgsNetworkAccessManager.instance()
        self.qnam.authenticationRequired.connect(self.authenticationRequired)
        self.qnam.sslErrors.connect(self.sslErrors)
        self.qnam.authenticationRequired.connect(self.authenticationRequired)
        self.qnam.sslErrors.connect(self.sslErrors)

        logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logfile = self.get_temppath("wfs20client.log")
        logging.basicConfig(filename=logfile, level=logging.DEBUG, format=logformat)

        self.logger = logging.getLogger('WFS 2.0 Client')

        self.ui.frmExtent.show()
        self.ui.frmParameter.hide()
        self.ui.progressBar.setVisible(False)
        self.ui.cmdListStoredQueries.setVisible(False)

        # Load default onlineresource
        if url:
            self.ui.txtUrl.setText(url)
        else:
            self.ui.txtUrl.setText(self.get_url())
        self.ui.txtCount.setText(self.get_featurelimit())

        self.ui.txtUsername.setVisible(False)
        self.ui.txtPassword.setVisible(False)
        self.ui.lblUsername.setVisible(False)
        self.ui.lblPassword.setVisible(False)

        self.parameter_lineedits = []
        self.parameter_labels = []

        self.init_variables()

        self.onlineresource = ""
        self.vendorparameters = ""

        # Canvas/CRS über plugin.iface
        self.ui.lblMessage.setText(
            "SRS is set to EPSG: {0}".format(
                str(self.plugin.iface.mapCanvas().mapSettings().destinationCrs().postgisSrid())
            )
        )
        self.ui.txtSrs.setText(
            "urn:ogc:def:crs:EPSG::{0}".format(
                str(self.plugin.iface.mapCanvas().mapSettings().destinationCrs().postgisSrid())
            )
        )

        self.ui.cmdGetCapabilities.clicked.connect(self.getCapabilities)
        self.ui.cmdListStoredQueries.clicked.connect(self.listStoredQueries)
        self.ui.cmdGetFeature.clicked.connect(self.getFeature)
        self.ui.cmdMetadata.clicked.connect(self.show_metadata)
        self.ui.cmdExtent.clicked.connect(self.show_extent)
        self.ui.chkExtent.clicked.connect(self.update_extent_frame)
        self.ui.chkAuthentication.clicked.connect(self.update_authentication)
        self.ui.cmbFeatureType.currentIndexChanged.connect(self.update_ui)

        self.httpRequestAborted = False
        self.reply = None

        if url:
            self.getCapabilities()

    def init_variables(self):
        self.columnid = 0
        self.bbox = ""
        self.querytype = ""
        self.featuretypes = {}
        self.storedqueries = {}

    # Process GetCapabilities-Request
    def getCapabilities(self):
        self.init_variables()
        self.ui.cmdGetFeature.setEnabled(False)
        self.ui.cmbFeatureType.clear()
        self.ui.frmExtent.show()
        self.ui.frmParameter.hide()
        self.ui.chkExtent.setChecked(False)
        self.ui.txtExtentWest.setText("")
        self.ui.txtExtentEast.setText("")
        self.ui.txtExtentNorth.setText("")
        self.ui.txtExtentSouth.setText("")
        self.ui.cmdMetadata.setVisible(True)
        self.ui.cmdExtent.setVisible(True)
        self.ui.lblCount.setVisible(True)
        self.ui.txtCount.setText(self.get_featurelimit())
        self.ui.txtCount.setVisible(True)
        self.ui.lblSrs.setVisible(True)
        self.ui.txtSrs.setText("urn:ogc:def:crs:EPSG::{0}".format(
            str(self.plugin.iface.mapCanvas().mapSettings().destinationCrs().postgisSrid())))
        self.ui.txtSrs.setVisible(True)
        self.ui.txtFeatureTypeTitle.setVisible(False)
        self.ui.txtFeatureTypeDescription.setVisible(False)
        self.ui.lblInfo.setText("FeatureTypes")
        self.ui.lblMessage.setText("")

        self.onlineresource = self.ui.txtUrl.text().strip()

        if len(self.onlineresource) == 0:
            QtWidgets.QMessageBox.critical(self, "OnlineResource Error", "Not a valid OnlineResource!")
            return

        if "?" in self.onlineresource:
            request = "{0}{1}".format(self.onlineresource, self.fix_acceptversions(self.onlineresource, "&"))
        else:
            request = "{0}{1}".format(self.onlineresource, self.fix_acceptversions(self.onlineresource, "?"))

        self.reply = None
        self.httpGetId = 0
        self.url = QtCore.QUrl(request)

        self.startCapabilitiesRequest(self.url)

    def _extract_authcfg(self, qurl: QtCore.QUrl) -> str:
        q = QtCore.QUrlQuery(qurl)
        return q.queryItemValue("authcfg").strip()

    def _apply_authcfg(self, request: QNetworkRequest):
        authcfg = self._extract_authcfg(request.url())
        if authcfg:
            QgsAuthManager.instance().updateNetworkRequest(request, authcfg)
            self.logMessage(f"Applied authcfg={authcfg} to request")

    # Process ListStoredQueries-Request
    def listStoredQueries(self):
        self.init_variables()
        self.ui.cmdGetFeature.setEnabled(False)
        self.ui.cmbFeatureType.clear()
        self.ui.frmExtent.hide()
        self.ui.frmParameter.show()
        self.layout_reset()
        self.ui.cmdMetadata.setVisible(False)
        self.ui.cmdExtent.setVisible(False)
        self.ui.lblCount.setVisible(False)
        self.ui.txtCount.setText("")
        self.ui.txtCount.setVisible(False)
        self.ui.lblSrs.setVisible(False)
        self.ui.txtSrs.setVisible(False)
        self.ui.txtFeatureTypeTitle.setVisible(False)
        self.ui.txtFeatureTypeDescription.setVisible(False)
        self.ui.lblInfo.setText("StoredQueries")
        self.ui.lblMessage.setText("")

        if not self.onlineresource:
            QtWidgets.QMessageBox.critical(self, "OnlineResource Error", "Not a valid OnlineResource!")
            return
        if "?" in self.onlineresource:
            request = "{0}&service=WFS&version=2.0.0&request=DescribeStoredQueries".format(self.onlineresource)
        else:
            request = "{0}?service=WFS&version=2.0.0&request=DescribeStoredQueries".format(self.onlineresource)
        request += self.vendorparameters

        self.reply = None
        self.httpGetId = 0
        self.url = QtCore.QUrl(request)

        self.startListStoredQueriesRequest(self.url)

    def startMetadataRequest(self, url):
        self.logMessage('Requesting metadata from {0}'.format(url.url()))
        req = QNetworkRequest(url)
        self._apply_authcfg(req)
        self.reply = self.qnam.get(req)
        self._connect_reply_signals(self.reply, self.MetadataRequestFinished)

    def startCapabilitiesRequest(self, url):
        self.logMessage('Requesting capabilities from {0}'.format(url.url()))
        req = QNetworkRequest(url)
        self._apply_authcfg(req)
        self.reply = self.qnam.get(req)
        self._connect_reply_signals(self.reply, self.capabilitiesRequestFinished)

    def startListStoredQueriesRequest(self, url):
        self.logMessage('Requesting list of stored queries from {0}'.format(url.url()))
        req = QNetworkRequest(url)
        self._apply_authcfg(req)
        self.reply = self.qnam.get(req)
        self._connect_reply_signals(self.reply, self.storedQueriesRequestFinished)

    def _connect_reply_signals(self, reply, finished_slot):
        reply.finished.connect(finished_slot)
        # PyQt5>=5.15 / Qt6:
        if hasattr(reply, "errorOccurred"):
            reply.errorOccurred.connect(self.errorOcurred)
        else:
            # older PyQt5 Fallback
            try:
                reply.error.connect(self.errorOcurred)
            except Exception:
                pass

    def MetadataRequestFinished(self):
        # Check for HTTP/network errors first
        if self.checkForHTTPErrors():
            return

        response = self.reply
        xslfilename = os.path.join(plugin_path, "iso19139jw.xsl")

        # Read raw response content (QByteArray)
        response_content = response.readAll()

        # -------- Parse headers (Qt5/Qt6 robust) --------
        encoding = 'utf_8'
        length = len(response_content)

        try:
            header_pairs = response.rawHeaderPairs()
        except Exception:
            header_pairs = []

        for name_ba, value_ba in header_pairs:
            # QByteArray → bytes
            name_bytes = bytes(name_ba).lower()
            value_bytes = bytes(value_ba)

            if name_bytes == b'content-type':
                # Extract charset from Content-Type, e.g. b"text/xml; charset=UTF-8"
                m = re.search(br'charset=([^\s;]+)', value_bytes, flags=re.I)
                if m:
                    try:
                        encoding = m.group(1).decode('ascii', 'ignore')
                        self.logMessage('Got encoding from header: {0}'.format(encoding))
                    except Exception:
                        pass

            elif name_bytes == b'content-length':
                try:
                    length = int(value_bytes.decode('ascii', 'ignore').strip())
                    self.logMessage('Found Content-Length header: {0}'.format(length))
                except Exception:
                    pass

        encoding = encoding.lower().translate(encoding.maketrans('-', '_'))
        self.logMessage('Using encoding {0} for metadata'.format(encoding))
        self.logMessage('Using content-length {0} for metadata'.format(length))

        # -------- Decode bytes into text with detected encoding --------
        try:
            xml_source = str(response_content, encoding)
        except LookupError:
            self.logMessage('Could not use encoding {0}, trying again with utf_8'.format(encoding), Qgis.Warning)
            xml_source = str(response_content, 'utf_8')
        except Exception as e:
            # Last fallback
            self.logMessage('Decoding error: {0}. Falling back to utf_8'.format(e), Qgis.Warning)
            try:
                xml_source = str(response_content, 'utf_8')
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Metadata Error", "Unable to decode metadata response.")
                return

        # -------- XSLT transformation --------
        html = None
        if HAS_XMLPATTERNS:
            # Qt5 path (if available): QtXmlPatterns (XSLT 2.0)
            try:
                qry = QtXmlPatterns.QXmlQuery(QtXmlPatterns.QXmlQuery.XSLT20)
                qry.setMessageHandler(MessageHandler())
                qry.setFocus(xml_source)
                qry.setQuery(QtCore.QUrl('file:///' + xslfilename))
                html = qry.evaluateToString()
            except Exception as e:
                self.logMessage('XSLT transformation failed: {0}'.format(e), Qgis.Warning)
                html = None
        else:
            # Qt6 path: try lxml (XSLT 1.0)
            try:
                import lxml.etree as LET
                # Parse XSLT and XML; ensure UTF-8 input for lxml
                xslt_doc = LET.parse(xslfilename)
                transform = LET.XSLT(xslt_doc)
                xml_doc = LET.fromstring(xml_source.encode('utf-8', errors='ignore'))
                result_tree = transform(xml_doc)
                html = str(result_tree)  # HTML string
            except Exception as e:
                self.logMessage('lxml XSLT fallback failed: {0}'.format(e), Qgis.Warning)
                html = None

        # -------- Show the result --------
        if html:
            dlg = MetadataClientDialog()
            dlg.ui.wvMetadata.setHtml(html)
            dlg.show()
            result = dlg.exec()  # Qt6-compatible
            if result == 1:
                pass
        else:
            QtWidgets.QMessageBox.critical(
                self,
                "XSLT not available",
                "QtXmlPatterns (XSLT) is not available under Qt6 and lxml fallback failed.\n"
                "The metadata HTML representation cannot be generated."
            )

    def capabilitiesRequestFinished(self):

        if self.reply is None:
            # already aborted
            return

        redirectionTarget = self.reply.attribute(_nr_attr("RedirectionTargetAttribute"))

        if redirectionTarget is not None:
            newUrl = self.url.resolved(redirectionTarget)

            self.abort_request()

            ret = QtWidgets.QMessageBox.question(
                self,
                "HTTP Location redirect",
                "The server wants to redirect your request to\n%s\n\nDo you wish to follow this redirect?\n\n"
                "Any authentication details will also be forwarded!" % newUrl.toString(),
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )

            if ret == QtWidgets.QMessageBox.Yes:
                self.url = newUrl
                self.startCapabilitiesRequest(self.url)
                return

            self.update_ui()
            return

        if self.checkForHTTPErrors():
            self.abort_request()
            self.update_ui()
            return

        buf = self.reply.readAll().data()

        try:
            root = ElementTree.fromstring(buf)
        except ElementTree.ParseError as err:
            QtWidgets.QMessageBox.critical(
                self,
                "XML Parsing error",
                "The capabilities document could not be read:\n{0}".format(err.msg)
            )
            return

        if self.is_wfs20_capabilties(root):
            # WFS 2.0 Namespace
            nswfs = "{http://www.opengis.net/wfs/2.0}"
            nsxlink = "{http://www.w3.org/1999/xlink}"
            nsows = "{http://www.opengis.net/ows/1.1}"
            # GetFeature OnlineResource
            for target in root.findall("{0}OperationsMetadata/{0}Operation".format(nsows)):
                if target.get("name") == "GetFeature":
                    for subtarget in target.findall("{0}DCP/{0}HTTP/{0}Get".format(nsows)):
                        getfeatureurl = subtarget.get("{0}href".format(nsxlink))
                        if not "?" in getfeatureurl:
                            self.onlineresource = getfeatureurl
                        else:
                            self.onlineresource = getfeatureurl[:getfeatureurl.find("?")]
                            self.vendorparameters = getfeatureurl[getfeatureurl.find("?"):].replace("?", "&")
            for target in root.findall("{0}FeatureTypeList/{0}FeatureType".format(nswfs)):
                for name in target.findall("{0}Name".format(nswfs)):
                    self.ui.cmbFeatureType.addItem(name.text, name.text)
                    featuretype = FeatureType(name.text)
                    if ":" in name.text:
                        nsmap = self.get_namespace_map(buf)
                        for prefix in nsmap:
                            if prefix == name.text[:name.text.find(":")]:
                                featuretype.setNamespace(nsmap[prefix])
                                featuretype.setNamespacePrefix(prefix)
                                break
                    for title in target.findall("{0}Title".format(nswfs)):
                        featuretype.setTitle(title.text)
                    for abstract in target.findall("{0}Abstract".format(nswfs)):
                        featuretype.setAbstract(abstract.text)
                    for metadata_url in target.findall("{0}MetadataURL".format(nswfs)):
                        featuretype.setMetadataUrl(metadata_url.get("{0}href".format(nsxlink)))
                    for bbox in target.findall("{0}WGS84BoundingBox".format(nsows)):
                        for lowercorner in bbox.findall("{0}LowerCorner".format(nsows)):
                            featuretype.setWgs84BoundingBoxEast(lowercorner.text.split(' ')[0])
                            featuretype.setWgs84BoundingBoxSouth(lowercorner.text.split(' ')[1])
                        for uppercorner in bbox.findall("{0}UpperCorner".format(nsows)):
                            featuretype.setWgs84BoundingBoxWest(uppercorner.text.split(' ')[0])
                            featuretype.setWgs84BoundingBoxNorth(uppercorner.text.split(' ')[1])
                    self.featuretypes[name.text] = featuretype
                    self.querytype = "adhocquery"
        else:
            self.ui.lblMessage.setText("")

        self.update_ui()

        # Lock
        self.ui.cmdGetCapabilities.setText("List FeatureTypes")
        self.ui.cmdListStoredQueries.setVisible(True)
        self.ui.chkAuthentication.setEnabled(False)
        self.ui.txtUrl.setEnabled(False)
        self.ui.txtUsername.setEnabled(False)
        self.ui.txtPassword.setEnabled(False)

    def storedQueriesRequestFinished(self):

        if self.reply is None:
            # already aborted
            return

        if self.checkForHTTPErrors():
            self.abort_request()
            self.update_ui()
            return

        buf = self.reply.readAll().data()
        try:
            root = ElementTree.fromstring(buf)
        except ElementTree.ParseError as err:
            QtWidgets.QMessageBox.critical(
                self,
                "XML Parsing error",
                "The stored queries list could not be read:\n{0}".format(err.msg)
            )
            self.update_ui()
            return

        # WFS 2.0 Namespace
        namespace = "{http://www.opengis.net/wfs/2.0}"
        # check correct Rootelement
        if root.tag == "{0}DescribeStoredQueriesResponse".format(namespace):
            for target in root.findall("{0}StoredQueryDescription".format(namespace)):
                self.ui.cmbFeatureType.addItem(target.get("id"), target.get("id"))
                lparameter = []
                for parameter in target.findall("{0}Parameter".format(namespace)):
                    lparameter.append(StoredQueryParameter(parameter.get("name"), parameter.get("type")))
                storedquery = StoredQuery(target.get("id"), lparameter)
                for title in target.findall("{0}Title".format(namespace)):
                    storedquery.setTitle(title.text)
                for abstract in target.findall("{0}Abstract".format(namespace)):
                    storedquery.setAbstract(abstract.text)
                self.storedqueries[target.get("id")] = storedquery
                self.querytype = "storedquery"  # R
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Not a valid DescribeStoredQueries-Response!")
        self.update_ui()

    def errorOcurred(self, error_code):
        if self.reply is None:
            self.logMessage('HTTP error occurred: {0}'.format(error_code), Qgis.Warning)
        else:
            self.logMessage('HTTP error occurred: {0}'.format(self.reply.errorString(), Qgis.Warning))

    def checkForHTTPErrors(self):
        http_code = self.reply.attribute(_nr_attr("HttpStatusCodeAttribute"))

        if http_code is not None:
            self.logMessage('Request finished with HTTP code {0}'.format(http_code))
        else:
            self.logMessage('Request finished with no HTTP code (aborted?)')

        if http_code == 401:
            QtWidgets.QMessageBox.critical(
                self,
                "HTTP 401 Unauthorized",
                "Authentication is required for this request"
            )
            return True

        if http_code == 403:
            QtWidgets.QMessageBox.critical(
                self,
                "HTTP 403 Forbidden",
                "Your authentication is insufficient for this request"
            )
            return True

        if http_code == 404:
            QtWidgets.QMessageBox.critical(
                self,
                "HTTP 404 Not Found",
                "The specified resource was not found - is the URL correct?"
            )
            return True

        error = self.reply.error()
        if error != _nrep_err("NoError"):
            if not self.httpRequestAborted:
                QtWidgets.QMessageBox.critical(self, "HTTP Error",
                                               "Request failed: %s." % self.reply.errorString())
            return True

    # Process GetFeature-Request
    def getFeature(self):
        self.ui.lblMessage.setText("Please wait while downloading!")
        if self.querytype == "storedquery":
            query_string = "?service=WFS&request=GetFeature&version=2.0.0&STOREDQUERY_ID={0}".format(
                self.ui.cmbFeatureType.currentText()
            )
            storedquery = self.storedqueries[self.ui.cmbFeatureType.currentText()]
            lparameter = storedquery.getStoredQueryParameterList()
            for i in range(len(lparameter)):
                if not lparameter[i].isValidValue(self.parameter_lineedits[i].text().strip()):
                    QtWidgets.QMessageBox.critical(self, "Validation Error",
                                                   lparameter[i].getName() + ": Value validation failed!")
                    self.ui.lblMessage.setText("")
                    return
                query_string += "&{0}={1}".format(
                    urlquote(lparameter[i].getName()),
                    urlquote(self.parameter_lineedits[i].text().strip())
                )
        else:
            # FIX
            featuretype = self.featuretypes[self.ui.cmbFeatureType.currentText()]
            typeNames = urlquote(self.ui.cmbFeatureType.currentText())
            if len(self.bbox) < 1:
                query_string = "?service=WFS&request=GetFeature&version=2.0.0&srsName={0}&typeNames={1}".format(
                    self.ui.txtSrs.text().strip(), typeNames)
            else:
                query_string = "?service=WFS&request=GetFeature&version=2.0.0&srsName={0}&typeNames={1}&bbox={2}".format(
                    self.ui.txtSrs.text().strip(), typeNames, self.bbox)

            if len(featuretype.getNamespace()) > 0 and len(featuretype.getNamespacePrefix()) > 0:
                query_string += "&namespaces=xmlns({0},{1})".format(
                    featuretype.getNamespacePrefix(), urlquote(featuretype.getNamespace())
                )

            if len(self.ui.txtCount.text().strip()) > 0:
                query_string += "&count={0}".format(self.ui.txtCount.text().strip())
            # /FIX

        query_string += self.vendorparameters

        resolvedepth = self.settings.value("/Wfs20Client/resolveDepth")
        if resolvedepth:
            query_string += "&resolve=local&resolvedepth={0}".format(resolvedepth)

        self.logMessage(self.onlineresource + query_string)

        self.httpGetId = 0
        self.httpRequestAborted = False

        layername = "wfs{0}".format(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))
        self.downloadFile(self.onlineresource, query_string, self.get_temppath("{0}.gml".format(layername)))

    """
    ############################################################################################################################
    # UI
    ############################################################################################################################
    """

    # UI: Update Parameter-Frame
    def update_ui(self):

        if self.querytype == "adhocquery":
            featuretype = self.featuretypes[self.ui.cmbFeatureType.currentText()]

            if featuretype.getTitle():
                if len(featuretype.getTitle()) > 0:
                    self.ui.txtFeatureTypeTitle.setVisible(True)
                    self.ui.txtFeatureTypeTitle.setPlainText(featuretype.getTitle())
                else:
                    self.ui.txtFeatureTypeTitle.setVisible(False)
            else:
                self.ui.txtFeatureTypeTitle.setVisible(False)

            if featuretype.getAbstract():
                if len(featuretype.getAbstract()) > 0:
                    self.ui.txtFeatureTypeDescription.setVisible(True)
                    self.ui.txtFeatureTypeDescription.setPlainText(featuretype.getAbstract())
                else:
                    self.ui.txtFeatureTypeDescription.setVisible(False)
            else:
                self.ui.txtFeatureTypeDescription.setVisible(False)

            self.show_metadata_button(True)
            self.show_extent_button(True)
            self.ui.cmdGetFeature.setEnabled(True)
            self.ui.lblMessage.setText("")

        if self.querytype == "storedquery":
            storedquery = self.storedqueries[self.ui.cmbFeatureType.currentText()]

            if storedquery.getTitle():
                if len(storedquery.getTitle()) > 0:
                    self.ui.txtFeatureTypeTitle.setVisible(True)
                    self.ui.txtFeatureTypeTitle.setPlainText(storedquery.getTitle())
                else:
                    self.ui.txtFeatureTypeTitle.setVisible(False)
            else:
                self.ui.txtFeatureTypeTitle.setVisible(False)
            if storedquery.getAbstract():
                if len(storedquery.getAbstract()) > 0:
                    self.ui.txtFeatureTypeDescription.setVisible(True)
                    self.ui.txtFeatureTypeDescription.setPlainText(storedquery.getAbstract())
                else:
                    self.ui.txtFeatureTypeDescription.setVisible(False)
            else:
                self.ui.txtFeatureTypeDescription.setVisible(False)

            self.ui.cmdGetFeature.setEnabled(True)
            self.ui.lblMessage.setText("")
            self.layout_reset()
            for parameter in storedquery.getStoredQueryParameterList():
                self.layout_add_parameter(parameter)

    # UI: Update Extent-Frame
    def update_extent_frame(self):
        if self.ui.chkExtent.isChecked():
            canvas = self.plugin.iface.mapCanvas()
            ext = canvas.extent()
            self.ui.txtExtentWest.setText('%s' % ext.xMinimum())
            self.ui.txtExtentEast.setText('%s' % ext.xMaximum())
            self.ui.txtExtentNorth.setText('%s' % ext.yMaximum())
            self.ui.txtExtentSouth.setText('%s' % ext.yMinimum())

            if (isAxisOrderLatLon(self.ui.txtSrs.text().strip())):
                self.bbox = '%s' % ext.yMinimum() + "," + '%s' % ext.xMinimum() + "," + '%s' % ext.yMaximum() + "," + '%s' % ext.xMaximum() + ",{0}".format(self.ui.txtSrs.text().strip())
            else:
                self.bbox = '%s' % ext.xMinimum() + "," + '%s' % ext.yMinimum() + "," + '%s' % ext.xMaximum() + "," + '%s' % ext.yMaximum() + ",{0}".format(self.ui.txtSrs.text().strip())
        else:
            self.ui.txtExtentWest.setText("")
            self.ui.txtExtentEast.setText("")
            self.ui.txtExtentNorth.setText("")
            self.ui.txtExtentSouth.setText("")
            self.bbox = ""

    # UI: Update Main-Frame / Enable|Disable Authentication
    def update_authentication(self):
        if not self.ui.chkAuthentication.isChecked():
            self.ui.frmMain.setGeometry(QtCore.QRect(10, 90, 501, 551))
            self.ui.txtUsername.setVisible(False)
            self.ui.txtPassword.setVisible(False)
            self.ui.lblUsername.setVisible(False)
            self.ui.lblPassword.setVisible(False)
            self.resize(516, 648)
        else:
            self.ui.frmMain.setGeometry(QtCore.QRect(10, 150, 501, 551))
            self.ui.txtUsername.setVisible(True)
            self.ui.txtPassword.setVisible(True)
            self.ui.lblUsername.setVisible(True)
            self.ui.lblPassword.setVisible(True)
            self.resize(516, 704)

    # GridLayout reset (StoredQueries)
    def layout_reset(self):
        for qlabel in self.parameter_labels:
            self.ui.gridLayout.removeWidget(qlabel)
            qlabel.setParent(None)  # http://www.riverbankcomputing.com/pipermail/pyqt/2008-March/018803.html

        for qlineedit in self.parameter_lineedits:
            self.ui.gridLayout.removeWidget(qlineedit)
            qlineedit.setParent(None)  # http://www.riverbankcomputing.com/pipermail/pyqt/2008-March/018803.html

        del self.parameter_labels[:]
        del self.parameter_lineedits[:]
        self.columnid = 0

    # GridLayout addParameter (StoredQueries)
    def layout_add_parameter(self, storedqueryparameter):
        qlineedit = QtWidgets.QLineEdit()
        qlabelname = QtWidgets.QLabel()
        qlabelname.setText(storedqueryparameter.getName())
        qlabeltype = QtWidgets.QLabel()
        qlabeltype.setText(storedqueryparameter.getType().replace("xsd:", ""))
        self.ui.gridLayout.addWidget(qlabelname, self.columnid, 0)
        self.ui.gridLayout.addWidget(qlineedit, self.columnid, 1)
        self.ui.gridLayout.addWidget(qlabeltype, self.columnid, 2)
        self.columnid = self.columnid + 1
        self.parameter_labels.append(qlabelname)
        self.parameter_labels.append(qlabeltype)
        self.parameter_lineedits.append(qlineedit)

    def lock_ui(self):
        self.ui.cmdGetCapabilities.setEnabled(False)
        self.ui.cmdListStoredQueries.setEnabled(False)
        self.ui.cmdGetFeature.setEnabled(False)
        self.ui.cmbFeatureType.setEnabled(False)
        self.show_metadata_button(False)
        self.show_extent_button(False)

    def unlock_ui(self):
        self.ui.cmdGetCapabilities.setEnabled(True)
        self.ui.cmdListStoredQueries.setEnabled(True)
        self.ui.cmdGetFeature.setEnabled(True)
        self.ui.cmbFeatureType.setEnabled(True)
        self.show_metadata_button(True)
        self.show_extent_button(True)

    def show_metadata_button(self, enabled):
        if enabled:
            if self.querytype == "adhocquery":
                featuretype = self.featuretypes[self.ui.cmbFeatureType.currentText()]
                if featuretype.getMetadataUrl():
                    if len(featuretype.getMetadataUrl()) > 0:
                        self.ui.cmdMetadata.setEnabled(True)
                    else:
                        self.ui.cmdMetadata.setEnabled(False)
                else:
                    self.ui.cmdMetadata.setEnabled(False)
        else:
            self.ui.cmdMetadata.setEnabled(False)

    def show_extent_button(self, enabled):
        if enabled:
            if self.querytype == "adhocquery":
                featuretype = self.featuretypes[self.ui.cmbFeatureType.currentText()]
                if featuretype.getWgs84BoundingBoxEast():
                    if float(featuretype.getWgs84BoundingBoxEast()) > 0.0:
                        self.ui.cmdExtent.setEnabled(True)
                    else:
                        self.ui.cmdExtent.setEnabled(False)
                else:
                    self.ui.cmdExtent.setEnabled(False)
        else:
            self.ui.cmdExtent.setEnabled(False)

    def show_extent(self):
        featuretype = self.featuretypes[self.ui.cmbFeatureType.currentText()]
        self.create_layer(featuretype)

    def create_layer(self, featuretype):
        layer = QgsVectorLayer("polygon?crs=epsg=4326&", featuretype.getName() + " (Extent)", "memory")
        QgsProject.instance().addMapLayer(layer)

        e = featuretype.getWgs84BoundingBoxEast()
        s = featuretype.getWgs84BoundingBoxSouth()
        w = featuretype.getWgs84BoundingBoxWest()
        n = featuretype.getWgs84BoundingBoxNorth()

        wkt = "POLYGON((" + e + " " + s + "," + e + " " + n + "," + w + " " + n + "," + w + " " + s + "," + e + " " + s + "))"
        geom = QgsGeometry.fromWkt(wkt)
        feature = QgsFeature()
        feature.setGeometry(geom)

        features = [feature]
        layer.dataProvider().addFeatures(features)
        layer.updateExtents()
        layer.reload()
        self.plugin.iface.mapCanvas().refresh()
        self.plugin.iface.zoomToActiveLayer()

    def show_metadata(self):
        featuretype = self.featuretypes[self.ui.cmbFeatureType.currentText()]
        url = featuretype.getMetadataUrl()
        if url == '':
            QtWidgets.QMessageBox.critical(self, "Metadata Error", "No metadata URL in FeatureType")
            return

        url = QtCore.QUrl(url)
        self.startMetadataRequest(url)

    """
    ############################################################################################################################
    # UTIL
    ############################################################################################################################
    """

    def logMessage(self, message, level=Qgis.Info):
        if 'QgsMessageLog' in globals():
            QgsMessageLog.logMessage(message, "Wfs20Client", level)

    def get_url(self):
        defaultwfs = self.settings.value("/Wfs20Client/defaultWfs")
        if defaultwfs:
            return defaultwfs
        else:
            return "https://www.geodaten-mv.de/dienste/inspire_au_atkis_bdlm_download"

    def get_featurelimit(self):
        defaultfeaturelimit = self.settings.value("/Wfs20Client/defaultFeatureLimit")
        if defaultfeaturelimit:
            return defaultfeaturelimit
        else:
            return "1000"

    def get_temppath(self, filename):
        tmpdir = os.path.join(tempfile.gettempdir(), 'wfs20client')
        if not os.path.exists(tmpdir):
            os.makedirs(tmpdir)
        tmpfile = os.path.join(tmpdir, filename)
        return tmpfile

    # check for OWS-Exception
    def is_exception(self, root):
        for namespace in ["{http://www.opengis.net/ows}", "{http://www.opengis.net/ows/1.1}"]:
            # check correct Rootelement
            if root.tag == "{0}ExceptionReport".format(namespace):
                for exception in root.findall("{0}Exception".format(namespace)):
                    for exception_text in exception.findall("{0}ExceptionText".format(namespace)):
                        QtWidgets.QMessageBox.critical(self, "OWS Exception",
                                                       "OWS Exception returned from the WFS:<br>" + str(exception_text.text))
                        self.ui.lblMessage.setText("")
                return True
        return False

    # check for correct WFS version (only WFS 2.0 supported)
    def is_wfs20_capabilties(self, root):
        if self.is_exception(root):
            return False
        if root.tag == "{0}WFS_Capabilities".format("{http://www.opengis.net/wfs/2.0}"):
            return True
        if root.tag == "{0}WFS_Capabilities".format("{http://www.opengis.net/wfs}"):
            QtWidgets.QMessageBox.warning(self, "Wrong WFS Version", "This Plugin has dedicated support for WFS 2.0!")
            self.ui.lblMessage.setText("")
            return False
        QtWidgets.QMessageBox.critical(self, "Error", "Not a valid WFS GetCapabilities-Response!")
        self.ui.lblMessage.setText("")
        return False

    # Check for empty GetFeature result
    def is_empty_response(self, root):
        # deegree 3.2: numberMatched="unknown" does return numberReturned="0" instead of numberReturned="unknown"
        # https://portal.opengeospatial.org/files?artifact_id=43925
        if not root.get("numberMatched") == "unknown":
            # no Features returned?
            if root.get("numberReturned") == "0":
                return True
        return False

    # Hack to fix version/acceptversions Request-Parameter
    def fix_acceptversions(self, onlineresource, connector):
        return "{0}service=WFS&acceptversions=2.0.0&request=GetCapabilities".format(connector)

    # Determine namespaces in the capabilities (including non-used)
    def get_namespace_map(self, xml):
        xml = str(xml)
        nsmap = {}
        for i in [m.start() for m in re.finditer('xmlns:', xml)]:
            j = i + 6
            prefix = xml[j:xml.find("=", j)]
            k = xml.find("\"", j)
            uri = xml[k + 1:xml.find("\"", k + 1)]

            prefix = prefix.strip()
            uri = uri.strip()

            nsmap[prefix] = uri
        return nsmap

    #############################################################################################################
    # QHttp GetFeature-Request - http://stackoverflow.com/questions/6852038/threading-in-pyqt4
    #############################################################################################################

    # QHttp Slot
    def downloadFile(self, onlineResource, queryString, fileName):
        self.lock_ui()
        url = QtCore.QUrl(onlineResource)
        if QtCore.QFile.exists(fileName):
            QtCore.QFile.remove(fileName)

        self.outFile = QtCore.QFile(fileName)
        if not self.outFile.open(_iodev_mode(_iodev_flag("WriteOnly"))):
            QtWidgets.QMessageBox.information(self, 'Error',
                                              'Unable to save the file %s: %s.' % (fileName, self.outFile.errorString()))
            self.outFile = None
            return

        self.httpRequestAborted = False
        self.ui.progressBar.setVisible(True)

        url.setUrl(onlineResource + queryString)

        self.startRequest(url)

    def startRequest(self, url):
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)
        req = QNetworkRequest(url)
        self._apply_authcfg(req)
        self.reply = self.qnam.get(req)
        if hasattr(self.reply, "errorOccurred"):
            self.reply.errorOccurred.connect(self.errorOcurred)
        else:
            try:
                self.reply.error.connect(self.errorOcurred)
            except Exception:
                pass
        self.reply.finished.connect(self.httpRequestFinished)
        self.reply.readyRead.connect(self.httpReadyRead)
        self.reply.downloadProgress.connect(self.updateDataReadProgress)

    def httpReadyRead(self):
        if self.outFile is not None:
            self.outFile.write(self.reply.readAll())

    # Currently unused
    def cancelDownload(self):
        self.abort_request()
        self.close()

        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)
        self.unlock_ui()

    # QHttp Slot
    def httpRequestFinished(self):
        if self.httpRequestAborted:
            if self.outFile is not None:
                self.outFile.close()
                self.outFile.remove()
                self.outFile = None

            self.reply.deleteLater()
            self.reply = None
            self.ui.progressBar.hide()
            return

        self.outFile.flush()
        self.outFile.close()

        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(100)

        # Parse and check only small files
        if os.path.getsize(str(self.outFile.fileName())) < 5000:
            try:
                root = ElementTree.parse(str(self.outFile.fileName())).getroot()

                if root and not self.is_exception(root):
                    if not self.is_empty_response(root):
                        self.load_vector_layer(str(self.outFile.fileName()), self.ui.cmbFeatureType.currentText())
                    else:
                        QtWidgets.QMessageBox.information(self, "Information", "0 Features returned!")
                        self.ui.lblMessage.setText("")
            except ElementTree.ParseError as err:
                QtWidgets.QMessageBox.critical(
                    self,
                    "XML Parsing error",
                    "The response could not be read:\n{0}".format(err.msg)
                )
        else:
            self.load_vector_layer(str(self.outFile.fileName()), self.ui.cmbFeatureType.currentText())

        self.unlock_ui()

    # QHttp Slot
    # Check for genuine error conditions.
    def readResponseHeader(self, responseHeader):
        if responseHeader.statusCode() not in (200, 300, 301, 302, 303, 307):
            QtWidgets.QMessageBox.critical(self, 'Error',
                                           'Download failed: %s.' % responseHeader.reasonPhrase())
            self.ui.lblMessage.setText("")
            self.abort_request()

    def updateDataReadProgress(self, bytesRead, totalBytes):
        if self.httpRequestAborted:
            return
        self.ui.progressBar.setMaximum(totalBytes)
        self.ui.progressBar.setValue(bytesRead)
        self.ui.lblMessage.setText(
            "Please wait while downloading - {0}/{1} Bytes downloaded!".format(str(bytesRead), str(totalBytes))
        )

    # QHttp Slot
    def authenticationRequired(self, reply, authenticator):
        if self._extract_authcfg(reply.request().url()):
            self.logMessage("authcfg in use; skipping basic auth prompt")
            authenticator.setUser("")
            authenticator.setPassword("")
            return
        use_authentication = self.ui.chkAuthentication.isChecked()
        username = self.ui.txtUsername.text().strip()
        password = self.ui.txtPassword.text().strip()
        previousUsername = authenticator.user()
        previousPassword = authenticator.password()

        terminate_request = False

        if not (use_authentication):
            QtWidgets.QMessageBox.critical(
                self,
                "Authentication required",
                "Authentication is required for this request"
            )
            self.ui.chkAuthentication.setChecked(True)
            self.update_authentication()
            self.ui.txtUsername.setFocus()
            terminate_request = True

        if username == '' and not terminate_request:
            QtWidgets.QMessageBox.critical(
                self,
                "Authentication required",
                "Please enter your username for this request"
            )
            self.ui.txtUsername.setFocus()
            terminate_request = True

        if username == previousUsername and password == previousPassword and not terminate_request:
            QtWidgets.QMessageBox.critical(
                self,
                "Authentication failed",
                "Authentication with username/password failed - please check and try again"
            )
            self.ui.txtUsername.setFocus()
            terminate_request = True

        if terminate_request:
            self.httpRequestAborted = True
            reply.abort()
            return

        authenticator.setUser(username)
        authenticator.setPassword(password)
        self.logMessage("Using username/password")

    def sslErrors(self, reply, errors):
        errorString = ""
        for error in errors:
            errorString += " * " + error.errorString() + "\n"

        ret = QtWidgets.QMessageBox.question(
            self,
            "Certificate validation error",
            "The following SSL validation errors have been reported:\n\n%s\n"
            "This may indicate a problem with the server and/or its certificate.\n\n"
            "Do you wish to continue anyway?" % errorString,
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if ret == QtWidgets.QMessageBox.Yes:
            self.logMessage("Ignoring SSL errors", Qgis.Warning)
            reply.ignoreSslErrors()
        else:
            self.httpRequestAborted = True

    def abort_request(self):
        if self.reply is not None:
            self.httpRequestAborted = True
            self.reply.abort()
            self.reply.deleteLater()
            self.reply = None

    def load_vector_layer(self, filename, layername):
        from qgis.PyQt.QtNetwork import QNetworkProxy

        self.ui.lblMessage.setText("Loading GML - Please wait!")
        self.logger.debug("### LOADING GML ###")

        # Configure OGR/GDAL GML-Driver
        resolvexlinkhref = self.settings.value("/Wfs20Client/resolveXpathHref")
        attributestofields = self.settings.value("/Wfs20Client/attributesToFields")
        disablenasdetection = self.settings.value("/Wfs20Client/disableNasDetection")

        gdaltimeout = "5"
        self.logger.debug("GDAL_HTTP_TIMEOUT " + gdaltimeout)
        gdal.SetConfigOption("GDAL_HTTP_TIMEOUT", gdaltimeout)

        if resolvexlinkhref is True or str(resolvexlinkhref).lower() == "true":
            gdal.SetConfigOption('GML_SKIP_RESOLVE_ELEMS', 'HUGE')
            self.logger.debug("resolveXpathHref " + str(resolvexlinkhref))
        else:
            gdal.SetConfigOption('GML_SKIP_RESOLVE_ELEMS', 'ALL')

        if attributestofields is True or str(attributestofields).lower() == "true":
            gdal.SetConfigOption('GML_ATTRIBUTES_TO_OGR_FIELDS', 'YES')
            self.logger.debug("attributesToFields " + str(attributestofields))
        else:
            gdal.SetConfigOption('GML_ATTRIBUTES_TO_OGR_FIELDS', 'NO')

        nasdetectionstring = "NAS-Operationen.xsd;NAS-Operationen_optional.xsd;AAA-Fachschema.xsd"
        if disablenasdetection is True or str(disablenasdetection).lower() == "true":
            nasdetectionstring = 'asdf/asdf/asdf'
        self.logger.debug("Using 'NAS_INDICATOR': " + nasdetectionstring)
        gdal.SetConfigOption('NAS_INDICATOR', nasdetectionstring)

        proxy = QgsNetworkAccessManager.instance().fallbackProxy()
        try:
            NO_PROXY = QNetworkProxy.ProxyType.NoProxy  # Qt6
        except AttributeError:
            NO_PROXY = QNetworkProxy.NoProxy  # Qt5

        try:
            ptype = proxy.type()  # Qt6
        except TypeError:
            ptype = proxy.type  # Qt5

        if ptype != NO_PROXY and proxy.hostName():
            proxy_string = f"{proxy.hostName()}:{proxy.port()}"
            gdal.SetConfigOption('GDAL_HTTP_PROXY', proxy_string)
            self.logger.debug("Using 'GDAL_HTTP_PROXY': " + proxy_string)
            self.logMessage('Set GDAL_HTTP_PROXY to ' + proxy_string)
            if proxy.user():
                gdal.SetConfigOption('GDAL_HTTP_PROXYUSERPWD', f"{proxy.user()}:{proxy.password()}")
                self.logger.debug("Using 'GDAL_HTTP_PROXYUSERPWD' with username " + proxy.user())
                self.logMessage('Set GDAL_HTTP_PROXYUSERPWD')

        if self.ui.chkAuthentication.isChecked() and self.ui.txtUsername.text():
            gdal.SetConfigOption('GDAL_HTTP_USERPWD',
                                 f"{self.ui.txtUsername.text()}:{self.ui.txtPassword.text()}")
            self.logger.debug("Using 'GDAL_HTTP_USERPWD' with username " + self.ui.txtUsername.text())
            self.logMessage('Set GDAL_HTTP_USERPWD')

        # Analyse GML-File
        self.logger.debug("OGR Datasource: " + filename)
        ogrdatasource = gdal.OpenEx(filename, allowed_drivers=["GML"])
        self.logger.debug("... loaded")

        if ogrdatasource is None:
            QtWidgets.QMessageBox.critical(self, "Error", "Response is not a valid QGIS-Layer!")
            self.ui.lblMessage.setText("")
            return

        # Determine the LayerCount
        ogrlayercount = ogrdatasource.GetLayerCount()
        self.logger.debug("OGR LayerCount: " + str(ogrlayercount))

        hasfeatures = False

        for i in range(0, ogrlayercount):
            j = ogrlayercount - 1 - i  # Reverse Order?
            ogrlayer = ogrdatasource.GetLayerByIndex(j)
            ogrlayername = ogrlayer.GetName()
            self.logger.debug("OGR LayerName: " + ogrlayername)

            ogrgeometrytype = ogrlayer.GetGeomType()
            self.logger.debug("OGR GeometryType: " + ogr.GeometryTypeToName(ogrgeometrytype))

            if ogrgeometrytype == 0:
                self.logger.debug("AbstractGeometry-Strategy ...")
                geomtypeids = ["1", "2", "3", "100"]
            else:
                self.logger.debug("DefaultGeometry-Strategy ...")
                geomtypeids = [str(ogrgeometrytype)]

            # Create a Layer for each GeometryType
            for geomtypeid in geomtypeids:
                qgislayername = ogrlayername
                uri = filename + "|layerid=" + str(j)
                if len(geomtypeids) > 1:
                    uri += "|subset=" + self.getsubset(geomtypeid)

                self.logger.debug("Loading QgsVectorLayer: " + uri)
                vlayer = QgsVectorLayer(uri, qgislayername, "ogr")
                vlayer.setProviderEncoding("UTF-8")  # Ignore System Encoding --> TODO: Use XML-Header

                if not vlayer.isValid():
                    QtWidgets.QMessageBox.critical(self, "Error", "Response is not a valid QGIS-Layer!")
                    self.ui.lblMessage.setText("")
                else:
                    featurecount = vlayer.featureCount()
                    if featurecount > 0:
                        hasfeatures = True
                        QgsProject.instance().addMapLayers([vlayer])
                        self.logger.debug("... added Layer! QgsFeatureCount: " + str(featurecount))
                        # self.plugin.iface.mapCanvas().zoomToFullExtent()

        if hasfeatures is False:
            QtWidgets.QMessageBox.information(self, "Information", "No Features returned!")

        self.ui.lblMessage.setText("")

    def getsubset(self, geomcode):

        if geomcode == "1":
            return "OGR_GEOMETRY='POINT' OR OGR_GEOMETRY='MultiPoint'"
        elif geomcode == "2":
            return "OGR_GEOMETRY='LineString' OR OGR_GEOMETRY='MultiLineString'"
        elif geomcode == "3":
            return "OGR_GEOMETRY='Polygon' OR OGR_GEOMETRY='MultiPolygon'"
        elif geomcode == "100":
            return "OGR_GEOMETRY='None'"
        else:
            return "OGR_GEOMETRY='Unknown'"


# MessageHandler für QtXmlPatterns (Qt5); Dummy unter Qt6
if HAS_XMLPATTERNS:
    class MessageHandler(QtXmlPatterns.QAbstractMessageHandler):
        def handleMessage(self, msg_type, description, identifier, source_location):
            if 'QgsMessageLog' in globals():
                QgsMessageLog.logMessage(str(msg_type) + description, "Wfs20Client", Qgis.Info)
else:
    class MessageHandler(object):
        pass
