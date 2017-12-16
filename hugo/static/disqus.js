// Call Disqus to add comment functionality.
//
// This is based on the Disqus provided code snippet from:
//   https://help.disqus.com/customer/portal/articles/472097-universal-embed-code
$(function() {
	var script = document.createElement('script');
	script.setAttribute('src', 'https://factualaudio.disqus.com/embed.js');
	script.setAttribute('data-timestamp', +new Date());
	document.head.appendChild(script);
});
