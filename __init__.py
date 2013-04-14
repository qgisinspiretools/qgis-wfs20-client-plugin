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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "WFS 2.0 Client"
def description():
    return "Client for OGC Web Feature Service 2.0.0"
def category():
    return "Web"
def version():
    return "Version 0.8.4"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.7"
def author():
    return "Juergen Weichand"
def email():
    return "juergen@weichand.de"
def classFactory(iface):
    # load WfsClient class from file WfsClient
    from wfsclient import WfsClient
    return WfsClient(iface)
