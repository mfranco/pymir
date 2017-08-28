"""
cccc|dddddddd|cccc

x axis: 4=2  8=1

"""

from pymir import settings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os


def compute(db):
    chord_segments = {}
    for song in db:
        segment = []
        for i in range(len(song['chord_vector'])-1):
            chord = song['chord_vector'][i]

            if not segment or chord == song['chord_vector'][i+1]:
                segment.append(chord)
            else:
                l = len(segment)
                # ignoring very very long segments
                if l < 50:
                    if l in chord_segments:
                        chord_segments[l] += 1
                    else:
                        chord_segments[l] = 1
                segment = []
    df = pd.Series(chord_segments)
    fname = (
        os.path.join(
            settings.IMG_DIR,
            'initial_diagnose', 'segment_lenght_histogram.png'))
    labels =  df.keys().tolist()
    values = df.values.tolist()
    fig, ax = plt.subplots()
    ind = np.arange(len(labels))  # the x locations for the groups
    fig, ax = plt.subplots()
    width = .5
    ax.bar(labels, values, width)
    ax.grid(True)
    plt.ylabel('Number of Segments')
    plt.xlabel('Lenght of Segment')
    plt.savefig(fname)
    ax.set_xticklabels(labels)
    ax.set_xticks(ind + width)
    #print(labels)
    #print(values)
