import numpy as np

# Equivalent to axes.amplitude_spectrum(), but plots on an RMS amplitude scale.
# (i.e. an input sine wave of RMS amplitude X will show up as X on the plot)
def rms_amplitude_spectrum(axes, wave, *args, **kwargs):
    return axes.magnitude_spectrum(wave / (wave.size / np.sqrt(2)), *args, **kwargs)
