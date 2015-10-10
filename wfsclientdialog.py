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

from PyQt4 import QtCore, QtGui
from PyQt4.QtNetwork import QHttp
from PyQt4 import QtXml, QtXmlPatterns
from ui_wfsclient import Ui_WfsClient
from qgis.core import *
from xml.etree import ElementTree 
from osgeo import gdal
from osgeo import ogr
import urllib
import urllib2 
import string
import random
import tempfile
import os
import os.path
import re
import logging
import epsglib
import wfs20lib
from metadataclientdialog import MetadataClientDialog

plugin_path = os.path.abspath(os.path.dirname(__file__))

class WfsClientDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.parent = parent
        self.ui = Ui_WfsClient()
        self.ui.setupUi(self)

        self.settings = QtCore.QSettings()

        logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logfile = self.get_temppath("wfs20client.log")
        logging.basicConfig(filename=logfile, level=logging.DEBUG, format=logformat)

        self.ui.frmExtent.show()
        self.ui.frmParameter.hide()
        self.ui.progressBar.setVisible(False)
        self.ui.cmdListStoredQueries.setVisible(False)

        # Load default onlineresource
        self.ui.txtUrl.setText(self.get_url())

        self.ui.txtUsername.setVisible(False)
        self.ui.txtPassword.setVisible(False)
        self.ui.lblUsername.setVisible(False)
        self.ui.lblPassword.setVisible(False)

        self.parameter_lineedits = []
        self.parameter_labels = []

        self.init_variables()

        self.onlineresource = ""
        self.vendorparameters = ""

        self.ui.lblMessage.setText("SRS is set to EPSG: {0}".format(str(self.parent.iface.mapCanvas().mapRenderer().destinationCrs().postgisSrid())))
        self.ui.txtSrs.setText("urn:ogc:def:crs:EPSG::{0}".format(str(self.parent.iface.mapCanvas().mapRenderer().destinationCrs().postgisSrid())))

        QtCore.QObject.connect(self.ui.cmdGetCapabilities, QtCore.SIGNAL("clicked()"), self.getCapabilities)
        QtCore.QObject.connect(self.ui.cmdListStoredQueries, QtCore.SIGNAL("clicked()"), self.listStoredQueries)
        QtCore.QObject.connect(self.ui.cmdGetFeature, QtCore.SIGNAL("clicked()"), self.getFeature)
        QtCore.QObject.connect(self.ui.cmdMetadata, QtCore.SIGNAL("clicked()"), self.show_metadata)
        QtCore.QObject.connect(self.ui.cmdExtent, QtCore.SIGNAL("clicked()"), self.show_extent)
        QtCore.QObject.connect(self.ui.chkExtent, QtCore.SIGNAL("clicked()"), self.update_extent_frame)
        QtCore.QObject.connect(self.ui.chkAuthentication, QtCore.SIGNAL("clicked()"), self.update_authentication)
        QtCore.QObject.connect(self.ui.cmbFeatureType, QtCore.SIGNAL("currentIndexChanged(int)"), self.update_ui)
        QtCore.QObject.connect(self.ui.txtUrl, QtCore.SIGNAL("textChanged(QString)"), self.check_url)
        self.check_url(self.ui.txtUrl.text().strip())

    def init_variables(self):
        self.columnid = 0
        self.bbox = ""
        self.querytype = ""
        self.featuretypes = {}
        self.storedqueries = {}

    # Process GetCapabilities-Request
    def getCapabilities(self):
        self.init_variables()
        self.ui.cmdGetFeature.setEnabled(False);
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
        self.ui.txtCount.setText("1000")
        self.ui.txtCount.setVisible(True)
        self.ui.lblSrs.setVisible(True)
        self.ui.txtSrs.setText("urn:ogc:def:crs:EPSG::{0}".format(str(self.parent.iface.mapCanvas().mapRenderer().destinationCrs().postgisSrid())))
        self.ui.txtSrs.setVisible(True)
        self.ui.txtFeatureTypeTitle.setVisible(False)
        self.ui.txtFeatureTypeDescription.setVisible(False)
        self.ui.lblInfo.setText("FeatureTypes")
        self.ui.lblMessage.setText("")

        try:
            self.onlineresource = self.ui.txtUrl.text().strip()
            if len(self.onlineresource) == 0:
                QtGui.QMessageBox.critical(self, "OnlineResource Error", "Not a valid OnlineResource!")
                return
            if "?" in self.onlineresource:
                request = "{0}{1}".format(self.onlineresource, self.fix_acceptversions(self.onlineresource, "&"))
            else:
                request = "{0}{1}".format(self.onlineresource, self.fix_acceptversions(self.onlineresource, "?"))
            if self.ui.chkAuthentication.isChecked():
                self.setup_urllib2(request, self.ui.txtUsername.text().strip(), self.ui.txtPassword.text().strip())
            else:
                self.setup_urllib2(request, "", "")
            self.logMessage(request)
            response = urllib2.urlopen(request, None, 10)
            buf = response.read()
        except urllib2.HTTPError, e:
            QtGui.QMessageBox.critical(self, "HTTP Error", "HTTP Error: {0}".format(e.code))
            if e.code == 401:
                self.ui.chkAuthentication.setChecked(True)
                self.update_authentication()
        except urllib2.URLError, e:
            QtGui.QMessageBox.critical(self, "URL Error", "URL Error: {0}".format(e.reason))
        else:
            # process Response
            root = ElementTree.fromstring(buf)
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
                        self.ui.cmbFeatureType.addItem(name.text,name.text)
                        featuretype = wfs20lib.FeatureType(name.text)
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
                        self.querytype="adhocquery"
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


    #Process ListStoredQueries-Request
    def listStoredQueries(self):
        self.init_variables()
        self.ui.cmdGetFeature.setEnabled(False);
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
        try:
            # self.onlineresource = self.ui.txtUrl.text().trimmed()
            if not self.onlineresource:
                QtGui.QMessageBox.critical(self, "OnlineResource Error", "Not a valid OnlineResource!")
                return
            if "?" in self.onlineresource:
                request = "{0}&service=WFS&version=2.0.0&request=DescribeStoredQueries".format(self.onlineresource)
            else:
                request = "{0}?service=WFS&version=2.0.0&request=DescribeStoredQueries".format(self.onlineresource)
            request += self.vendorparameters
            if self.ui.chkAuthentication.isChecked():
                self.setup_urllib2(request, self.ui.txtUsername.text().strip(), self.ui.txtPassword.text().strip())
            else:
                self.setup_urllib2(request, "", "")
            self.logMessage(request)
            response = urllib2.urlopen(request, None, 10)
            buf = response.read()
        except urllib2.HTTPError, e:
            QtGui.QMessageBox.critical(self, "HTTP Error", "HTTP Error: {0}".format(e.code))
            if e.code == 401:
                self.ui.chkAuthentication.setChecked(True)
                self.update_authentication()
        except urllib2.URLError, e:
            QtGui.QMessageBox.critical(self, "URL Error", "URL Error: {0}".format(e.reason))
        else:
            # process Response
            root = ElementTree.fromstring(buf)
            # WFS 2.0 Namespace
            namespace = "{http://www.opengis.net/wfs/2.0}"
            # check correct Rootelement
            if root.tag == "{0}DescribeStoredQueriesResponse".format(namespace):
                for target in root.findall("{0}StoredQueryDescription".format(namespace)):
                    self.ui.cmbFeatureType.addItem(target.get("id"),target.get("id"))
                    lparameter = []
                    for parameter in target.findall("{0}Parameter".format(namespace)):
                        lparameter.append(wfs20lib.StoredQueryParameter(parameter.get("name"), parameter.get("type")))
                    storedquery = wfs20lib.StoredQuery(target.get("id"), lparameter)
                    for title in target.findall("{0}Title".format(namespace)):
                        storedquery.setTitle(title.text)
                    for abstract in target.findall("{0}Abstract".format(namespace)):
                        storedquery.setAbstract(abstract.text)
                    self.storedqueries[target.get("id")] = storedquery
                    self.querytype="storedquery" #R
            else:
                QtGui.QMessageBox.critical(self, "Error", "Not a valid DescribeStoredQueries-Response!")
            self.update_ui()


    # Process GetFeature-Request
    def getFeature(self):
        self.ui.lblMessage.setText("Please wait while downloading!")
        if self.querytype == "storedquery":
            query_string = "?service=WFS&request=GetFeature&version=2.0.0&STOREDQUERY_ID={0}".format(self.ui.cmbFeatureType.currentText())
            storedquery = self.storedqueries[self.ui.cmbFeatureType.currentText()]
            lparameter = storedquery.getStoredQueryParameterList()
            for i in range(len(lparameter)):
                if not lparameter[i].isValidValue(self.parameter_lineedits[i].text().strip()):
                    QtGui.QMessageBox.critical(self, "Validation Error", lparameter[i].getName() + ": Value validation failed!")
                    self.ui.lblMessage.setText("")
                    return
                query_string+= "&{0}={1}".format(lparameter[i].getName(),self.parameter_lineedits[i].text().strip())
        else :
            # FIX
            featuretype = self.featuretypes[self.ui.cmbFeatureType.currentText()]
            if len(self.bbox) < 1:
                query_string = "?service=WFS&request=GetFeature&version=2.0.0&srsName={0}&typeNames={1}".format(self.ui.txtSrs.text().strip(), self.ui.cmbFeatureType.currentText())
            else:
                filterString='<fes:Filter xmlns:fes="http://www.opengis.net/fes/2.0" xmlns:gml="http://www.opengis.net/gml/3.2"><fes:BBOX><gml:Envelope srsName="{0}"><gml:lowerCorner>{1} {2}</gml:lowerCorner><gml:upperCorner>{3} {4}</gml:upperCorner></gml:Envelope></fes:BBOX></fes:Filter>'.format(self.ui.txtSrs.text().strip(),self.bbox.split(',')[0],self.bbox.split(',')[1],self.bbox.split(',')[2],self.bbox.split(',')[3])
                query_string = "?service=WFS&request=GetFeature&version=2.0.0&srsName={0}&typeNames={1}&filter={2}".format(self.ui.txtSrs.text().strip(), self.ui.cmbFeatureType.currentText(), urllib.quote_plus(filterString))

            if len(featuretype.getNamespace()) > 0 and len(featuretype.getNamespacePrefix()) > 0:
                #query_string += "&namespace=xmlns({0}={1})".format(featuretype.getNamespacePrefix(), urllib.quote(featuretype.getNamespace(),""))
                query_string += "&namespaces=xmlns({0},{1})".format(featuretype.getNamespacePrefix(), urllib.quote(featuretype.getNamespace(),""))

            if len(self.ui.txtCount.text().strip()) > 0:
                query_string+= "&count={0}".format(self.ui.txtCount.text().strip())
            # /FIX

        query_string+=self.vendorparameters

        resolvedepth = self.settings.value("/Wfs20Client/resolveDepth")
        if resolvedepth:
            query_string+="&resolvedepth={0}".format(resolvedepth)

        self.logMessage(self.onlineresource + query_string)

        self.httpGetId = 0
        self.httpRequestAborted = False

        self.setup_qhttp()
        self.http.requestFinished.connect(self.httpRequestFinished)
        self.http.dataReadProgress.connect(self.updateDataReadProgress)
        self.http.responseHeaderReceived.connect(self.readResponseHeader)
        self.http.authenticationRequired.connect(self.authenticationRequired)
        self.http.sslErrors.connect(self.sslErrors)

        layername="wfs{0}".format(''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6)))
        self.downloadFile(self.onlineresource, query_string, self.get_temppath("{0}.gml".format(layername)))


    """
    ############################################################################################################################
    # UI
    ############################################################################################################################
    """


    # UI: Update SSL-Warning
    def check_url(self, url):
        if (url.startswith("https")):
            self.ui.lblWarning.setVisible(True)
        else:
            self.ui.lblWarning.setVisible(False)

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
            canvas=self.parent.iface.mapCanvas()
            ext=canvas.extent()
            self.ui.txtExtentWest.setText('%s'%ext.xMinimum())
            self.ui.txtExtentEast.setText('%s'%ext.xMaximum())
            self.ui.txtExtentNorth.setText('%s'%ext.yMaximum())
            self.ui.txtExtentSouth.setText('%s'%ext.yMinimum())

            if (epsglib.isAxisOrderLatLon(self.ui.txtSrs.text().strip())):
                self.bbox='%s'%ext.yMinimum() + "," + '%s'%ext.xMinimum() + "," + '%s'%ext.yMaximum() + "," + '%s'%ext.xMaximum() + ",{0}".format(self.ui.txtSrs.text().strip())
            else:
                self.bbox='%s'%ext.xMinimum() + "," + '%s'%ext.yMinimum() + "," + '%s'%ext.xMaximum() + "," + '%s'%ext.yMaximum() + ",{0}".format(self.ui.txtSrs.text().strip())
        else:
            self.ui.txtExtentWest.setText("")
            self.ui.txtExtentEast.setText("")
            self.ui.txtExtentNorth.setText("")
            self.ui.txtExtentSouth.setText("")
            self.bbox=""

    # UI: Update Main-Frame / Enable|Disable Authentication
    def update_authentication(self):
        if not self.ui.chkAuthentication.isChecked():
            self.ui.frmMain.setGeometry(QtCore.QRect(10,90,501,551))
            self.ui.txtUsername.setVisible(False)
            self.ui.txtPassword.setVisible(False)
            self.ui.lblUsername.setVisible(False)
            self.ui.lblPassword.setVisible(False)
            self.resize(516, 648)
        else:
            self.ui.frmMain.setGeometry(QtCore.QRect(10,150,501,551))
            self.ui.txtUsername.setVisible(True)
            self.ui.txtPassword.setVisible(True)
            self.ui.lblUsername.setVisible(True)
            self.ui.lblPassword.setVisible(True)
            self.resize(516, 704)


    # GridLayout reset (StoredQueries)
    def layout_reset(self):
        for qlabel in self.parameter_labels:
            self.ui.gridLayout.removeWidget(qlabel)
            qlabel.setParent(None) # http://www.riverbankcomputing.com/pipermail/pyqt/2008-March/018803.html

        for qlineedit in self.parameter_lineedits:
            self.ui.gridLayout.removeWidget(qlineedit)
            qlineedit.setParent(None) # http://www.riverbankcomputing.com/pipermail/pyqt/2008-March/018803.html

        del self.parameter_labels[:]
        del self.parameter_lineedits[:]
        self.columnid = 0


    # GridLayout addParameter (StoredQueries)
    def layout_add_parameter(self, storedqueryparameter):
        qlineedit = QtGui.QLineEdit()
        qlabelname = QtGui.QLabel()
        qlabelname.setText(storedqueryparameter.getName())
        qlabeltype = QtGui.QLabel()
        qlabeltype.setText(storedqueryparameter.getType().replace("xsd:", ""))
        self.ui.gridLayout.addWidget(qlabelname, self.columnid, 0)
        self.ui.gridLayout.addWidget(qlineedit, self.columnid, 1)
        self.ui.gridLayout.addWidget(qlabeltype, self.columnid, 2)
        self.columnid = self.columnid + 1
        self.parameter_labels.append(qlabelname)
        self.parameter_labels.append(qlabeltype)
        self.parameter_lineedits.append(qlineedit)
        # newHeight = self.geometry().height() + 21
        # self.resize(self.geometry().width(), newHeight)


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
                    if featuretype.getWgs84BoundingBoxEast() > 0:
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
        layer = QgsVectorLayer("polygon?crs=epsg:4326&", featuretype.getName() + " (Extent)", "memory")
        QgsMapLayerRegistry.instance().addMapLayer(layer)

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
        self.parent.iface.mapCanvas().refresh()
        self.parent.iface.zoomToActiveLayer()


    def show_metadata(self):
        featuretype = self.featuretypes[self.ui.cmbFeatureType.currentText()]
        xslfilename = os.path.join(plugin_path, "iso19139jw.xsl")

        html = self.xsl_transform(featuretype.getMetadataUrl(), xslfilename)

        if html:
            # create and show the dialog
            dlg = MetadataClientDialog()
            dlg.ui.wvMetadata.setHtml(html)
            # show the dialog
            dlg.show()
            result = dlg.exec_()
            # See if OK was pressed
            if result == 1:
                # do something useful (delete the line containing pass and
                # substitute with your code
                pass
        else:
            QtGui.QMessageBox.critical(self, "Metadata Error", "Unable to read the Metadata")



    """
    ############################################################################################################################
    # UTIL
    ############################################################################################################################
    """

    def logMessage(self, message):
        if globals().has_key('QgsMessageLog'):
            QgsMessageLog.logMessage(message, "Wfs20Client")

    def get_url(self):
        defaultwfs = self.settings.value("/Wfs20Client/defaultWfs")
        if defaultwfs:
            return defaultwfs
        else:
            return "http://geoserv.weichand.de:8080/geoserver/wfs"

    def get_temppath(self, filename):
        tmpdir = os.path.join(tempfile.gettempdir(),'wfs20client')
        if not os.path.exists(tmpdir):
            os.makedirs(tmpdir)
        tmpfile= os.path.join(tmpdir, filename)
        return tmpfile

    # Receive Proxy from QGIS-Settings
    def getProxy(self):
        if self.settings.value("/proxy/proxyEnabled") == "true":
           proxy = "{0}:{1}".format(self.settings.value("/proxy/proxyHost"), self.settings.value("/proxy/proxyPort"))
           if proxy.startswith("http://"):
               return proxy
           else:
               return proxy
        else:
            return ""

    # Setup urllib2 (Proxy)
    def setup_urllib2(self, request, username, password):

        # Proxy-Handler
        if not self.getProxy() == "":
            if (request.startswith("https")):
                proxy_handler = urllib2.ProxyHandler({"https" : self.getProxy()})
            else:
                proxy_handler = urllib2.ProxyHandler({"http" : self.getProxy()})
        else:
            proxy_handler = urllib2.ProxyHandler({})

        # Auth-Handler
        if username and len(username) > 0 and password and len(password) > 0:

            # Auth-Handler
            password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
            password_mgr.add_password(None, request, username, password)
            auth_handler = HTTPBasicAuthHandlerLimitRetries(password_mgr)
            opener = urllib2.build_opener(proxy_handler, auth_handler)

        else:
            opener = urllib2.build_opener(proxy_handler)

        urllib2.install_opener(opener)


    # Setup Qhttp (Proxy)
    def setup_qhttp(self):
        self.http = QHttp(self)
        if not self.getProxy() == "":
            self.http.setProxy(QgsNetworkAccessManager.instance().fallbackProxy()) # Proxy


    # XSL Transformation
    def xsl_transform(self, url, xslfilename):
        try:
            self.setup_urllib2(url, "", "")
            response = urllib2.urlopen(url, None, 10)
            encoding=response.headers['content-type'].split('charset=')[-1]
            xml_source = unicode(response.read(), encoding)
        except urllib2.HTTPError, e:
            QtGui.QMessageBox.critical(self, "HTTP Error", "HTTP Error: {0}".format(e.code))
        except urllib2.URLError, e:
            QtGui.QMessageBox.critical(self, "URL Error", "URL Error: {0}".format(e.reason))
        else:
            # load xslt
            xslt_file = QtCore.QFile(xslfilename)
            xslt_file.open(QtCore.QIODevice.ReadOnly)
            xslt = unicode(xslt_file.readAll())
            xslt_file.close()

            # xslt
            qry = QtXmlPatterns.QXmlQuery(QtXmlPatterns.QXmlQuery.XSLT20)
            qry.setFocus(xml_source)
            qry.setQuery(xslt)

            xml_target = qry.evaluateToString()
            return xml_target


    # WFS 2.0 UTILS

    # check for OWS-Exception
    def is_exception(self, root):
        for namespace in ["{http://www.opengis.net/ows}", "{http://www.opengis.net/ows/1.1}"]:
        # check correct Rootelement
            if root.tag == "{0}ExceptionReport".format(namespace):
                for exception in root.findall("{0}Exception".format(namespace)):
                    for exception_text in exception.findall("{0}ExceptionText".format(namespace)):
                        QtGui.QMessageBox.critical(self, "OWS Exception", "OWS Exception returned from the WFS:<br>"+ str(exception_text.text))
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
            QtGui.QMessageBox.warning(self, "Wrong WFS Version", "This Plugin has dedicated support for WFS 2.0!")
            self.ui.lblMessage.setText("")
            return False
        QtGui.QMessageBox.critical(self, "Error", "Not a valid WFS GetCapabilities-Response!")
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
        nsmap = {}
        for i in [m.start() for m in re.finditer('xmlns:', xml)]:
            j = i + 6
            prefix = xml[j:xml.find("=", j)]
            k = xml.find("\"", j)
            uri = xml[k + 1:xml.find("\"", k + 1)]

            prefix = prefix.strip()
            # uri = uri.replace("\"","")
            uri = uri.strip()
            # text+= prefix + " " + uri + "\n"

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
        if not self.outFile.open(QtCore .QIODevice.WriteOnly):
            QtGui.QMessageBox.information(self, 'Error', 'Unable to save the file %s: %s.' % (fileName, self.outFile.errorString()))
            self.outFile = None
            return

        port = url.port()
        if port == -1:
            port = 0

        if onlineResource.startswith("https"):
            self.http.setHost(url.host(), QHttp.ConnectionModeHttps, port)
        else:
            self.http.setHost(url.host(), QHttp.ConnectionModeHttp, port)

        self.httpRequestAborted = False
        # Download the file.
        self.ui.progressBar.setVisible(True)
        self.httpGetId = self.http.get(url.path() + queryString, self.outFile)


    # Currently unused
    def cancelDownload(self):
        self.httpRequestAborted = True
        self.http.abort()
        self.close()

        self.ui.progressBar.setMaximum(1)
        self.ui.progressBar.setValue(0)
        self.unlock_ui()

    # QHttp Slot
    def httpRequestFinished(self, requestId, error):
        if requestId != self.httpGetId:
            return

        if self.httpRequestAborted:
            if self.outFile is not None:
                self.outFile.close()
                self.outFile.remove()
                self.outFile = None
            return

        self.outFile.close()

        self.ui.progressBar.setMaximum(1)
        self.ui.progressBar.setValue(1)

        if error:
            self.outFile.remove()
            QtGui.QMessageBox.critical(self, "Error", "Download failed: %s." % self.http.errorString())
        else:
            # Parse and check only small files
            if os.path.getsize(str(self.outFile.fileName())) < 5000:
                root = ElementTree.parse(str(self.outFile.fileName())).getroot()
                if not self.is_exception(root):
                    if not self.is_empty_response(root):
                        self.load_vector_layer(str(self.outFile.fileName()), self.ui.cmbFeatureType.currentText())
                    else:
                        QtGui.QMessageBox.information(self, "Information", "0 Features returned!")
                        self.ui.lblMessage.setText("")
            else:
                self.load_vector_layer(str(self.outFile.fileName()), self.ui.cmbFeatureType.currentText())

        self.ui.progressBar.setMaximum(1)
        self.ui.progressBar.setValue(0)
        self.unlock_ui()

    # QHttp Slot
        # Check for genuine error conditions.Gz
    def readResponseHeader(self, responseHeader):
        if responseHeader.statusCode() not in (200, 300, 301, 302, 303, 307):
            QtGui.QMessageBox.critical(self, 'Error',
                    'Download failed: %s.' % responseHeader.reasonPhrase())
            self.ui.lblMessage.setText("")
            self.httpRequestAborted = True
            self.http.abort()

    def updateDataReadProgress(self, bytesRead, totalBytes):
        if self.httpRequestAborted:
            return
        self.ui.progressBar.setMaximum(totalBytes)
        self.ui.progressBar.setValue(bytesRead)
        self.ui.lblMessage.setText("Please wait while downloading - {0} Bytes downloaded!".format(str(bytesRead)))

    # QHttp Slot
    def authenticationRequired(self, hostName, _, authenticator):
        authenticator.setUser(self.ui.txtUsername.text().strip())
        authenticator.setPassword(self.ui.txtPassword.text().strip())

    def sslErrors(self, errors):
        errorString = ""
        for error in errors:
            errorString+=error.errorString() + "\n"
        # QtGui.QMessageBox.critical(self, "Error", errorString)

        self.http.ignoreSslErrors()

    def load_vector_layer(self, filename, layername):

        self.ui.lblMessage.setText("Loading GML - Please wait!")
        logging.debug("### LOADING GML ###")

        # Configure OGR/GDAL GML-Driver
        resolvexlinkhref = self.settings.value("/Wfs20Client/resolveXpathHref")
        attributestofields = self.settings.value("/Wfs20Client/attributesToFields")

        gdaltimeout = "5"
        logging.debug("GDAL_HTTP_TIMEOUT " + gdaltimeout)
        gdal.SetConfigOption("GDAL_HTTP_TIMEOUT", gdaltimeout)
        if resolvexlinkhref and resolvexlinkhref == "true":
            gdal.SetConfigOption('GML_SKIP_RESOLVE_ELEMS', 'NONE')
            logging.debug("resolveXpathHref " + resolvexlinkhref)
        else:
            gdal.SetConfigOption('GML_SKIP_RESOLVE_ELEMS', 'ALL')

        if attributestofields and attributestofields == "true":
            gdal.SetConfigOption('GML_ATTRIBUTES_TO_OGR_FIELDS', 'YES')
            logging.debug("attributesToFields " + attributestofields)
        else:
            gdal.SetConfigOption('GML_ATTRIBUTES_TO_OGR_FIELDS', 'NO')


        # Analyse GML-File
        ogrdriver = ogr.GetDriverByName("GML")
        logging.debug("OGR Datasource: " + filename)
        ogrdatasource = ogrdriver.Open(filename)
        logging.debug("... loaded")

        if ogrdatasource is None:
            QtGui.QMessageBox.critical(self, "Error", "Response is not a valid QGIS-Layer!")
            self.ui.lblMessage.setText("")

        else:
            # Determine the LayerCount
            ogrlayercount = ogrdatasource.GetLayerCount()
            logging.debug("OGR LayerCount: " + str(ogrlayercount))

            hasfeatures = False


            # Load every Layer
            for i in range(0, ogrlayercount):

                j = ogrlayercount -1 - i # Reverse Order?
                ogrlayer = ogrdatasource.GetLayerByIndex(j)
                ogrlayername = ogrlayer.GetName()
                logging.debug("OGR LayerName: " + ogrlayername)

                ogrgeometrytype = ogrlayer.GetGeomType()
                logging.debug("OGR GeometryType: " + ogr.GeometryTypeToName(ogrgeometrytype))

                geomtypeids = []

                # Abstract Geometry
                if ogrgeometrytype==0:
                    logging.debug("AbstractGeometry-Strategy ...")
                    geomtypeids = ["1", "2", "3", "100"]

                # One GeometryType
                else:
                    logging.debug("DefaultGeometry-Strategy ...")
                    geomtypeids = [str(ogrgeometrytype)]


                # Create a Layer for each GeometryType
                for geomtypeid in geomtypeids:

                    qgislayername = ogrlayername # + "#" + filename
                    uri = filename + "|layerid=" + str(j)

                    if len(geomtypeids) > 1:
                        uri += "|subset=" + self.getsubset(geomtypeid)

                    logging.debug("Loading QgsVectorLayer: " + uri)
                    vlayer = QgsVectorLayer(uri, qgislayername, "ogr")
                    vlayer.setProviderEncoding("UTF-8") #Ignore System Encoding --> TODO: Use XML-Header

                    if not vlayer.isValid():
                        QtGui.QMessageBox.critical(self, "Error", "Response is not a valid QGIS-Layer!")
                        self.ui.lblMessage.setText("")
                    else:
                        featurecount = vlayer.featureCount()
                        if featurecount > 0:
                            hasfeatures = True
                            QgsMapLayerRegistry.instance().addMapLayers([vlayer])
                            logging.debug("... added Layer! QgsFeatureCount: " + str(featurecount))


            if hasfeatures == False:
                QtGui.QMessageBox.information(self, "Information", "No Features returned!")

            self.ui.lblMessage.setText("")



    def getsubset(self, geomcode):

        if      geomcode == "1":    return "OGR_GEOMETRY='POINT' OR OGR_GEOMETRY='MultiPoint'"
        elif    geomcode == "2":    return "OGR_GEOMETRY='LineString' OR OGR_GEOMETRY='MultiLineString'"
        elif    geomcode == "3":    return "OGR_GEOMETRY='Polygon' OR OGR_GEOMETRY='MultiPolygon'"
        elif    geomcode == "100":  return "OGR_GEOMETRY='None'"
        else:                       return "OGR_GEOMETRY='Unknown'"



###
#
# Custom HTTPBasicAuthHandler with fix for infinite retries when submitting wrong password
# http://bugs.python.org/issue8797
# http://bugs.python.org/file20471/simpler_fix.patch
#
###

class HTTPBasicAuthHandlerLimitRetries(urllib2.HTTPBasicAuthHandler):
    def __init__(self, *args, **kwargs):
        urllib2.HTTPBasicAuthHandler.__init__(self, *args, **kwargs)

    def http_error_auth_reqed(self, authreq, host, req, headers):
        authreq = headers.get(authreq, None)
        if authreq:
            mo = urllib2.AbstractBasicAuthHandler.rx.search(authreq)
            if mo:
                if len(mo.groups()) == 3:
                    scheme, quote, realm = mo.groups()
                else:
                    scheme, realm = mo.groups()
                if scheme.lower() == 'basic':
                    return self.retry_http_basic_auth(host, req, realm)

    def retry_http_basic_auth(self, host, req, realm):
        user, pw = self.passwd.find_user_password(realm, host)
        if pw is not None:
            raw = "%s:%s" % (user, pw)
            auth = 'Basic %s' % urllib2.base64.b64encode(raw).strip()
            if req.get_header(self.auth_header, None) == auth:
                return None
            req.add_unredirected_header(self.auth_header, auth)
            #return self.parent.open(req, timeout=req.timeout)
            return self.parent.open(req)
