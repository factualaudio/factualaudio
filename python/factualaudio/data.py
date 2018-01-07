import numpy as np

def sine_wave(frequency=1000, num_periods=3, samples_per_period=100, phase_radians=0):
    return np.tile(np.sin(np.linspace(0, 1, endpoint=False, num=samples_per_period) * (np.pi * 2) + phase_radians), num_periods), samples_per_period * frequency

def noise(size):
    # Use an explicit seed to guarantee deterministic output.
    return (np.random.RandomState(0).rand(size) * 2) - 1

def piano_c5():
    import soundfile as sf
    return sf.read("../data/piano-c5.flac")
