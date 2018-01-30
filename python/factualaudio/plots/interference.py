from factualaudio.decibel import from_decibels, to_decibels
import numpy as np

def populate_figure(figure):
    figure.set_figheight(2.5)
    amplitude_axes = figure.add_subplot(1, 2, 1)
    phase_axes = figure.add_subplot(1, 2, 2)

    for other_wave_amplitude_db in [0, 1, 3, 6]:
        other_wave_amplitude = from_decibels(other_wave_amplitude_db)
        # Don't include the limit values to avoid numerical instability
        other_wave_phase_deg = np.linspace(-180, 180, num=1000)[1:-1]
        other_wave_phase_rad = np.radians(other_wave_phase_deg)

        # From http://2000clicks.com/mathhelp/GeometryTrigEquivPhaseShift.aspx
        amplitudes = to_decibels(np.sqrt(1 + np.square(other_wave_amplitude) + 2*other_wave_amplitude*np.cos(other_wave_phase_rad)))
        phases = np.degrees(np.arctan2(other_wave_amplitude*np.sin(other_wave_phase_rad), 1 + other_wave_amplitude*np.cos(other_wave_phase_rad)))

        amplitude_axes.plot(other_wave_phase_deg, amplitudes, label=str(other_wave_amplitude_db)+' dB')
        phase_axes.plot(other_wave_phase_deg, phases, label=str(other_wave_amplitude_db)+' dB')

    for axes in [amplitude_axes, phase_axes]:
        axes.set_xlabel('Phase (degrees)')
        axes.set_xticks([-180, -90, 0, 90, 90, 180])

    amplitude_axes.legend(loc='lower center')
    amplitude_axes.autoscale(axis='x', tight=True)
    amplitude_axes.set_ylabel('Resulting amplitude (dB)')
    amplitude_axes.set_ylim(-25, 15)
    amplitude_axes.axhline(color='gray', linestyle='--', zorder=0)

    phase_axes.autoscale(tight=True)
    phase_axes.set_ylabel('Resulting phase (degrees)')
    phase_axes.set_yticks([-180, -90, 0, 90, 180])
    phase_axes.axhline(color='gray', linestyle='--', zorder=0)
