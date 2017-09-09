call "lib/waveform.plt"

set ytics

unset xtics
unset xlabel

plot [0:2] 0, sinh(sin(x*pi*2)*100)/sinh(100)

