% Generates samples for *exactly* one cycle of a sine wave.
% Assuming |sample_rate| is an integer multiple of |frequency|, the output will be perfectly periodic;
% as in, if you repeat the output multiple times, you still end up with a perfect sine.
% (This is especially useful when plotting FFTs, as Fourier really likes perfectly periodic inputs.
function samples = sine_wave_cycle(frequency, sample_rate)
	samples = sin([0:(frequency / sample_rate):1]*pi*2);
	% Because the above bounds are inclusive, the last sample is actually part of the next cycle,
	% so remove it to preserve periodicity.
	samples = samples(1:end-1);
endfunction

