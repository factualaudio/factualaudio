from factualaudio.data import noise
import numpy as np

# Equivalent to axes.amplitude_spectrum(), but plots on an RMS amplitude scale.
# (i.e. an input sine wave of RMS amplitude X will show up as X on the plot)
def rms_amplitude_spectrum(axes, wave, noise_level=1e-14, *args, **kwargs):
    # Add some noise to avoid numerical issues when converting to dB
    wave += noise(wave.size) * noise_level
    return axes.magnitude_spectrum(wave / (wave.size / np.sqrt(2)), *args, **kwargs)
