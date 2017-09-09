call "lib/waveform.plt"

set ytics

set style arrow 1 heads filled size 0.03,30 front

set arrow from 0.4,0 rto 0,0.238 arrowstyle 1
set label "RMS" at 0.4,0.1 offset 1,0 front
set arrow from 1.4,0 rto 0,1 arrowstyle 1
set label "Peak" at 1.4,0.3 offset 1,0 front
set arrow from 1.6,-1 rto 0,2 arrowstyle 1
set label "Peak-to-peak" at 1.6,0.3 offset 1,0 front

unset xtics
unset xlabel

plot [0:2] 0, sinh(sin(x*pi*2)*100)/sinh(100), 0.238

