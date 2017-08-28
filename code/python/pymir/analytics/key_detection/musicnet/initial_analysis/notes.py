from pymir import settings
from pymir.common import EXISTING_NOTES, EXISTING_KEYS

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import csv

def get_notes_by_song(song, notes_map):
    """
    Iterate over all labels for a given song
    to extract notes
    """
    notes = {}
    for segment in song:
        # (start,end,(instrument,note,measure,beat,note_value))
        if segment[2][1] not in notes_map:
            continue
        note = notes_map[segment[2][1]]['note']
        if note not in notes:
            notes[note] = 1
        else:
            notes[note] += 1
    return notes


def compute_frequency(musicnet_ds, notes_map):
    """
    Counts notes frequency in the dataset
    """
    notes = {}

    # X: audio time series Y: labels
    for id in musicnet_ds.files:
        X, Y = musicnet_ds[id]
        for k, v in get_notes_by_song(Y, notes_map).items():
            if k in notes:
                notes[k] += v
            else:
                notes[k] = 1

    # generating image
    fname = (
        os.path.join(
            settings.IMG_DIR,
            'feature_extraction', 'musicnet', 'notes.png'))

    df = pd.Series(notes)
    fig, ax = plt.subplots()
    total = df.values.tolist()
    labels =  df.keys().tolist()
    ind = np.arange(len(labels))  # the x locations for the groups
    fig, ax = plt.subplots()
    width = 0.3
    ax.bar(ind, total, width)
    ax.grid(True)
    plt.ylabel('Frequency')
    plt.xlabel('Notes')
    ax.set_xticklabels(labels, rotation=60)
    ax.set_xticks(ind + width)
    plt.tight_layout()
    plt.savefig(fname)


def compute_notes_distribution_by_key(metadata, musicnet_ds, notes_map):
    """
    Distribution of notes by key
    """
    major_keys = {
        key: {note: 0 for note in EXISTING_NOTES if 'm' not in note}
        for key in EXISTING_KEYS if '+' in key
    }

    minor_keys = {
        key: {note: 0 for note in EXISTING_NOTES  if 'm' not in note}
        for key in EXISTING_KEYS if '-' in key
    }

    minor_keys_cp = minor_keys.copy()
    major_keys_cp = major_keys.copy()

    for k, song in metadata.items():
        is_major = False
        key = song['armony']
        if key in major_keys:
            notes = major_keys[key]
            is_major = True
        elif key in minor_keys:
            notes = minor_keys[key]
        else:
            continue

        X, Y = musicnet_ds[k]
        s_notes = get_notes_by_song(Y, notes_map)
        for k, v in s_notes.items():
            notes[k] += v

        if is_major:
            major_keys_cp[key] = notes
        else:
            minor_keys_cp[key] = notes
    fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'notes_distribution.csv'))

    with open(fname, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        columns_names = [note for note in EXISTING_NOTES  if 'm' not in note]
        header = ['key']
        header.extend(columns_names)
        writer.writerow(header)

        for key, notes in major_keys_cp.items():
            row = [key]
            for n in columns_names:
                row.append(notes[n])
            writer.writerow(row)

        for key, notes in minor_keys_cp.items():
            row = [key]
            for n in columns_names:
                row.append(notes[n])
            writer.writerow(row)



def compute(metadata, musicnet_ds, notes_map):
    compute_notes_distribution_by_key(metadata, musicnet_ds, notes_map)
