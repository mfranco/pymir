from pymir import settings
from pymir.utils.readers import (
    load_musicnet_metadata, load_musicnet_ds, load_midi_notes_map)

import csv
import os


def get_notes_by_song(song, notes_map):
    """
    Iterate over all labels for a given song.

    Same note have different midi codes in different octaves.

    For example the note C has the following codes: 12, 24, 36, 48, 60, 72,
    84, 96, 108, 120


    For this representation, we transform all these code only to the note C.
    We do the same for all the notes.
    """
    notes = []
    for segment in song:
        # (start,end,(instrument,note,measure,beat,note_value))
        notes.append(notes_map[segment[2][1]]['note'])
    return notes



def generate_ds(fname):
    """
    Extracts notes information from musicnet dataset for each song
    """
    musicnet_ds =  load_musicnet_ds()
    notes_map = load_midi_notes_map()
    songs = []
    metadata = load_musicnet_metadata()
    for id in musicnet_ds.files:
        print('.')
        X, Y = musicnet_ds[id]
        s = {}
        s['notes'] = get_notes_by_song(Y, notes_map)
        s['key'] = metadata[id]['armony']
        s['id'] = id
        songs.append(s)

    with open(fname, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for a in songs:
            writer.writerow([a['key']]  + a['notes'])


def compute():
    """
    Transform Musicnet Dataset into another dataset of sequence of notes
    representation with the format:

    key, sequence of notes
    """

    fname = (
        os.path.join(
        settings.DATA_DIR, 'musicnet', 'representations',
        'sequence_of_notes', 'musicnet.csv'))

    generate_ds(fname)
