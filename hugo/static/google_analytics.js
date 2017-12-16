// Send tracking data to Google Analytics.
//
// This is based on the Google Analytics provided code snippet from:
//   https://support.google.com/analytics/answer/1008080
//
// However, we don't follow that approach exactly - instead of having an async
// script in <head> (which has performance implications), we run the code at the
// end after all other scripts. This ensures that GA cannot block anything else
// on the page.
$(function() {
	var ga_tracking_id = 'UA-109981744-1';

	window.dataLayer = window.dataLayer || [];
	function gtag(){dataLayer.push(arguments);}
	gtag('js', new Date());
	gtag('config', ga_tracking_id);

	var script = document.createElement('script');
	script.setAttribute('src', 'https://www.googletagmanager.com/gtag/js?id=' + ga_tracking_id);
	document.head.appendChild(script);
});
