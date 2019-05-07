import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile as wf

sample_rate, samples = wf.read('output.wav')
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

plt.pcolormesh(frequencies, times, spectrogram)
plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()