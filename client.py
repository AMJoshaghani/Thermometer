import pyaudio
import numpy as np
from time import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44_100
THRESHOLD = 1_000  # Adjust this threshold as needed
FREQUENCY_TO_DETECT = 1_000  # Frequency to detect in Hz

p = pyaudio.PyAudio()


def listen(r):
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    start = time()
    while True:
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        fft_data = np.fft.fft(data)
        freqs = np.fft.fftfreq(len(fft_data), 1.0 / RATE)

        idx = np.argmax(np.abs(fft_data))
        freq_detected = freqs[idx]

        if np.abs(fft_data[idx]) > THRESHOLD and abs(freq_detected - FREQUENCY_TO_DETECT) < 20:
            # print(f"Frequency {freq_detected} Hz detected.")
            break
    stop = time()
    stream.stop_stream()
    stream.close()
    p.terminate()

    r['∆t'] = stop - start
