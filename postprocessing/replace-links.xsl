<?xml version="1.0" encoding="UTF-8" ?>
<!--
	Replace the contents of |src| and |href| attributes in the input
	using the specified rename manifest, which can be generated by
	the fingerprint-assets script.
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:param name="manifest" />
	<xsl:variable name="manifest-document" select="document($manifest)" />
	<xsl:key name="rename" match="renames/rename" use="from" />

	<!-- Sanity checks -->
	<xsl:template match="/">
		<xsl:if test="not($manifest)">
			<xsl:message terminate="yes">ERROR: No manifest specified</xsl:message>
		</xsl:if>
		<xsl:if test="not($manifest-document)">
			<xsl:message terminate="yes">ERROR: Unable to load manifest</xsl:message>
		</xsl:if>
		<xsl:if test="not($manifest-document/renames/rename)">
			<xsl:message terminate="yes">ERROR: Invalid manifest contents (no renames found)</xsl:message>
		</xsl:if>
		<xsl:if test="$manifest-document/renames/rename[not(from and to)]">
			<xsl:message terminate="yes">ERROR: Invalid rename found in manifest</xsl:message>
		</xsl:if>
		<xsl:apply-templates />
	</xsl:template>

	<xsl:template match="@href | @src">
		<xsl:attribute name="{name()}">
			<xsl:variable name="old-asset-uri" select="." />
			<xsl:for-each select="$manifest-document">
				<xsl:variable name="new-asset-uri" select="key('rename', $old-asset-uri)/to" />
				<xsl:choose>
					<xsl:when test="$new-asset-uri">
						<xsl:value-of select="$new-asset-uri" />
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="$old-asset-uri" />
					</xsl:otherwise>
				</xsl:choose>
			</xsl:for-each>
		</xsl:attribute>
	</xsl:template>

	<!-- By default, copy the input to the output. -->
	<xsl:template match="@*|node()">
		<xsl:copy>
			<xsl:apply-templates select="@*|node()" />
		</xsl:copy>
	</xsl:template>
</xsl:stylesheet>
