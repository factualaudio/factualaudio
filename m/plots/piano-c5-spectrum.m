[samples, sample_rate] = audioread("input/piano-c5.flac");
plot_fft(samples, sample_rate);
format_spectrum_plot();
set(gca(), 'ylim', [45 60]);
set(gca(), 'ylabel', 'Amplitude');
set(gca(), 'ytick', []);
