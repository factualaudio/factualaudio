% From http://musicdsp.org/files/Audio-EQ-Cookbook.txt
function H = peak_transfer_function(s, peak_gain, Q)
	A = sqrt(peak_gain);
	H = abs((s.^2 .+ s .* (A ./ Q) .+ 1) ./ (s.^2 .+ s ./ (A .* Q) .+ 1));
endfunction

plot_transfer_function_gain(@(s) peak_transfer_function(s, 2, 2), 1000);

