from scipy.io import wavfile
from scipy import fft, arange
import matplotlib.pyplot as plt
import numpy as np


def plot(source, img_name, sample_rate=48000):
    """
    Command that loads an audio signal and generates a graphical
    representation
    of amplitude and frequency
    """

    grate, gdata = wavfile.read(source)
    gy = gdata[:,1]
    gtimp = len(gy) / sample_rate
    gt = np.linspace(0, gtimp, len(gy))

    f, plots = plt.subplots(1, 2, figsize=(10, 3))
    plots[0].plot(gt, gy)
    plots[0].set_xlabel('Time')
    plots[0].set_ylabel('Amplitude')

    plots[0].grid(True)

    n = len(gy) # lungime semnal
    k = arange(n)
    T = n / sample_rate
    frq = k / T # two sides frequency range
    frq = frq[list(range(int(n / 2)))] # one side frequency range

    Y = fft(gy) / n # fft computing and normalization
    Y = Y[list(range(int(n / 2)))]
    plots[1].plot(frq, abs(Y), 'r') # plotting the spectrum
    plots[1].set_xlabel('Freq (Hz)')
    plots[1].set_ylabel('Magnitude / Power')
    plots[1].grid(True)

    plots[1].set_xscale('log')
    plt.tight_layout()
    plt.savefig(img_name)
