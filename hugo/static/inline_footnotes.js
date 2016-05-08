// Converts inline footnotes to traditional footnotes that bigfoot.js can recognize.
$(function() {
	var footnotes = $(".footnotes ol").last();
	if (!footnotes.length) footnotes = $("<ol/>").appendTo($(".footnotes").last());

	var inline_footnotes = $(".inlineFootnote");

	// We process the footnotes in two passes so that nested footnotes are handled correctly.

	// First pass: add footnote link to each inline footnote and allocate a slot in the footnote list.
	inline_footnotes.each(function() {
		var index = footnotes.children("li").length + 1;
		var id = "inline:" + index;

		var bigfootnote = $("<sup/>", {"id": "fnref:" + id}).append(
			$("<a/>", {"href": "#fn:" + id, rel: "footnote", text: index}));
		$(this).after(bigfootnote);

		var item = $("<li/>", {"id": "fn:" + id}).append(
			$("<a/>", {"href": "#fnref:" + id, "title": "return to article", text: " ↩"}));
		footnotes.append(item);
		$(this).data("inlineFootnoteItem", item);
	});

	// Second pass: move the contents of the inline footnotes into the list.
	// We process the list in reverse so that innermost footnotes are processed first.
	$(inline_footnotes.get().reverse()).each(function() {
		var contents = $(this).find(".inlineFootnoteContent").contents();
		if (!contents.length) contents = $(this).contents();
		$(this).data("inlineFootnoteItem").prepend(contents);

		$(this).remove();
	});
});
