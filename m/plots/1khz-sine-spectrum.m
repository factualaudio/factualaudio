% Use the same approach as piano-c5, so that the plot looks similar in terms of resolution.
[samples, sample_rate] = audioread("input/piano-c5.flac");
samples = sin([0:length(samples)-1]'*pi*2*1000/sample_rate);
plot_fft(samples, sample_rate);
format_spectrum_plot();
set(gca(), 'ylim', [55 70]);
set(gca(), 'ytick', []);
set(gca(), 'ylabel', 'Amplitude');
