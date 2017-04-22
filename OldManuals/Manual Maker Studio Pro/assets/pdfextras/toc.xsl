<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:outline="http://code.google.com/p/wkhtmltopdf/outline"
                xmlns="http://www.w3.org/1999/xhtml">
  <xsl:output doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"
              doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"
              indent="yes" />
  <xsl:template match="outline:outline">
    <html>
      <head>
        <title>Table of Content</title>
        <style>
	
	        <style>

	       	  	.toc_header {
		 			font: 18px 'Helvetica Neue', Arial, 'Liberation Sans', FreeSans, sans-serif;
					padding-bottom: 20px;
		        }

				.list {
					font: 18px 'Helvetica Neue', Arial, 'Liberation Sans', FreeSans, sans-serif;
				}

				.indent .list {font-size: 80%;}

				.list_item {
					padding-top: 20px;
					display: block;
					position: relative;
					height: 20px;
					margin-bottom: 10px;
					overflow-x: hidden;
				}
				
				.indent .list_item {padding-top: 0px;}

				.list_item:before {
				   	background: white;
					display:inline;
					position:absolute;
					bottom: 0px;
				    white-space: nowrap;
					font: 13px 'Helvetica Neue', Arial, 'Liberation Sans', FreeSans, sans-serif;
				    content:
				 ". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "
				". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "
				". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "
				". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "
				 ". . . . . . . . . . . . . . . . . . . . "}

				.indent {
					padding-left: 1em;
				}

				.outline_item {
					background: white;
					display:inline;
					position:absolute;
					bottom: 0px;
					padding-right: 5px;
				}

				.pagenum{
					background: white;
					position:absolute;
					padding-right:5px;
					padding-left:7px;
					right:0px;
					bottom: 0px;
					display:inline;
					font: 13px 'Helvetica Neue', Arial, 'Liberation Sans', FreeSans, sans-serif;
				}

				a{text-decoration:none; color: black;}

	        </style>

        </style>
      </head>
      <body>
        <div class="toc_header">Table of Content</div>
        <div class="list"><xsl:apply-templates select="outline:item/outline:item"/></div>
      </body>
    </html>
  </xsl:template>
  <xsl:template match="outline:item">
 	<div class="list_item">
      <xsl:if test="@title!=''">
          <a>
            <xsl:if test="@link">
              <xsl:attribute name="href"><xsl:value-of select="@link"/></xsl:attribute>
            </xsl:if>
            <xsl:if test="@backLink">
              <xsl:attribute name="name"><xsl:value-of select="@backLink"/></xsl:attribute>
            </xsl:if>
			<span class="outline_item"> <xsl:value-of select="@title" /> </span>
          </a>
			<span class="pagenum"> <xsl:value-of select="@page" /> </span>
      </xsl:if>
	</div>
	<div class="indent">
     	<div class="list">
       		<xsl:apply-templates select="outline:item"/>
    	</div>
	</div>

  </xsl:template>
</xsl:stylesheet>
