<?xml version="1.0" encoding="UTF-8" ?>
<!--
	Given an input RSS feed, and an index parameter, outputs the description of the Nth item.
	If there is no such item, outputs nothing.
	Note that counting starts from 1 (one) not zero. Ah, XPath.
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:param name="index" />
	<xsl:output method="text" />

	<xsl:template match="/">
		<xsl:if test="string-length($index) = 0">
			<xsl:message terminate="yes">ERROR: no index provided</xsl:message>
		</xsl:if>
		<xsl:if test="number($index) != $index">
			<xsl:message terminate="yes">ERROR: invalid index</xsl:message>
		</xsl:if>
		<xsl:if test="$index &lt; 1">
			<xsl:message terminate="yes">ERROR: indices start from one</xsl:message>
		</xsl:if>
		<xsl:if test="not(rss/channel/item/description)">
			<xsl:message terminate="yes">ERROR: input is not an RSS feed, or does not contain any item descriptions</xsl:message>
		</xsl:if>

		<xsl:value-of select="rss/channel/item[position() = $index]/description" />
	</xsl:template>
</xsl:stylesheet>
