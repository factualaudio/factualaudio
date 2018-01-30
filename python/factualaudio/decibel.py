import numpy as np

def to_decibels(value):
    return 20 * np.log10(value)

def from_decibels(value):
    return np.power(20, value/20)
