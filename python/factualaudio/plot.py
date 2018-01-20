from factualaudio.data import noise
from factualaudio.decibel import to_decibels
import numpy as np

def waveform(axes, wave, sample_rate):
    return axes.plot(np.arange(0, wave.size) * (1000 / sample_rate), wave)

# Equivalent to axes.amplitude_spectrum(), but plots on an RMS amplitude scale.
# (i.e. an input sine wave of RMS amplitude X will show up as X on the plot)
def rms_amplitude_spectrum(axes, wave, noise_level=1e-14, *args, **kwargs):
    kwargs.setdefault("window", np.ones(wave.size))
    kwargs.setdefault("scale", "dB")
    # Add some noise to avoid numerical issues when converting to dB
    wave += noise(wave.size) * noise_level
    return axes.magnitude_spectrum(wave / (wave.size / np.sqrt(2)), *args, **kwargs)

def transfer_function_gain(axes, transfer_function, corner_frequency=1000):
    x = np.linspace(0, 20000, num=1000)
    return axes.semilogx(x, to_decibels(np.absolute(transfer_function(x * (1j / corner_frequency)))))
