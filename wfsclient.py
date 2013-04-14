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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from wfsclientdialog import WfsClientDialog

class WfsClient:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/wfsclient/icon.png"), \
            "WFS 2.0 Client", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        self.aboutAction=QAction(QIcon(":/plugins/wfsclient/icon.png"), \
            "About", self.iface.mainWindow())
        QObject.connect(self.aboutAction, SIGNAL("activated()"), self.about)

        # Add toolbar button and menu item
        if hasattr( self.iface, "addPluginToWebMenu" ):
            self.iface.addPluginToWebMenu("&WFS 2.0 Client", self.action)
            self.iface.addPluginToWebMenu("&WFS 2.0 Client", self.aboutAction)
            self.iface.addWebToolBarIcon(self.action)
        else:
            self.iface.addToolBarIcon(self.action)
            self.iface.addPluginToMenu("&WFS 2.0 Client", self.action)
            self.iface.addPluginToMenu("&WFS 2.0 Client", self.aboutAction)

    def unload(self):
        # Remove the plugin menu item and icon
        if hasattr( self.iface, "addPluginToWebMenu" ):
            self.iface.removePluginWebMenu("&WFS 2.0 Client", self.action)
            self.iface.removePluginWebMenu("&WFS 2.0 Client", self.aboutAction)
            self.iface.removeWebToolBarIcon(self.action)
        else:
            self.iface.removeToolBarIcon(self.action)
            self.iface.removePluginMenu("&WFS 2.0 Client", self.action)
            self.iface.removePluginMenu("&WFS 2.0 Client", self.aboutAction)

    def about(self):
        infoString = "<table><tr><td colspan=\"2\"><b>WFS 2.0 Client 0.8.4 beta</b></td></tr><tr><td colspan=\"2\"></td></tr><tr><td>Author:</td><td>J&uuml;rgen Weichand</td></tr><tr><td>Mail:</td><td><a href=\"mailto:juergen@weichand.de\">juergen@weichand.de</a></td></tr><tr><td>Website:</td><td><a href=\"http://www.weichand.de\">http://www.weichand.de</a></td></tr></table>"
        QMessageBox.information(self.iface.mainWindow(), "About WFS 2.0 Client", infoString)

    # run method that performs all the real work
    def run(self):

        # create and show the dialog
        dlg = WfsClientDialog(self)
        # show the dialog
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass
