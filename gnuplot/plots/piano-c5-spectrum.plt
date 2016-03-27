call "lib/input.plt"
call "lib/spectrum.plt"

set yrange [0:500000]

plot audio_to_spectrum(required_file("input/piano-c5.flac")) with impulses
