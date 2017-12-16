<?xml version="1.0" encoding="UTF-8" ?>
<!-- Outputs a HTML5 doctype, followed by the input, untouched. -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:template match="/">
		<!-- xsltproc doesn't know about HTML5 doctypes, so hack it together using xsl:text. -->
		<xsl:text disable-output-escaping="yes"><![CDATA[<!DOCTYPE html>]]>&#xa;</xsl:text>
		<xsl:apply-templates />
	</xsl:template>

	<xsl:template match="@*|node()">
		<xsl:copy>
			<xsl:apply-templates select="@*|node()" />
		</xsl:copy>
	</xsl:template>
</xsl:stylesheet>
