function annotate_amplitude(samples)
	min_amplitude = min(samples);
	max_amplitude = max(samples);
	rms_amplitude = sqrt(meansq(samples));

	horizontal_line(min_amplitude);
	horizontal_line(0);
	horizontal_line(max_amplitude);
	horizontal_line(rms_amplitude);

	vertical_annotation(1.5, [min_amplitude max_amplitude], 0.25, 'Peak-to-peak');
	vertical_annotation(2.0, [0 max_amplitude], 0.25, 'Peak');
	vertical_annotation(2.5, [0 rms_amplitude], 0.25, 'RMS');
endfunction
