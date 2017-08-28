from scipy.io import wavfile
from scipy import fft, arange
import matplotlib.pyplot as plt
import numpy as np


def plot(source, output, duration_ms=0.05, offset_ms=1, sample_rate=48000):
    sample_len = 1 / sample_rate

    # compution position in the array for offset
    offset_position = int((offset_ms / sample_len) / 2)

    # computing final position based in duration
    end_position = int((duration_ms / sample_len) / 2)

    grate, gdata = wavfile.read(source)
    gy = gdata[:,1]
    gtimp = len(gy) / sample_rate
    gt = np.linspace(0, gtimp, len(gy))

    f, plots = plt.subplots(1, 1, figsize=(10, 3))
    x_subset = gt[offset_position: offset_position + end_position]
    y_subset = gy[offset_position: offset_position + end_position]
    plots.plot(x_subset, y_subset)

    plots.set_xlabel('Time')
    plots.set_ylabel('Amplitude')
    plots.grid(True)
    plt.tight_layout()
    plt.savefig(output)
    import ipdb; ipdb.set_trace()
