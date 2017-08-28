from scipy import arange
from scipy.io import wavfile
from scipy.signal import hilbert, chirp

import numpy as np
import matplotlib.pyplot as plt


def plot(source, output_fname, sample_rate=48000):
    """
    Hilbert transform to determine the amplitude envelope and instantaneous
    frequency of an amplitude-modulated signal.
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html
    """
    grate, gdata = wavfile.read(source)
    gy = gdata[:,1]
    n = len(gy) # lungime semnal
    k = arange(n)
    T = n / sample_rate
    frq = k / T # two sides frequency range
    frq = frq[list(range(int(n / 2)))] # one side frequency range


    analytic_signal = hilbert(gdata)
    amplitude_envelope = np.abs(analytic_signal)
    Y = amplitude_envelope[list(range(int(n / 2)))]
    analytic_signal = analytic_signal[list(range(int(n / 2)))]
    plt.figure(figsize=(8, 3))
    plt.grid(True)

    fig, ax = plt.subplots()
    ax.plot(frq, Y)
    ax.xlabel('Time')
    ax.ylabel('Amplitude')
    #ax.plot(frq, analytic_signal, label='signal')
    plt.savefig(output_fname)
