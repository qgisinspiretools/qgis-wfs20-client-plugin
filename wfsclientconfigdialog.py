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
from ui_wfsclientconfig import Ui_WfsClientConfig
from qgis.core import *


class WfsClientConfigDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_WfsClientConfig()
        self.ui.setupUi(self)

        self.settings = QtCore.QSettings()

        #Restore UI from Settings
        resolvexlinkhref = self.settings.value("/Wfs20Client/resolveXpathHref")
        attributestofields = self.settings.value("/Wfs20Client/attributesToFields")
        resolvedepth = self.settings.value("/Wfs20Client/resolveDepth")
        defaultwfs = self.settings.value("/Wfs20Client/defaultWfs")
        defaultfeaturelimit = self.settings.value("/Wfs20Client/defaultFeatureLimit")

        index = self.ui.cmbResolveDepth.findText(resolvedepth)
        self.ui.cmbResolveDepth.setCurrentIndex(index)

        if resolvexlinkhref:
            if resolvexlinkhref == "true":
                self.ui.chkResolveXlinkHref.setChecked(True)
            else:
                self.ui.chkResolveXlinkHref.setChecked(False)

        if attributestofields:
            if attributestofields == "true":
                self.ui.chkAttributesToFields.setChecked(True)
            else:
                self.ui.chkAttributesToFields.setChecked(False)

        if defaultwfs:
            self.ui.txtUrl.setText(defaultwfs)

        if defaultfeaturelimit:
            self.ui.txtFeatureLimit.setText(defaultfeaturelimit)

        QtCore.QObject.connect(self.ui.cmdSaveConfig, QtCore.SIGNAL("clicked()"), self.save_config)



    def save_config(self):
        # Save Settings
        self.settings.setValue("/Wfs20Client/resolveXpathHref", self.ui.chkResolveXlinkHref.isChecked())
        self.settings.setValue("/Wfs20Client/attributesToFields", self.ui.chkAttributesToFields.isChecked())
        self.settings.setValue("/Wfs20Client/resolveDepth", self.ui.cmbResolveDepth.currentText())
        self.settings.setValue("/Wfs20Client/defaultWfs", self.ui.txtUrl.text().strip())
        self.settings.setValue("/Wfs20Client/defaultFeatureLimit", self.ui.txtFeatureLimit.text().strip())
        QtGui.QMessageBox.information(self, "Information", "Configuration saved!")
        self.close()