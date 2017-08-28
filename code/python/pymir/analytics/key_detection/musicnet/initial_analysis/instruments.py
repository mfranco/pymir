from pymir import settings

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


def get_instruments_by_song(song):
    """
    Iterate over all labels for a given song
    to find out what instruments are being played
    """
    instruments = []
    for segment in song:
        # (start,end,(instrument,note,measure,beat,note_value))
        instrument = segment[2][0]
        if instrument not in instruments:
            instruments.append(instrument)
    return instruments


def compute(musicnet_ds, midi_map):
    """
    Counts number of songs by instrument
    """
    settings.DEFAULT_SAMPLE_RATE
    instruments = {}
    # X: audio time series Y: labels
    for id in musicnet_ds.files:
        X, Y = musicnet_ds[id]
        for inst in get_instruments_by_song(Y):
            if inst in instruments:
                instruments[inst] += 1
            else:
                instruments[inst] = 1
    # translation from midi codes to instrument names
    instruments_by_song = {}
    for k, v in instruments.items():
        name = midi_map[k]
        instruments_by_song[name] = v

    # generating image
    fname = (
        os.path.join(
            settings.IMG_DIR,
            'feature_extraction', 'musicnet', 'instruments.png'))

    df = pd.Series(instruments_by_song)
    fig, ax = plt.subplots()
    total = df.values.tolist()
    labels =  df.keys().tolist()
    ind = np.arange(len(labels))  # the x locations for the groups
    fig, ax = plt.subplots()
    width = 0.3
    ax.bar(ind, total, width)
    ax.grid(True)
    plt.ylabel('Number of Songs')
    plt.xlabel('Instrument')
    ax.set_xticklabels(labels, rotation=60)
    ax.set_xticks(ind + width)
    plt.tight_layout()
    plt.savefig(fname)
