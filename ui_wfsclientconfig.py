# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_wfsclientconfig.ui'
#
# Created: Sat Mar 21 18:01:41 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WfsClientConfig(object):
    def setupUi(self, WfsClientConfig):
        WfsClientConfig.setObjectName(_fromUtf8("WfsClientConfig"))
        WfsClientConfig.resize(541, 297)
        self.cmdSaveConfig = QtGui.QPushButton(WfsClientConfig)
        self.cmdSaveConfig.setEnabled(True)
        self.cmdSaveConfig.setGeometry(QtCore.QRect(370, 270, 161, 23))
        self.cmdSaveConfig.setObjectName(_fromUtf8("cmdSaveConfig"))
        self.frmGml = QtGui.QFrame(WfsClientConfig)
        self.frmGml.setGeometry(QtCore.QRect(10, 10, 521, 101))
        self.frmGml.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmGml.setFrameShadow(QtGui.QFrame.Raised)
        self.frmGml.setObjectName(_fromUtf8("frmGml"))
        self.chkAttributesToFields = QtGui.QCheckBox(self.frmGml)
        self.chkAttributesToFields.setGeometry(QtCore.QRect(210, 70, 21, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkAttributesToFields.setFont(font)
        self.chkAttributesToFields.setText(_fromUtf8(""))
        self.chkAttributesToFields.setObjectName(_fromUtf8("chkAttributesToFields"))
        self.lblAttributesToFields = QtGui.QLabel(self.frmGml)
        self.lblAttributesToFields.setGeometry(QtCore.QRect(20, 70, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblAttributesToFields.setFont(font)
        self.lblAttributesToFields.setObjectName(_fromUtf8("lblAttributesToFields"))
        self.lblResolveXlinkHref = QtGui.QLabel(self.frmGml)
        self.lblResolveXlinkHref.setGeometry(QtCore.QRect(20, 40, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblResolveXlinkHref.setFont(font)
        self.lblResolveXlinkHref.setObjectName(_fromUtf8("lblResolveXlinkHref"))
        self.chkResolveXlinkHref = QtGui.QCheckBox(self.frmGml)
        self.chkResolveXlinkHref.setGeometry(QtCore.QRect(210, 40, 21, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkResolveXlinkHref.setFont(font)
        self.chkResolveXlinkHref.setText(_fromUtf8(""))
        self.chkResolveXlinkHref.setObjectName(_fromUtf8("chkResolveXlinkHref"))
        self.lblGmlHeader = QtGui.QLabel(self.frmGml)
        self.lblGmlHeader.setGeometry(QtCore.QRect(10, 10, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblGmlHeader.setFont(font)
        self.lblGmlHeader.setObjectName(_fromUtf8("lblGmlHeader"))
        self.frmWfs = QtGui.QFrame(WfsClientConfig)
        self.frmWfs.setGeometry(QtCore.QRect(10, 120, 521, 141))
        self.frmWfs.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmWfs.setFrameShadow(QtGui.QFrame.Raised)
        self.frmWfs.setObjectName(_fromUtf8("frmWfs"))
        self.lblWfsHeader = QtGui.QLabel(self.frmWfs)
        self.lblWfsHeader.setGeometry(QtCore.QRect(10, 10, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblWfsHeader.setFont(font)
        self.lblWfsHeader.setObjectName(_fromUtf8("lblWfsHeader"))
        self.lblResolveDepth_2 = QtGui.QLabel(self.frmWfs)
        self.lblResolveDepth_2.setGeometry(QtCore.QRect(20, 90, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblResolveDepth_2.setFont(font)
        self.lblResolveDepth_2.setObjectName(_fromUtf8("lblResolveDepth_2"))
        self.cmbResolveDepth = QtGui.QComboBox(self.frmWfs)
        self.cmbResolveDepth.setGeometry(QtCore.QRect(20, 60, 271, 22))
        self.cmbResolveDepth.setObjectName(_fromUtf8("cmbResolveDepth"))
        self.cmbResolveDepth.addItem(_fromUtf8(""))
        self.cmbResolveDepth.setItemText(0, _fromUtf8(""))
        self.cmbResolveDepth.addItem(_fromUtf8(""))
        self.cmbResolveDepth.addItem(_fromUtf8(""))
        self.cmbResolveDepth.addItem(_fromUtf8(""))
        self.cmbResolveDepth.addItem(_fromUtf8(""))
        self.lblResolveDepth = QtGui.QLabel(self.frmWfs)
        self.lblResolveDepth.setGeometry(QtCore.QRect(20, 36, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblResolveDepth.setFont(font)
        self.lblResolveDepth.setObjectName(_fromUtf8("lblResolveDepth"))
        self.txtUrl = QtGui.QLineEdit(self.frmWfs)
        self.txtUrl.setGeometry(QtCore.QRect(20, 110, 481, 20))
        self.txtUrl.setObjectName(_fromUtf8("txtUrl"))

        self.retranslateUi(WfsClientConfig)
        QtCore.QMetaObject.connectSlotsByName(WfsClientConfig)

    def retranslateUi(self, WfsClientConfig):
        WfsClientConfig.setWindowTitle(_translate("WfsClientConfig", "WFS 2.0 Client - Config", None))
        self.cmdSaveConfig.setText(_translate("WfsClientConfig", "Save", None))
        self.lblAttributesToFields.setText(_translate("WfsClientConfig", "Convert attributes to fields", None))
        self.lblResolveXlinkHref.setText(_translate("WfsClientConfig", "Resolve elements (xlink:href)", None))
        self.lblGmlHeader.setText(_translate("WfsClientConfig", "GML-Reader (OGR/GDAL)", None))
        self.lblWfsHeader.setText(_translate("WfsClientConfig", "WFS 2.0", None))
        self.lblResolveDepth_2.setText(_translate("WfsClientConfig", "Default WFS", None))
        self.cmbResolveDepth.setItemText(1, _translate("WfsClientConfig", "1", None))
        self.cmbResolveDepth.setItemText(2, _translate("WfsClientConfig", "2", None))
        self.cmbResolveDepth.setItemText(3, _translate("WfsClientConfig", "3", None))
        self.cmbResolveDepth.setItemText(4, _translate("WfsClientConfig", "*", None))
        self.lblResolveDepth.setText(_translate("WfsClientConfig", "Resolvedepth (WFS)", None))
        self.txtUrl.setText(_translate("WfsClientConfig", "http://geoserv.weichand.de:8080/geoserver/wfs", None))

