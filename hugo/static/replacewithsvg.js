// Replace PNG figures with their SVG equivalents.
//
// The reason why the figures are not SVG in the HTML itself is because
// "dumb clients" (like RSS readers, Pocket Article View) don't support
// SVG. Since such clients typically don't support Javascript either,
// they don't run this code and therefore use the PNG images (which are
// supported). Meanwhile, full-featured browsers will run this code, so
// they will display the visually superior SVG images.
$(function() {
	$("img[data-svg-alternative]").each(function() {
		var img = $(this);

		// We use <object>, not <img>, for SVG because fonts
		// don't work with <img> for some reason.
		var obj = $("<object/>", {"class": "fitvidsignore " + img.attr("class")}).attr("data", img.data("svg-alternative"));

		// If we hide the object, Chrome doesn't want to preload it.
		// However, setting width and height to zero seems to work.
		obj.attr("width", 0).attr("height", 0);

		// Note: it appears that behavior is suboptimal if we move the
		// object element around (especially in Chrome), so it's
		// important to add it in its final resting place.
		obj.one('load', function() {
			obj.removeAttr("width");
			obj.removeAttr("height");
			img.remove();
		});
		img.after(obj);
	});
});
