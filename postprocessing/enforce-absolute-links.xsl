<?xml version="1.0" encoding="UTF-8" ?>
<!--
     Check that every known link attribute in the input is an absolute link,
     or at least resembles one. This is important, because most of the
     fingerprinting/concatenation assumes that we're dealing with absolute URLs
     everywhere.
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:template match="/">
		<xsl:for-each select=".//@href | .//@src | .//@data-concatenate-into | .//@data-svg-alternative">
			<xsl:if test="not(starts-with(., 'http://') or starts-with(., 'https://') or starts-with(., 'mailto:') or starts-with(., '#'))">
				<xsl:message terminate="yes">ERROR: found non-absolute URL: <xsl:value-of select="." /></xsl:message>
			</xsl:if>
		</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>
