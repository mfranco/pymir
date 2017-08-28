"""
How many majors and minor chords are in all songs
"""
from pymir import settings

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


def compute(db):
    mayor_minor = []
    for song in db:
        row = {'mayor': 0, 'minor': 0}
        for c in song['chord_vector_detected']:
            if 'm' in c.lower():
                row['minor'] += 1
            else:
                row['mayor'] += 1
        mayor_minor.append(row)
    df = pd.DataFrame(mayor_minor)
    fname = (
        os.path.join(
            settings.IMG_DIR,
            'initial_diagnose', 'major_vs_minor_chords_histogram.png'))
    total = df.sum().values.tolist()
    labels = df.columns.tolist()
    ind = np.arange(len(labels))  # the x locations for the groups
    fig, ax = plt.subplots()
    width = 0.6
    ax.bar(ind, total, width)
    ax.grid(True)
    plt.ylabel('Chords frequency')
    ax.set_xticklabels(labels)
    ax.set_xticks(ind + width)
    plt.savefig(fname)
