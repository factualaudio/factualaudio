% For best results, disable supersampling (i.e. set the factor to 1) when the input
% is known to be perfectly periodic (e.g. it's an output of sine_wave_cycle()).
% Background information: http://www.ni.com/white-paper/4278/
function plot_fft(samples, sample_rate, supersampling_factor = 8)
	supersampled_samples = [ samples, zeros(1, length(samples)*(supersampling_factor-1)) ];  % zero-pad for improved interpolation

	spectrum = fft(supersampled_samples);

	% Discard DC and mirror image (alias)
	spectrum(1) = 0;
	spectrum = spectrum(1:end/2);

	amplitude_spectrum_rms = sqrt(2) * abs(spectrum) / length(samples);

	amplitude_spectrum_db = mag2db(amplitude_spectrum_rms);

	% Sometimes the calculation can be a bit too "perfect" and we end up with -inf
	% in some places, which confuses plot().
	min_amplitude = -200;
	amplitude_spectrum_db(amplitude_spectrum_db < min_amplitude) = min_amplitude;

	plot([0:length(amplitude_spectrum_db)-1]*sample_rate/length(amplitude_spectrum_db)/2, amplitude_spectrum_db);
endfunction
