<?xml version="1.0" encoding="UTF-8"?>
<!--
"""                      
/***************************************************************************
 Metadata Viewer
 
 ISO 19139 Metadata to HTML XSL-Transformation
                             - - - - - - - - 
        begin                : 2012-08-14
        update               : 2012-10-27
        copyright            : (c) 2012 by Juergen Weichand
        email                : juergen@weichand.de
        web                  : weichand.de
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
-->
<xsl:stylesheet 
    version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"    
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:csw="http://www.opengis.net/cat/csw/2.0.2"
    xmlns:gmd="http://www.isotc211.org/2005/gmd"    
    xmlns:gco="http://www.isotc211.org/2005/gco"
    xmlns:srv="http://www.isotc211.org/2005/srv"
    xmlns:wei="http://www.weichand.de"
    exclude-result-prefixes="gmd gco csw srv">
        
    <xsl:output method="html" encoding="UTF-8"/>
    
    <xsl:template name="tableRow" >
        <xsl:param name="key"/>
        <xsl:param name="value"/>
        <xsl:choose>
            <xsl:when test="string($value)">
                <tr>
                    <td>
                        <xsl:attribute name="width">
                            <xsl:value-of select="'20%'"/>                            
                        </xsl:attribute>                        
                        <xsl:value-of select="$key"/>
                    </td>
                    <td>
                        <xsl:value-of select="$value"/>
                    </td>
                </tr>
            </xsl:when>
            <xsl:otherwise></xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
    <xsl:template name="tableRowLink" >
        <xsl:param name="key"/>
        <xsl:param name="url"/>
        <xsl:param name="name"/>
        <xsl:param name="description"/>
        <xsl:choose>
            <xsl:when test="string($url)">
                <tr>
                    <td>
                        <xsl:attribute name="width">
                            <xsl:value-of select="'20%'"/>                            
                        </xsl:attribute>   
                        <xsl:value-of select="$key"/>                            
                    </td>
                    <td>
                        <a>
                            <xsl:attribute name="href">
                                <xsl:value-of select="$url"/>                            
                            </xsl:attribute>          
                            <!--
                            <xsl:attribute name="target">
                                <xsl:value-of select="'_blank'"/>                            
                            </xsl:attribute>                                   
                            -->
                            <xsl:choose>
                                <xsl:when test="string($description)">                                   
                                    <xsl:attribute name="title">
                                        <xsl:value-of select="$description"/>                            
                                    </xsl:attribute>                                   
                                </xsl:when>
                                <xsl:otherwise></xsl:otherwise>                                
                            </xsl:choose>                            
                            <xsl:choose>
                                <xsl:when test="string($name)">
                                    <xsl:value-of select="$name"/>                            
                                </xsl:when>
                                <xsl:otherwise>
                                    <xsl:value-of select="$url"/>                                                
                                </xsl:otherwise>                                
                            </xsl:choose>
                        </a>    
                    </td>                        
                </tr>
            </xsl:when>                
        </xsl:choose>
    </xsl:template>      


    
    
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <meta http-equiv="content-type" content="text/html; charset=utf-8" /> 
                <style type="text/css">
                    body {
                    color: #8B0000;
                    background: #E6E6E6;
                    font-family: Arial,Helvetica,sans-serif;	
                    font-size: 1.2em;
                    text-align: center;    
                    }

                    .top {
                    color: #000000;
                    font-size: 1.6em;
                    font-weight: bold;
                    text-align: center;    
                    }

                    .copyright {
                    color: #000000;
                    font-size: 0.6em;
                    text-align: center;    
                    }
                      
                    table {
                    text-align: center;
                    width: 852px;
                    border:1px solid #696969;
                    background: #FAFAFA;
                    margin: 1em auto;
                    border-collapse: collapse;
                    }

                    caption {
                    color: #2E2E2E;
                    font-weight: bolder;
                    font-size: 0.9em;
                    text-align: center;
                    }

                    .subcaption {
                    color: #2E2E2E;
                    font-weight: bolder;
                    font-size: 0.9em;
                    text-align: left;
                    }

                    td {
                    border:1px solid #696969;
                    color: #3F3F3F;
                    font-size: 0.8em;
                    padding: .3em 1em;
                    text-align: left;
                    }

                </style>
            </head>
            
            <body>        
                <xsl:apply-templates select="//gmd:MD_Metadata" />
                <p class="copyright">
                    Metadata Viewer - <a href="http://www.weichand.de/">http://www.weichand.de</a> - (c) Juergen Weichand<br />
                    Version: 2012-10-27
                </p>                                    
            </body>
        </html>
    </xsl:template>
    
   
    <xsl:template match="gmd:MD_Metadata">
        <table style="background: #F2F2F2"> 
            <caption>Identification Info</caption>
            <tr>
                <td>
                    <table>
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Title'"/>
                            <xsl:with-param name="value" select="gmd:identificationInfo[1]/*/gmd:citation/*/gmd:title/gco:CharacterString"/>
                        </xsl:call-template>             
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Alternate Title'"/>
                            <xsl:with-param name="value" select="gmd:identificationInfo[1]/*/gmd:citation/*/gmd:alternateTitle/gco:CharacterString"/>
                        </xsl:call-template>                                     
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Abstract'"/>
                            <xsl:with-param name="value" select="gmd:identificationInfo[1]/*/gmd:abstract/gco:CharacterString"/>
                        </xsl:call-template>
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Purpose'"/>
                            <xsl:with-param name="value" select="gmd:identificationInfo[1]/*/gmd:purpose/gco:CharacterString"/>
                        </xsl:call-template>
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Identifier'"/>
                            <xsl:with-param name="value" select="gmd:identificationInfo[1]/*/gmd:citation/*/gmd:identifier/*/gmd:code/gco:CharacterString"/>
                        </xsl:call-template>    
                        <tr>
                            <td>Date(s)</td>
                            <td>
                                <xsl:apply-templates select="gmd:identificationInfo[1]/*/gmd:citation/*/gmd:date" />
                            </td>
                        </tr>                            
                        <tr>
                            <td>Keyword(s)</td>
                            <td>
                                <xsl:apply-templates select="gmd:identificationInfo[1]/*/gmd:descriptiveKeywords" />
                            </td>
                        </tr>                              
                    </table>                                                          
                    <xsl:apply-templates select="gmd:identificationInfo[1]/*/*/gmd:EX_Extent" />
                    
                    <!-- Service -->
                    <table>
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Service Type'"/>
                            <xsl:with-param name="value" select="gmd:identificationInfo[1]/*/srv:serviceType/*"/>
                        </xsl:call-template>                                     
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Service Type Version'"/>
                            <xsl:with-param name="value" select="gmd:identificationInfo[1]/*/srv:serviceTypeVersion/gco:CharacterString"/>
                        </xsl:call-template>                           
                        <xsl:apply-templates select="gmd:identificationInfo[1]/srv:SV_ServiceIdentification" />
                    </table>
                    
                    <xsl:apply-templates select="gmd:identificationInfo[1]/*/gmd:pointOfContact/gmd:CI_ResponsibleParty" />
                </td>
            </tr>
        </table>
        
        <table style="background: #F2F2F2"> 
            <caption>Distribution Info</caption>
            <tr>
                <td>
                    <table>
                        <xsl:apply-templates select="gmd:distributionInfo[1]/*/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine" />
                    </table>
                    <xsl:apply-templates select="gmd:distributionInfo[1]/*/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty" />                                        
                </td>                
            </tr>        
        </table>  
        
        
        <table style="background: #F2F2F2"> 
            <caption>Metadata</caption>
            <tr>
                <td>
                    <table>           
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'File Identifier'"/>
                            <xsl:with-param name="value" select="gmd:fileIdentifier/gco:CharacterString"/>
                        </xsl:call-template>                          
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Language'"/>
                            <xsl:with-param name="value" select="gmd:language/*"/>
                        </xsl:call-template>                         
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Character Set'"/>
                            <xsl:with-param name="value" select="gmd:characterSet/*"/>
                        </xsl:call-template>                      
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Hierarchy Level'"/>
                            <xsl:with-param name="value" select="gmd:hierarchyLevel/*"/>
                        </xsl:call-template>  
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Hierarchy Level Name'"/>
                            <xsl:with-param name="value" select="gmd:hierarchyLevelName/gco:CharacterString"/>
                        </xsl:call-template>                                                  
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Metadata Standard Name'"/>
                            <xsl:with-param name="value" select="gmd:metadataStandardName/gco:CharacterString"/>
                        </xsl:call-template>  
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Metadata Standard Version'"/>
                            <xsl:with-param name="value" select="gmd:metadataStandardVersion/gco:CharacterString"/>
                        </xsl:call-template>                        
                        <xsl:call-template name="tableRow">
                            <xsl:with-param name="key" select="'Date Stamp'"/>
                            <xsl:with-param name="value" select="gmd:dateStamp/*"/>
                        </xsl:call-template>                                                    
                    </table>                    
                    <table>
                        <xsl:apply-templates select="gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier" />
                    </table>
                    <xsl:apply-templates select="gmd:contact/gmd:CI_ResponsibleParty" />
                </td>                
            </tr>        
        </table>
    </xsl:template>
    
    
    <!-- ##################################################################################### -->
    
    <xsl:template match="gmd:descriptiveKeywords">
        <xsl:for-each select="gmd:MD_Keywords/gmd:keyword/gco:CharacterString">
            <xsl:value-of select="."/>
            <br />
        </xsl:for-each>
    </xsl:template>
    
    <xsl:template match="gmd:date">
        <xsl:for-each select=".">
            <xsl:variable name="date">
                <xsl:value-of select="gmd:CI_Date/gmd:date/*"/>
            </xsl:variable>
            <xsl:variable name="dateType">
                <xsl:value-of select="gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode/@codeListValue"/>
            </xsl:variable>            
            <xsl:value-of select="concat($date, ' (', $dateType, ')')"/>
            <br />            
        </xsl:for-each>
    </xsl:template>    

    <xsl:template match="gmd:RS_Identifier">       
        <xsl:call-template name="tableRow">
            <xsl:with-param name="key" select="gmd:codeSpace/gco:CharacterString"/>
            <xsl:with-param name="value" select="gmd:code/gco:CharacterString"/>
        </xsl:call-template>  
    </xsl:template>
    <!--gmd:version/gco:CharacterString -->
    
    <xsl:template match="gmd:EX_Extent">       
        <table> 
            <!-- <caption>Extent</caption> -->
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Description'"/>
                <xsl:with-param name="value" select="gmd:description/gco:CharacterString"/>
            </xsl:call-template>  
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'East Bound Longitude'"/>
                <xsl:with-param name="value" select="gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/*"/>
            </xsl:call-template>                    
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'North Bound Latitude'"/>
                <xsl:with-param name="value" select="gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/*"/>
            </xsl:call-template>                
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'West Bound Longitude'"/>
                <xsl:with-param name="value" select="gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/*"/>
            </xsl:call-template>                
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'South Bound Latitude'"/>
                <xsl:with-param name="value" select="gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/*"/>
            </xsl:call-template>                            
        </table>
    </xsl:template>    
    
    <xsl:template match="gmd:CI_ResponsibleParty">        
        <table>           
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Individual Name'"/>
                <xsl:with-param name="value" select="gmd:individualName/gco:CharacterString"/>
            </xsl:call-template>  
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Organisation Name'"/>
                <xsl:with-param name="value" select="gmd:organisationName/gco:CharacterString"/>
            </xsl:call-template>    
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Position Name'"/>
                <xsl:with-param name="value" select="gmd:positionName/gco:CharacterString"/>
            </xsl:call-template>                      
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Telephone'"/>
                <xsl:with-param name="value" select="gmd:contactInfo/gmd:CI_Contact/gmd:phone/gmd:CI_Telephone/gmd:voice/gco:CharacterString"/>
            </xsl:call-template>  
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Facsimile'"/>
                <xsl:with-param name="value" select="gmd:contactInfo/gmd:CI_Contact/gmd:phone/gmd:CI_Telephone/gmd:facsimile/gco:CharacterString"/>
            </xsl:call-template>  
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Delivery Point'"/>
                <xsl:with-param name="value" select="gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString"/>
            </xsl:call-template>  
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Postal Code'"/>
                <xsl:with-param name="value" select="gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString"/>
            </xsl:call-template>      
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'City'"/>
                <xsl:with-param name="value" select="gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString"/>
            </xsl:call-template>     
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Administrative Area'"/>
                <xsl:with-param name="value" select="gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:administrativeArea/gco:CharacterString"/>
            </xsl:call-template>                    
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Country'"/>
                <xsl:with-param name="value" select="gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString"/>
            </xsl:call-template>                                           
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Electronic Mail Address'"/>
                <xsl:with-param name="value" select="gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString"/>
            </xsl:call-template>  
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Online Resource'"/>
                <xsl:with-param name="value" select="gmd:contactInfo/gmd:CI_Contact/gmd:onlineResource/gmd:CI_OnlineResource/gmd:linkage/*"/>
            </xsl:call-template>              
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Hours of Service'"/>
                <xsl:with-param name="value" select="gmd:contactInfo/gmd:CI_Contact/gmd:hoursOfService/gco:CharacterString"/>
            </xsl:call-template>                          
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Contact Instructions'"/>
                <xsl:with-param name="value" select="gmd:contactInfo/gmd:CI_Contact/gmd:contactInstructions/gco:CharacterString"/>
            </xsl:call-template>                       
            <!--
            <xsl:call-template name="tableRow">
                <xsl:with-param name="key" select="'Role'"/>
                <xsl:with-param name="value" select="gmd:role/gmd:CI_RoleCode/@codeListValue"/>
            </xsl:call-template>                                     
            -->                
        </table>    
    </xsl:template>
 
 
 
    <xsl:template match="gmd:onLine">
        <xsl:call-template name="tableRowLink">
            <xsl:with-param name="key" select="'Online Resource'"/>
            <xsl:with-param name="url" select="gmd:CI_OnlineResource/gmd:linkage/gmd:URL"/>
            <xsl:with-param name="name" select="gmd:CI_OnlineResource/gmd:name/gco:CharacterString"/>                
            <xsl:with-param name="description" select="gmd:CI_OnlineResource/gmd:description/gco:CharacterString"/>                                
        </xsl:call-template>  
            <!-- gmd:CI_OnlineResource/gmd:applicationProfile/gco:CharacterString -->
            <!-- gmd:CI_OnlineResource/gmd:function/gmd:CI_OnLineFunctionCode/@codeListValue -->            
    </xsl:template>

    
    <!-- SERVICE -->
    <xsl:template match="srv:SV_ServiceIdentification">     
    
        <tr>
            <td>Operations</td>
            <td>
                <xsl:for-each select="srv:containsOperations/srv:SV_OperationMetadata/srv:operationName/gco:CharacterString">
                    <xsl:value-of select="."/>
                    <br />
                </xsl:for-each>                                
            </td>
        </tr>       
         <xsl:apply-templates select="srv:operatesOn" />
    </xsl:template>         
        
    <xsl:template match="srv:operatesOn">     
        <xsl:call-template name="tableRowLink">
            <xsl:with-param name="key" select="'Operates On'"/>
            <xsl:with-param name="url" select="@xlink:href"/>
            <xsl:with-param name="name" select="@xlink:title"/>                
            <xsl:with-param name="description" select="@uuidref"/>                                
        </xsl:call-template>      
    </xsl:template>                   
        
</xsl:stylesheet>