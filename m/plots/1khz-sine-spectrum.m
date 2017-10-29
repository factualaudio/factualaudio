sample_rate = 48000;
plot_fft(repmat(sine_wave_cycle(1000, sample_rate), 1, 5), sample_rate, 1);
format_spectrum_plot();
set(gca(), 'ylim', [-35 10]);
set(gca(), 'ytick', []);
set(gca(), 'ylabel', 'Amplitude');
