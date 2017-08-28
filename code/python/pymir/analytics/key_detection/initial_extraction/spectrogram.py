from scipy.io import wavfile
from scipy import fft, arange

import matplotlib.pyplot as plt

import numpy as np
import librosa
import librosa.display

from pymir.utils.readers import (
    load_musicnet_metadata, load_musicnet_ds, load_midi_map,
    load_midi_notes_map)


def plot1(source_fname, output_fname):
    """
    plots an espectogram
    """
    y, sr = librosa.core.load(source_fname, duration=2, offset=1.0)
    plt.figure(figsize=(8, 3))
    D = librosa.logamplitude(np.abs(librosa.stft(y))**2, ref_power=np.max)
    librosa.display.specshow(D, y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.grid(True)
    plt.savefig(output_fname)

def plot(source, img_name, duration_ms=0.05, offset_ms=1, sample_rate=48000):
    sample_len = 1 / sample_rate

    # compution position in the array for offset
    offset_position = int((offset_ms / sample_len) / 2)

    # computing final position based in duration
    end_position = int((duration_ms / sample_len) / 2)



    grate, gdata = wavfile.read(source)
    gy = gdata[:,1]
    gy = gy[offset_position: offset_position + end_position]
    gtimp = len(gy) / sample_rate
    gt = np.linspace(0, gtimp, len(gy))

    f, plots = plt.subplots(1, 1, figsize=(10, 3))

    n = len(gy) # lungime semnal
    k = arange(n)
    T = n / sample_rate
    frq = k / T # two sides frequency range
    frq = frq[list(range(int(n / 2)))] # one side frequency range

    Y = fft(gy) / n # fft computing and normalization
    Y = Y[list(range(int(n / 2)))]
    Y = abs(Y)
    plots.plot(frq, Y, 'r') # plotting the spectrum
    plots.set_xlabel('Freq (Hz)')
    plots.set_ylabel('Magnitude / Power')
    plots.grid(True)

    plots.set_xscale('log')
    plt.tight_layout()
    plt.savefig(img_name)

    import ipdb; ipdb.set_trace()


def plot0(source, img_name, sample_rate=48000):
    grate, gdata = wavfile.read(source)
    X = gdata[:,1]
    window_size = 2048  # 2048-sample fourier windows
    stride = 512        # 512 samples between windows
    wps = sample_rate/float(512) # ~86 windows/second
    Xs = np.empty([int(10*wps),2048])

    for i in range(Xs.shape[0]):
        Xs[i] = np.abs(fft(X[i*stride:i*stride+window_size]))

    f, plots = plt.subplots(1, 1, figsize=(10, 3))
    plots.plot(Xs.T[0:150])
    plots.set_xlabel('Freq (Hz)')
    plots.set_ylabel('Magnitude / Power')
    plt.tight_layout()

    plots.set_xscale('log')
    plt.tight_layout()
    plt.savefig(img_name)
    import ipdb; ipdb.set_trace()
