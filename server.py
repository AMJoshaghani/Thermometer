import sounddevice as sd
import numpy as np

# Attributes of the sound
duration = 1.0  # in sec
frequency = 1_000  # in Hz

# Generation of a time array
sample_rate = 44_100
t = np.linspace(0, duration, int(duration * sample_rate), endpoint=True)

# Generation of a sine wave
y = np.sin(2 * np.pi * frequency * t)


def emit(r):
    try:
        # Playing the sound
        sd.play(y, sample_rate)

        # Waiting for sound to finish
        sd.wait()

        r['ok'] = True

    except Exception as e:
        r['ok'] = False
        r['e'] = e
