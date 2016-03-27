call "lib/input.plt"
call "lib/waveform.plt"

plot audio_to_pcm("input/piano-c5.flac") using ($1*1000):2 with lines,0

