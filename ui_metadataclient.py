# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_metadataclient.ui'
#
# Created: Sun Apr 14 13:21:02 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MetadataClient(object):
    def setupUi(self, MetadataClient):
        MetadataClient.setObjectName(_fromUtf8("MetadataClient"))
        MetadataClient.resize(1029, 571)
        self.wvMetadata = QtWebKit.QWebView(MetadataClient)
        self.wvMetadata.setGeometry(QtCore.QRect(10, 10, 1011, 551))
        self.wvMetadata.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.wvMetadata.setObjectName(_fromUtf8("wvMetadata"))

        self.retranslateUi(MetadataClient)
        QtCore.QMetaObject.connectSlotsByName(MetadataClient)

    def retranslateUi(self, MetadataClient):
        MetadataClient.setWindowTitle(QtGui.QApplication.translate("MetadataClient", "WFS 2.0 Client - Metadata Viewer", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
