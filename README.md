QGIS Plugin for OGC Web Feature Service 2.0.0
=============================================

## Features

* support for WFS 2.0 (ISO 19142)
* support for BBOX-query
* support for stored queries
* support for reference resolving (resolve; resolvedepth)
* configure how QGIS will load the GML GetFeature response

## Installation

* the plugin can be installed using the QGIS Plugin Manager
* search for `wfs 2.0` and press `Install plugin`
* the plugin will be available in the `web` menu

## Note for *nix-users

* if your get an error message
  `ImportError: cannot import name 'QtXmlPatterns' from 'PyQt5'`
  it is necessary to additionally install the QtXmlPatterns library,
  which since QGIS 3.6 is not automatically installed as a requirement
  of QGIS itself.
  * example for `apt`-based distributions:
```
apt install python3-pyqt5.qtxmlpatterns
```
  * for MacOS the following command may work:
```
brew install python3-pyqt5.qtxmlpatterns
```
