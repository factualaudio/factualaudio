from math import inf, isnan
import numpy as np

def xy_to_complex(xy):
    return xy[0] + 1j*xy[1]

def complex_to_xy(comp):
    return [np.real(comp), np.imag(comp)]

def complex_plane(width=1000, height=1000, centered=True):
    x, x_step = np.linspace(0, 1, num=width, endpoint=False, retstep=True)
    y, y_step = np.linspace(0, 1, num=height, endpoint=False, retstep=True)
    if centered:
        x += 0 if isnan(x_step) else (x_step / 2)
        y += 0 if isnan(y_step) else (y_step / 2)
    return x[np.newaxis,:] + 1j*y[:,np.newaxis]

def distance_plane(complex_plane, point):
    return np.abs(complex_plane - point)

def waveform_plane(distance_plane, cycle_count=inf):
    source_phase = np.pi/2 - (cycle_count % 1) * 2*np.pi if cycle_count != inf else 0
    phase_plane = distance_plane * 2*np.pi + source_phase
    wave = np.exp(1j*phase_plane)
    np.putmask(wave, distance_plane > cycle_count, 0)
    return wave

def source_waveform_plane(complex_plane, source, wavelength=1, cycle_count=inf, spreading=True, min_spreading_distance=1e-14):
    distance = distance_plane(complex_plane, source)
    source_waveform_plane = waveform_plane(distance / wavelength, cycle_count)
    if spreading: source_waveform_plane /= np.fmax(distance, min_spreading_distance)
    return source_waveform_plane

