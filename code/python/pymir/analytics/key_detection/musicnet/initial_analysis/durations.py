
from pymir import settings

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


def get_durations_by_song(song):
    """
    Iterate over all labels for a given song
    to extract notes
    """
    durations = {}
    for segment in song:
        # (start,end,(instrument,note,measure,beat,note_value))
        duration = segment[2][4].decode('utf-8')
        if duration not in durations:
            durations[duration] = 1
        else:
            durations[duration] += 1
    print(durations)
    return durations


def compute(musicnet_ds):
    """
    Counts notes frequency in the dataset
    """
    durations = {}

    # X: audio time series Y: labels
    for id in musicnet_ds.files:
        X, Y = musicnet_ds[id]
        for k, v in get_durations_by_song(Y).items():
            if k in durations:
                durations[k] += v
            else:
                durations[k] = v
    # generating image
    fname = (
        os.path.join(
            settings.IMG_DIR,
            'feature_extraction', 'musicnet', 'durations.png'))

    df = pd.Series(durations)
    fig, ax = plt.subplots()
    total = df.values.tolist()
    labels =  df.keys().tolist()
    ind = np.arange(len(labels))  # the x locations for the groups
    fig, ax = plt.subplots()
    width = 0.3
    ax.bar(ind, total, width)
    ax.grid(True)
    plt.ylabel('Frequency')
    plt.xlabel('Durations')
    ax.set_xticklabels(labels, rotation=90)
    ax.set_xticks(ind + width)
    plt.tight_layout()
    plt.savefig(fname)
