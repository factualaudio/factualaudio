call "lib/waveform.plt"

set ytics
set ylabel "Sound pressure in Pa"

plot [0:2] sin(x*pi*2) * 0.356
