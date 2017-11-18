// Replace PNG figures with their SVG equivalents.
//
// The reason why the figures are not SVG in the HTML itself is because
// "dumb clients" (like RSS readers, Pocket Article View) don't support
// SVG. Since such clients typically don't support Javascript either,
// they don't run this code and therefore use the PNG images (which are
// supported). Meanwhile, full-featured browsers will run this code, so
// they will display the visually superior SVG images.
$(function() {
	$("img.replacewithsvg").each(function() {
		var prefix = $(this).attr("src").split(".").slice(0, -1).join(".");
		// We use <object>, not <img>, for SVG because fonts
		// don't work with <img> for some reason.
		$(this).replaceWith($("<object/>", {"class": "fitvidsignore " + $(this).attr("class"),}).attr("data", prefix + ".svg"));
	});
});
