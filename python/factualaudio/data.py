import numpy as np

def sine_wave(num_periods=3, samples_per_period=100):
    return np.tile(np.sin(np.linspace(0, 1, endpoint=False, num=samples_per_period) * (np.pi * 2)), num_periods)

def noise(size):
    # Use an explicit seed to guarantee deterministic output.
    return (np.random.RandomState(0).rand(size) * 2) - 1

def piano_c5():
    import soundfile as sf
    return sf.read("../data/piano-c5.flac")
