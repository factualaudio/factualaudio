call "lib/waveform.plt"

set samples 88

set ytics (-32767,-16384,0,16384,32767)
set ylabel "Sample value"

set xlabel "Time in samples"

plot [0:88] sin(x*pi*2 * 1000 / 44100) * 32767 with impulse
