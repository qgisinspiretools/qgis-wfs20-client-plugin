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
from qgis.PyQt import QtCore, QtGui, QtWidgets, uic
from qgis.core import *

UI_WFS_PATH = os.path.join(os.path.dirname(__file__), "ui_wfsclientconfig.ui")


class _UiProxy:
    """Redirects self.ui.<name> to widgets on self so that existing code remains unchanged."""
    def __init__(self, owner):
        self._o = owner
    def __getattr__(self, name):
        return getattr(self._o, name)


class WfsClientConfigDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        uic.loadUi(UI_WFS_PATH, self)
        self.ui = _UiProxy(self)

        self.settings = QgsSettings()

        #Restore UI from Settings
        resolvexlinkhref = self.settings.value("/Wfs20Client/resolveXpathHref")
        attributestofields = self.settings.value("/Wfs20Client/attributesToFields")
        disablenasdetection = self.settings.value("/Wfs20Client/disableNasDetection")
        resolvedepth = self.settings.value("/Wfs20Client/resolveDepth")
        defaultwfs = self.settings.value("/Wfs20Client/defaultWfs")
        defaultfeaturelimit = self.settings.value("/Wfs20Client/defaultFeatureLimit")

        index = self.ui.cmbResolveDepth.findText(resolvedepth)
        self.ui.cmbResolveDepth.setCurrentIndex(index)

        if resolvexlinkhref is True or resolvexlinkhref == "true":
            self.ui.chkResolveXlinkHref.setChecked(True)
        else:
            self.ui.chkResolveXlinkHref.setChecked(False)

        if attributestofields is True or attributestofields == "true":
            self.ui.chkAttributesToFields.setChecked(True)
        else:
            self.ui.chkAttributesToFields.setChecked(False)

        if disablenasdetection is True or disablenasdetection == "true":
            self.ui.chkDisableNasDetection.setChecked(True)
        else:
            self.ui.chkDisableNasDetection.setChecked(False)



        if defaultwfs:
            self.ui.txtUrl.setText(defaultwfs)

        if defaultfeaturelimit:
            self.ui.txtFeatureLimit.setText(defaultfeaturelimit)

        self.ui.cmdSaveConfig.clicked.connect(self.save_config)



    def save_config(self):
        # Save Settings
        self.settings.setValue("/Wfs20Client/resolveXpathHref", self.ui.chkResolveXlinkHref.isChecked())
        self.settings.setValue("/Wfs20Client/attributesToFields", self.ui.chkAttributesToFields.isChecked())
        self.settings.setValue("/Wfs20Client/disableNasDetection", self.ui.chkDisableNasDetection.isChecked())
        self.settings.setValue("/Wfs20Client/resolveDepth", self.ui.cmbResolveDepth.currentText())
        self.settings.setValue("/Wfs20Client/defaultWfs", self.ui.txtUrl.text().strip())
        self.settings.setValue("/Wfs20Client/defaultFeatureLimit", self.ui.txtFeatureLimit.text().strip())
        QtWidgets.QMessageBox.information(self, "Information", "Configuration saved!")
        self.close()