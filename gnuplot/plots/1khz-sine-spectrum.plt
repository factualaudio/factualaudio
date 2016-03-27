call "lib/input.plt"
call "lib/spectrum.plt"

set yrange [0:2]

$spectrum << EOD
1000 1.5
EOD

plot $spectrum with impulses
