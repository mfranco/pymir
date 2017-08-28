"""
Counts How many changes by song
"""

from pymir import settings

import pandas as pd
import matplotlib.pyplot as plt

import os


def compute(db):
    chord_changes = {}
    for song in db:
        changes = 0
        # if there chord in following position is different, then there
        # is a chord change
        for i in range(len(song['chord_vector'])-1):
            if song['chord_vector'][i] != song['chord_vector'][i+1]:
                changes += 1
        if changes in chord_changes:
            chord_changes[changes] += 1
        else:
            chord_changes[changes] = 1
    df = pd.Series(chord_changes)
    fname = (
        os.path.join(
            settings.IMG_DIR,
            'initial_diagnose', 'changes_by_song_histogram.png'))
    labels =  df.keys().tolist()
    fig, ax = plt.subplots()
    ax.hist(labels, len(labels))
    ax.grid(True)
    plt.ylabel('Number of Songs')
    plt.xlabel('Number of Chord Changes')
    plt.savefig(fname)
