<?xml version="1.0" encoding="UTF-8" ?>
<!--
     For all input nodes that have a |data-concatenate-into| attribute,
     move its contents intp the |src| or |href| attribute.
     This is meant to run after the concatenate-assets script,
     to make use of the newly concatenated files.
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<!-- Muenchian grouping - see https://en.wikipedia.org/wiki/XSLT/Muenchian_grouping -->
	<xsl:key name="output-file" match="*" use="@data-concatenate-into" />
	<xsl:template match="*[@data-concatenate-into]">
		<xsl:if test="count(. | key('output-file', @data-concatenate-into)[1]) = 1">
			<xsl:copy>
				<xsl:apply-templates select="@*|node()" />
				<xsl:if test="@src">
					<xsl:attribute name="src"><xsl:value-of select="@data-concatenate-into" /></xsl:attribute>
				</xsl:if>
				<xsl:if test="@href">
					<xsl:attribute name="href"><xsl:value-of select="@data-concatenate-into" /></xsl:attribute>
				</xsl:if>
			</xsl:copy>
		</xsl:if>
	</xsl:template>

	<!-- Remove the |data-concatenate-into| attributes. -->
	<xsl:template match="@data-concatenate-into" />

	<!-- By default, copy the input to the output. -->
	<xsl:template match="@*|node()">
		<xsl:copy>
			<xsl:apply-templates select="@*|node()" />
		</xsl:copy>
	</xsl:template>
</xsl:stylesheet>
