<?xml version="1.0" encoding="UTF-8" ?>
<!--
     For each item in the input RSS feed, replaces its description with the contents
     of an "N.html.xml" file (where N is the item index) from the specified directory.
     That file should contain a single <htmlbody> element whose contents are XML-escaped.
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:param name="descriptions-dir" />

	<!-- Sanity checks -->
	<xsl:template match="/">
		<xsl:if test="not($descriptions-dir)">
			<xsl:message terminate="yes">ERROR: No descriptions directory specified</xsl:message>
		</xsl:if>
		<xsl:apply-templates />
	</xsl:template>

	<xsl:template match="/rss/channel/item/description">
		<xsl:variable name="html-path" select="concat($descriptions-dir, '/', count(../preceding-sibling::item)+1, '.html.xml')" />
		<xsl:variable name="html" select="document($html-path)/htmlbody" />
		<xsl:if test="not($html)">
			<xsl:message terminate="yes">ERROR: Cannot load <xsl:value-of select="$html-path" /></xsl:message>
		</xsl:if>
		<xsl:copy>
			<xsl:value-of select="$html" />
		</xsl:copy>
	</xsl:template>

	<!-- By default, copy the input to the output. -->
	<xsl:template match="@*|node()">
		<xsl:copy>
			<xsl:apply-templates select="@*|node()" />
		</xsl:copy>
	</xsl:template>
</xsl:stylesheet>
