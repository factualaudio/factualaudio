format_waveform_plot();
samples = repmat(sine_wave_cycle(1000, 48000), 1, 6);
samples += (rand(1, length(samples)) - 0.5) * 0.5;
plot(samples);
set(gca(), 'xlim', [0 length(samples)]);
set(gca(), 'ylim', [-1.5 1.5]);
set(gca(), 'xtick', []);
set(gca(), 'ytick', []);
