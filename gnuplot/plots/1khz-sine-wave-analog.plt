call "lib/waveform.plt"

set ytics
set ylabel "Voltage in volts"

plot [0:2] sin(x*pi*2) * 1.41
