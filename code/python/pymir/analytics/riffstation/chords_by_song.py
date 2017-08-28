"""
Number of chords by song for all songs

"""
from pymir import settings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os


def compute(db):
    chords_freq = {}

    for song in db:
        freq = len(song['chord_vector_detected'])

        if not freq:
            continue

        if freq in chords_freq:
            chords_freq[freq] += 1
        else:
            chords_freq[freq] = 1
    df = pd.Series(chords_freq)
    fname = (
        os.path.join(
            settings.IMG_DIR,
            'initial_diagnose', 'chords_by_song_histogram.png'))
    total = df.values.tolist()
    labels =  df.keys().tolist()
    ind = np.arange(len(labels))  # the x locations for the groups
    fig, ax = plt.subplots()
    width = 0.3
    ax.bar(ind, total, width)
    ax.grid(True)
    plt.ylabel('Number of Songs')
    plt.xlabel('Number of Chords')
    ax.set_xticklabels(labels)
    ax.set_xticks(ind + width)
    plt.savefig(fname)
