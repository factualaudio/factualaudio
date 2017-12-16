<?xml version="1.0" encoding="UTF-8" ?>
<!--
	Implements "intrinsic placeholders", also known as the "padding-bottom hack".
	If you don't know what that is, here are some pointers:
		https://www.smashingmagazine.com/2013/09/responsive-images-performance-problem-case-study/
		http://daverupert.com/2015/12/intrinsic-placeholders-with-picture/

	In practice, for elements that have the |data-intrinsic-placeholder| attribute
	set to "unprocessed", searches for a child element with an |src| attribute,
	looks it up in the specified image manifest (which can be generated by
	generated-image-manifest), changes the |data-intrinsic-placeholder| attribute
	to "processed" and adds a style attribute to the container with the following
	content:
		style="padding-top: calc((HEIGHT/WIDTH)*100%);"

	Note that this transform only fills in the dynamic data (i.e. the actual
	padding value, which depends on actual image aspect ratio); it leaves the rest
	to the CSS stylesheet, which needs to have the necessary styles to make this
	work.
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:param name="manifest" />
	<xsl:variable name="manifest-document" select="document($manifest)" />
	<xsl:key name="image-by-url" match="images/image" use="url" />

	<!-- Sanity checks -->
	<xsl:template match="/">
		<xsl:if test="not($manifest)">
			<xsl:message terminate="yes">ERROR: No manifest specified</xsl:message>
		</xsl:if>
		<xsl:if test="not($manifest-document)">
			<xsl:message terminate="yes">ERROR: Unable to load manifest</xsl:message>
		</xsl:if>
		<xsl:if test="not($manifest-document/images/image)">
			<xsl:message terminate="yes">ERROR: Invalid manifest contents (no renames found)</xsl:message>
		</xsl:if>
		<xsl:if test="$manifest-document/images/image[not(url and width and height)]">
			<xsl:message terminate="yes">ERROR: Invalid rename found in manifest</xsl:message>
		</xsl:if>
		<xsl:apply-templates />
	</xsl:template>

	<xsl:template match="*[@data-intrinsic-placeholder='unprocessed']">
		<xsl:if test="@style">
			<xsl:message terminate="yes">ERROR: placeholder already has a style attribute</xsl:message>
		</xsl:if>
		<xsl:copy>
			<xsl:variable name="img" select=".//*[@src]" />
			<xsl:if test="count($img) != 1">
				<xsl:message terminate="yes">ERROR: invalid placeholder structure</xsl:message>
			</xsl:if>
			<xsl:variable name="url" select="$img[position() = 1]/@src" />
			<xsl:for-each select="$manifest-document">
				<xsl:variable name="image" select="key('image-by-url', $url)" />
				<xsl:if test="not($image)">
					<xsl:message terminate="yes">ERROR: could not find <xsl:value-of select="$url" /></xsl:message>
				</xsl:if>
				<xsl:attribute name="style">padding-top: calc((<xsl:value-of select="$image/height" />/<xsl:value-of select="$image/width" />)*100%);</xsl:attribute>
			</xsl:for-each>
			<xsl:attribute name="data-intrinsic-placeholder">processed</xsl:attribute>

			<xsl:variable name="filtered-attributes" select="@data-intrinsic-placeholder" />
			<xsl:apply-templates select="@*[count(. | $filtered-attributes) != count($filtered-attributes)]|node()" />
		</xsl:copy>
	</xsl:template>

	<!-- By default, copy the input to the output. -->
	<xsl:template match="@*|node()">
		<xsl:copy>
			<xsl:apply-templates select="@*|node()" />
		</xsl:copy>
	</xsl:template>
</xsl:stylesheet>