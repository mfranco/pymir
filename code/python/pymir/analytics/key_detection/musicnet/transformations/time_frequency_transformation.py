from pymir import settings
from pymir.utils.readers import (
    load_musicnet_metadata, load_musicnet_ds)


import csv
import os
import numpy as np
from scipy import fft


fs = 44100            # samples/second
stride = 512          # samples between windows
wps = fs/float(512)   # windows/second


def generate_ds(
        fname,
        window_size=512):
    musicnet_ds =  load_musicnet_ds()

    metadata = load_musicnet_metadata()

    with open(fname, 'w') as f:
        writer = csv.writer(f, delimiter=' ')

        for id in musicnet_ds.files:
            Xs = np.empty([int(10*wps), window_size])
            X, Y = musicnet_ds[id]
            print('.')

            for i in range(Xs.shape[0]):
                Xs[i] = np.abs(fft(X[i*stride: i*stride + window_size]))

            song = []

            for i in range(Xs.shape[0]):
                song.extend(Xs[i].tolist())

            s = {}
            key = metadata[id]['armony']
            s['ts'] = song
            writer.writerow([key]  + song)



def compute(window_size=512):
    """
    Each song is represente by ist key (label) and a time series sequence computed from fourier 
    transformations
    """

    fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'time_series', 'frequency_domain', 'musicnet.csv'))


    generate_ds(fname, window_size=window_size)
