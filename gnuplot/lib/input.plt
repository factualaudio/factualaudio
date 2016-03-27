# If file exists, returns file. Otherwise, return garbage so that gnuplot will
# fail loudly when trying to use the file.
required_file(file) = (system("[ -e '".file."' ] && echo ok") eq "ok") ? file : 1/0

# Returns a string that can be used as a file spec for the PCM contents of an
# audio file. Requires SoX to be installed on the system.
audio_to_pcm(audiofile) = "< sox ".audiofile. " --type .dat -"

# Same as above, but outputs the spectrum.
audio_to_spectrum(audiofile) = "< sox ".audiofile." --null stat -freq 2>&1"
