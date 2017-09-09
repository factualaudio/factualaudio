call "lib/waveform.plt"

set ytics

unset xtics
unset xlabel

plot [0:2] 0, sin(x*pi*2)
