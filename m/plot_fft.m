function plot_fft(samples, sample_rate, supersampling_factor = 8)
	samples = [ samples; zeros(length(samples)*(supersampling_factor-1), 1) ];  % zero-pad for improved interpolation
	spectrum = fft(samples);
	plot([0:length(spectrum)-1]*sample_rate/length(spectrum), mag2db(abs(spectrum)));
endfunction
