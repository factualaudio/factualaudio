sample_rate = 48000;
plot_fft(repmat(min(max(sine_wave_cycle(1000, sample_rate) * 1.2, -1), 1), 1, 5), sample_rate, 1);
format_spectrum_plot();
set(gca(), 'ylim', [-60 0]);
set(gca(), 'ylabel', 'Amplitude (dB)');

ticks = [1 3 5 7 9];
set(gca(), 'xtick', ticks * 1000);
set(gca(), 'xticklabel', cellstr(num2str(ticks', '%.0fk')));

a = annotation('ellipse', [ 0.65 0.025 0.275 0.7 ]);
set(a, 'linewidth', 2);
set(a, 'edgecolor', 'red');

