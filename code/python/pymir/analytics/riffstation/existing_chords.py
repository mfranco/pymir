"""
Generates an histogram of existing chords by song for all songs
Some of the code to generate plot was taken from
http://matplotlib.org/examples/api/barchart_demo.html
"""
from pymir import settings
from pymir.common import EXISTING_NOTES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os


def compute(db):
    songs_chords = []
    for song in db:
        chords = {}
        for n in EXISTING_NOTES:
            if n in song['chord_vector_detected']:
                chords[n] = 1
            else:
                chords[n] = 0
        songs_chords.append(chords)
    df = pd.DataFrame(songs_chords)
    fname = (
        os.path.join(
            settings.IMG_DIR,
            'initial_diagnose', 'existing_chords_histogram.png'))
    total = df.sum().values.tolist()
    labels = df.columns.tolist()
    ind = np.arange(len(labels))  # the x locations for the groups
    fig, ax = plt.subplots()
    width = 0.3
    ax.bar(ind, total, width)
    ax.grid(True)
    plt.ylabel('Chords frequency')
    ax.set_xticklabels(labels, rotation=60)
    ax.set_xticks(ind + width)
    plt.savefig(fname)
