# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WfsClient
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

# Import the PyQt and QGIS libraries
import os

from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.core import *

# Import the code for the dialog
from .wfsclientdialog import WfsClientDialog
from .wfsclientconfigdialog import WfsClientConfigDialog


def _icon_path(filename="icon.png"):
    """Build absolute path to an icon file located next to this module."""
    return os.path.join(os.path.dirname(__file__), filename)


def _icon(filename="icon.png"):
    """Create a QIcon from a file next to this module."""
    return QIcon(_icon_path(filename))


def _exec_dialog(dlg: QDialog) -> int:
    """Qt5/Qt6 compatible exec for dialogs."""
    try:
        return dlg.exec()     # PyQt6
    except AttributeError:
        return dlg.exec_()    # PyQt5


class WfsClient:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.clientAction = None
        self.configAction = None
        self.aboutAction = None

    def initGui(self):
        # Create actions using a file-based icon (works in Qt5 & Qt6)
        self.clientAction = QAction(_icon("icon.png"), "WFS 2.0 Client", self.iface.mainWindow())
        self.clientAction.triggered.connect(self.runClient)

        self.configAction = QAction(_icon("icon.png"), "Config", self.iface.mainWindow())
        self.configAction.triggered.connect(self.runConfig)

        self.aboutAction = QAction(_icon("icon.png"), "About", self.iface.mainWindow())
        self.aboutAction.triggered.connect(self.about)

        # Add toolbar button and menu item
        if hasattr( self.iface, "addPluginToWebMenu" ):
            self.iface.addPluginToWebMenu("&WFS 2.0 Client", self.clientAction)
            self.iface.addPluginToWebMenu("&WFS 2.0 Client", self.configAction)
            self.iface.addPluginToWebMenu("&WFS 2.0 Client", self.aboutAction)
            self.iface.addWebToolBarIcon(self.clientAction)
        else:
            self.iface.addToolBarIcon(self.clientAction)
            self.iface.addPluginToMenu("&WFS 2.0 Client", self.clientAction)
            self.iface.addPluginToMenu("&WFS 2.0 Client", self.configAction)
            self.iface.addPluginToMenu("&WFS 2.0 Client", self.aboutAction)

    def unload(self):
        # Remove the plugin menu item and icon
        if hasattr( self.iface, "addPluginToWebMenu" ):
            self.iface.removePluginWebMenu("&WFS 2.0 Client", self.clientAction)
            self.iface.removePluginWebMenu("&WFS 2.0 Client", self.configAction)
            self.iface.removePluginWebMenu("&WFS 2.0 Client", self.aboutAction)
            self.iface.removeWebToolBarIcon(self.clientAction)
        else:
            self.iface.removeToolBarIcon(self.clientAction)
            self.iface.removePluginMenu("&WFS 2.0 Client", self.clientAction)
            self.iface.removePluginMenu("&WFS 2.0 Client", self.configAction)
            self.iface.removePluginMenu("&WFS 2.0 Client", self.aboutAction)

    def about(self):
        infoString = "<table>" \
                     "<tr><td colspan=\"2\"><b>WFS 2.0 Client 0.9.11</b></td></tr>" \
                     "<tr><td colspan=\"2\"></td></tr>" \
                     "<tr><td rowspan=\"4\">Authors:</td>" \
                     "<td>J&uuml;rgen Weichand " \
                     "(<a href=\"mailto:juergen@weichand.de\">juergen@weichand.de</a>)</td></tr>" \
                     "<tr><td>Tim Vinzing</td></tr>" \
                     "<tr><td>Edward Nash " \
                     "(<a href=\"mailto:e.nash@dvz-mv.de\">e.nash@dvz-mv.de</a>)</td></tr>" \
                     "<tr><td>Wilhelm Beiche</td></tr>" \
                     "<tr><td colspan=\"2\"></td></tr>" \
                     "<tr><td>Website:</td>" \
                     "<td><a href=\"https://github.com/qgisinspiretools/qgis-wfs20-client-plugin\">" \
                     "https://github.com/qgisinspiretools/qgis-wfs20-client-plugin</a></td></tr>" \
                     "</table>"
        QMessageBox.information(self.iface.mainWindow(), "About WFS 2.0 Client", infoString)

    # run method that performs all the real work
    def runClient(self, url=None):
        # create and show the dialog
        dlg = WfsClientDialog(self.iface.mainWindow(), self, url)
        dlg.show()
        result = _exec_dialog(dlg)
        if result == 1:
            pass

    def runConfig(self):
        dlg = WfsClientConfigDialog(self.iface.mainWindow(), plugin=self)
        dlg.exec()