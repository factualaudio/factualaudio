from factualaudio.plot_format import format_spectrum
import factualaudio.iso9613 as iso9613
import numpy as np

def plot_air_attenuation(axes, temperature_celsius, relative_humidity_percentage, *args, **kwargs):
    ambient_pressure_kpa = 101.325 # Mean sea level pressure
    temperature_kelvin = iso9613.celsius_to_kelvin(temperature_celsius)
    water_concentration_percentage = iso9613.relative_humidity_to_water_concentration(
            ambient_pressure_kpa, relative_humidity_percentage, temperature_kelvin)
    x = np.linspace(20, 20000, num=1000)
    return axes.semilogx(
            x, -10*iso9613.atmospheric_absorption_coefficient(x, ambient_pressure_kpa, water_concentration_percentage, temperature_kelvin),
            label=str(temperature_celsius)+' °C; '+str(relative_humidity_percentage)+' %RH', *args, **kwargs)

def populate_figure(figure):
    axes = figure.add_subplot(1, 1, 1)
    plot_air_attenuation(axes, 10, 30, linestyle='--')
    plot_air_attenuation(axes, 20, 50)
    plot_air_attenuation(axes, 30, 70, linestyle='--')
    format_spectrum(figure)
    axes.legend(loc='lower left')
    axes.set_ylim(-6, 1)
    axes.set_ylabel('Gain over 10 meters (dB)')
