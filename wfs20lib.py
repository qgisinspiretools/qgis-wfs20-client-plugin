"""
/***************************************************************************
 WFS 2.0 Library
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



class FeatureType(object):

    def __init__(self, name):
        self.__name__ = name
        self.__title = ""
        self.__abstract = ""
        self.__namespace = ""
        self.__namespace_prefix = ""
        self.__metadata_url = ""

        self.__wgs84bbox_east = 0
        self.__wgs84bbox_south = 0
        self.__wgs84bbox_west = 0
        self.__wgs84bbox_north = 0

    def getName(self):
        return self.__name__

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getAbstract(self):
        return self.__abstract

    def setAbstract(self, abstract):
        self.__abstract = abstract

    def getNamespace(self):
        return self.__namespace.encode('utf8')

    def setNamespace(self, namespace):
        self.__namespace = namespace.decode('utf8')

    def getNamespacePrefix(self):
        return self.__namespace_prefix

    def setNamespacePrefix(self, namespace_prefix):
        self.__namespace_prefix = namespace_prefix

    def getMetadataUrl(self):
        return self.__metadata_url

    def setMetadataUrl(self, metadata_url):
        self.__metadata_url = metadata_url


    def getWgs84BoundingBoxEast(self):        
        return self.__wgs84bbox_east

    def setWgs84BoundingBoxEast(self, east):
        self.__wgs84bbox_east = east

    def getWgs84BoundingBoxSouth(self):        
        return self.__wgs84bbox_south

    def setWgs84BoundingBoxSouth(self, south):
        self.__wgs84bbox_south = south

    def getWgs84BoundingBoxWest(self):        
        return self.__wgs84bbox_west

    def setWgs84BoundingBoxWest(self, west):
        self.__wgs84bbox_west = west

    def getWgs84BoundingBoxNorth(self):        
        return self.__wgs84bbox_north

    def setWgs84BoundingBoxNorth(self, north):
        self.__wgs84bbox_north = north
        
        

class StoredQuery(object):

    def __init__(self, name, lparameter):
        self.__name__ = name
        self.__lparameter = lparameter
        self.__title = ""
        self.__abstract = ""

    def getName(self):
        return self.__name

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getAbstract(self):
        return self.__abstract

    def setAbstract(self, abstract):
        self.__abstract = abstract

    def getStoredQueryParameterList(self):
        return self.__lparameter

class StoredQueryParameter(object):

    def __init__(self, name, type):
        self.__name = name
        self.__type = type

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def isValidValue(self, value):
        if len(value) == 0:
            return False

        # simple integer check
        if self.__type == "xsd:int" or self.__type == "xsd:integer"  or self.__type == "xsd:long":
            try:
                long(str(value))
                return True
            except ValueError:
                return False
            return True

        # simple number check
        if self.__type == "xsd:double" or self.__type == "xsd:float":
            try:
                float(str(value))
                return True
            except ValueError:
                return False
            return True
     
        return True