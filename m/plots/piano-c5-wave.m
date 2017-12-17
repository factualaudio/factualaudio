[samples, sample_rate] = audioread("input/piano-c5.flac");
labels = [0:length(samples)-1]/sample_rate*1000;
plot(labels, samples);
set(gca(), 'xlim', [0 labels(end)]);
format_waveform_plot();
set(gca(), 'ytick', []);
set(gca(), 'ylabel', 'Amplitude');
