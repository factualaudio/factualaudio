<?xml version="1.0" encoding="UTF-8" ?>
<!--
	For all input nodes that have the same |data-concatenate-into| attribute:
	- Outputs one line with the contents of the |data-concatenate-into| attribute.
	- Outputs one line with the contents of the |src| and |href| attributes (in input order).
	- Outputs an empty line as a delimiter.
	The resulting "manifest" is meant to be fed to the concatenate-assets script.
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:output method="text" />

	<!-- Muenchian grouping - see https://en.wikipedia.org/wiki/XSLT/Muenchian_grouping -->
	<xsl:key name="output-file" match="*" use="@data-concatenate-into" />
	<xsl:template match="/">
		<xsl:for-each select=".//*[@data-concatenate-into and count(. | key('output-file', @data-concatenate-into)[1]) = 1]">
			<xsl:value-of select="@data-concatenate-into" /><xsl:text>&#xa;</xsl:text>
			<xsl:for-each select="key('output-file', @data-concatenate-into)">
				<xsl:if test="@src"><xsl:value-of select="@src" /><xsl:text>&#xa;</xsl:text></xsl:if>
				<xsl:if test="@href"><xsl:value-of select="@href" /><xsl:text>&#xa;</xsl:text></xsl:if>
			</xsl:for-each>
			<xsl:text>&#xa;</xsl:text>
		</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>
