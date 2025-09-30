# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MetadataClientDialog
                                 A QGIS plugin helper dialog
 Displays HTML-rendered metadata (e.g., ISO19139 via XSLT).
                             -------------------
        begin                : 2012-05-17
        author               : Your Team
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
import io
from qgis.PyQt import QtCore, QtGui, QtWidgets, uic

UI_PATH = os.path.join(os.path.dirname(__file__), "ui_metadataclient.ui")


class _UiProxy:
    """Allow dlg.ui.<name> even though widgets live directly on self."""
    def __init__(self, owner):
        self._o = owner
    def __getattr__(self, name):
        return getattr(self._o, name)


class MetadataClientDialog(QtWidgets.QDialog):
    """
    Dialog expecting a widget named 'wvMetadata' with setHtml(str) capability.
    At runtime we patch the .ui to replace QWebView (QtWebKit) with QTextBrowser (QtWidgets).
    """

    def __init__(self, parent: QtWidgets.QWidget | None = None):
        super().__init__(parent)

        loaded = False
        if os.path.exists(UI_PATH):
            try:
                # Read and patch UI XML: QWebView/QtWebKit* -> QTextBrowser/QtWidgets
                with open(UI_PATH, "r", encoding="utf-8") as f:
                    ui_xml = f.read()
                ui_xml = (ui_xml
                          .replace("QWebView", "QTextBrowser")
                          .replace("QtWebKitWidgets", "QtWidgets")
                          .replace("QtWebKit", "QtWidgets"))
                # Load from in-memory stream (avoid touching the file on disk)
                uic.loadUi(io.BytesIO(ui_xml.encode("utf-8")), self)
                loaded = True
            except Exception as e:
                # Fall back to minimal UI if patch-Load fails
                print("UI patch-load failed:", e)

        if not loaded:
            # Minimal fallback layout
            self.setLayout(QtWidgets.QVBoxLayout())
            lbl = QtWidgets.QLabel("Metadata Viewer", self)
            # Qt6 enum namespace safe alignment
            Align = getattr(QtCore.Qt, "AlignmentFlag", QtCore.Qt)
            lbl.setAlignment(Align.AlignLeft | Align.AlignVCenter)
            self.layout().addWidget(lbl)

        # ui proxy
        self.ui = _UiProxy(self)

        # Ensure we have a 'wvMetadata' widget with setHtml; if not, create a QTextBrowser
        if not hasattr(self, "wvMetadata") or self.wvMetadata is None:
            browser = QtWidgets.QTextBrowser(self)
            browser.setObjectName("wvMetadata")
            if self.layout() is None:
                self.setLayout(QtWidgets.QVBoxLayout())
            self.layout().addWidget(browser)
            self.wvMetadata = browser

        # Window title & modality (Qt6-safe)
        self.setWindowTitle("Metadata")
        try:
            self.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        except Exception:
            self.setWindowModality(QtCore.Qt.NonModal)

        # ESC closes dialog
        QtGui.QShortcut(QtGui.QKeySequence("Escape"), self, activated=self.reject)
