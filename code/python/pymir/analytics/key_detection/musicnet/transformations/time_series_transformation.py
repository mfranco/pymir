from pymir import settings
from pymir.utils.readers import (
    load_musicnet_metadata, load_musicnet_ds)


import csv
import os
import numpy as np
import matplotlib.pyplot as plt

fs = 44100            # samples/second
window_size = 2048    # fourier window size
d = 1024              # number of features
m = 128               # number of distinct notes
stride = 512          # samples between windows
wps = fs/float(512)   # windows/second
n = 1000              # training data points per recording



def plot_distribution(durations, durations_reduced):
    f, plots = plt.subplots(1, 2, figsize=(10, 3))


    plots[0].hist(durations, 50, normed=1, facecolor='green', alpha=0.75)
    plots[0].grid(True)
    plots[0].set_xlabel('Songs')
    plots[0].set_ylabel('Probability')


    plots[1].hist(durations_reduced, 50, normed=0, facecolor='green', alpha=0.75)
    plots[1].grid(True)
    plots[1].set_xlabel('Songs')
    plots[1].set_ylabel('Probability')

    fname = (
        os.path.join(
            settings.IMG_DIR,
            'key_detection', 'musicnet', 'ts_len.png'))
    plt.tight_layout()
    plt.savefig(fname)



def resample(resample_size=1024):
    musicnet_ds =  load_musicnet_ds()
    durations = []
    durations_reduced = []
    reduced_ds = []
    ids = []


    for id in musicnet_ds.files:
        print('.')
        X, Y = musicnet_ds[id]
        #X = np.where(X != 0)[0]
        durations.append(len(X))
        # subsampling
        # import ipdb; ipdb.set_trace()
        ds = list(X[1::resample_size])
        durations_reduced.append(len(ds))
        ids.append(id)
        reduced_ds.append(ds)
    return ids, reduced_ds, durations, durations_reduced


def generate_ds(fname, ids, ds):
    metadata = load_musicnet_metadata()

    with open(fname, 'w') as f:
        writer = csv.writer(f, delimiter=' ')

        for id, ts in zip(ids, ds):
            key = metadata[id]['armony']
            writer.writerow([key]  + ts)


def compute(resample_size=1024):
    """
    Each song in the dataset is represented by the key and a time series
    """
    fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'time_series', 'time_domain',  'musicnet.csv'))

    ids, reduced_ds, durations, durations_reduced = resample(
        resample_size=resample_size)
    generate_ds(fname, ids, reduced_ds)
    plot_distribution(durations, durations_reduced)
