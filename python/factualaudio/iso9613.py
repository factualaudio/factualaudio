# Implements formulae from ISO 9613-1:1993, "Acoustics - Attenuation of sound during propagation outdoors - Part 1: Calculation of the absorption of sound by the atmosphere"

import numpy as np

reference_ambient_pressure = 101.325
reference_temperature_kelvin = 293.15
triple_point_isotherm_kelvin = 273.16

# Section 6.2 equation (3)
def oxygen_relaxation_frequency(ambient_pressure_kpa, water_concentration_percentage):
    pa = ambient_pressure_kpa
    pr = reference_ambient_pressure
    h = water_concentration_percentage
    fro = (pa/pr)*(24+4.04e4*h*(0.02+h)/(0.391+h))
    return fro

# Section 6.2 equation (4)
def nitrogen_relaxation_frequency(ambient_pressure_kpa, water_concentration_percentage, temperature_kelvin):
    pa = ambient_pressure_kpa
    pr = reference_ambient_pressure
    h = water_concentration_percentage
    t = temperature_kelvin
    t0 = reference_temperature_kelvin
    frn = ((pa/pr)*((t/t0)**(-1/2))
        *(9+280*h*np.exp(-4.170*((t/t0)**(-1/3)-1))))
    return frn

# Section 6.2 equation (5). Result is in dB per metre.
def atmospheric_absorption_coefficient(frequency, ambient_pressure_kpa, water_concentration_percentage, temperature_kelvin):
    f = frequency
    f2 = np.square(frequency)
    pa = ambient_pressure_kpa
    pr = reference_ambient_pressure
    t = temperature_kelvin
    t0 = reference_temperature_kelvin
    fro = oxygen_relaxation_frequency(ambient_pressure_kpa, water_concentration_percentage)
    frn = nitrogen_relaxation_frequency(ambient_pressure_kpa, water_concentration_percentage, temperature_kelvin)
    alpha = 8.686*f2*((1.84e-11*((pa/pr)**-1)*((t/t0)**(1/2)))
        +((t/t0)**(-5/2))
        *(0.01275*np.exp(-2239.1/t)*((fro + (f2/fro))**-1)
        +0.1068*np.exp(-3352.0/t)*((frn+(f2/frn))**-1)))
    return alpha

# Section B.1 equations (B.1), (B.2), (B.3)
def relative_humidity_to_water_concentration(ambient_pressure_kpa, relative_humidity_percentage, temperature_kelvin):
    hr = relative_humidity_percentage
    pa = ambient_pressure_kpa
    pr = reference_ambient_pressure
    t01 = triple_point_isotherm_kelvin
    t = temperature_kelvin
    C = -6.8346*((t01/t)**1.261)+4.6151
    psat_pr = 10**C
    h = hr*psat_pr/(pa/pr)
    return h

def celsius_to_kelvin(temperature_celsius):
    return temperature_celsius + 273.15
