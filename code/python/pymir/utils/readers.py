from pymir import settings
from pymir.common import EXISTING_NOTES
from decimal import Decimal

import csv
import numpy as np
import os


def load_riffstation_dataset(sep='\n'):

    def parse(fname):
        """
        Database format is not splitted line by line, so custom
        parsing is required
        """
        song = {}
        with open(fname) as f:
            lines = f.read().split('\n')
            song['title'] = lines[0].split('/')[-1]

            # parsing songbeats, sometimes last item in the list is an
            # empty string
            txtbeats = lines[1][len('beats: '):].split(' ')
            if not txtbeats[-1]:
                txtbeats.pop(-1)
            song['beats'] = list(map(Decimal, txtbeats))

            # parsing chordvector, sometimes last item is an empty string
            chord_vector = lines[2][len('chordVec1: '):].split(' ')
            if not chord_vector[-1]:
                chord_vector.pop(-1)

            # Chord detector algorithm can only detect major and minor chors,
            #  not 7ths, 9th, etc, so this notes are replaced by -
            chord_vector = [
                c if c in EXISTING_NOTES else '-' for c in chord_vector
            ]

            song['chord_vector'] = chord_vector

            # unique chords
            chord_vector_detected = [
                c for c in lines[3][len('chordVecDetected1: '):].split(' ')
                if c in EXISTING_NOTES
            ]

            song['chord_vector_detected'] = chord_vector_detected
            song['sample_rate'] = int(lines[4][len('sample_rate: '):])
            song['tempo'] = Decimal(lines[5][len('tempo: '):])
            song['meter'] = int(lines[6][len('meter: '):])
            return song

    dirname = os.path.join(settings.DATA_DIR, 'riffstation')
    song_files = []
    for directory in next(os.walk(dirname))[1]:
        for song in os.listdir(os.path.join(dirname, directory)):
            if 'rsm' in song:
                song_files.append(os.path.join(dirname, directory, song))

    songs = []
    for s in song_files:
        try:
            songs.append(parse(s))
        except Exception as error:
            print(s)
            print(error)
    return songs


def load_riffstation_detected_chords(sep='\n'):
    """
    Load detected chords by song
    """
    songs = []
    fname = os.path.join(settings.DATA_DIR, 'results', 'songChords.csv')
    with open(fname) as f:
        lines = f.read().split('\n')
        index = 0
        while index < len(lines) - 1:
            if not lines[index]:
                index += 1
                continue

            s = {}
            s['id'] = lines[index]
            index += 1
            s['title'] = lines[index].split('/')[-1]
            index += 1
            s['detected_chords'] = [s for s in lines[index].split('\t') if s]
            index += 1
            s['unique_chords'] = [s for s in lines[index].split('\t') if s]
            songs.append(s)
            index += 1

    return songs


def load_musicnet_metadata():
    fname = os.path.join(settings.DATA_DIR, 'musicnet', 'musicnet_metadata.csv')
    with open(fname) as f:
        # metadata info contains unncesary quotes that should be removed
        lines = [row for row in csv.reader(f, delimiter=',')]
        labels = lines[0]
        data = {}
        for l in lines[1:]:
            song = {}
            for x in range(len(labels)):
                song[labels[x]] = l[x]
            data[song['id']] = song
        return data


def load_musicnet_ds():
    fname = os.path.join(settings.DATA_DIR, 'musicnet', 'db', 'musicnet.npz')
    return np.load(open(fname, 'rb'), encoding='bytes')


def load_midi_map():
    fname = os.path.join(settings.DATA_DIR, 'musicnet', 'midi.csv')
    with open(fname) as csvfile:
        return {int(row[0]): row[1] for row in csv.reader(csvfile, delimiter=',')}

def load_midi_notes_map():
    fname = os.path.join(settings.DATA_DIR, 'musicnet', 'midi_notes.csv')
    with open(fname) as csvfile:
        lines = [row for row in csv.reader(csvfile, delimiter=',')]
        labels = lines[0]
        notes = {}
        octave = 0
        for row in lines[1:-1]:
            i = 0
            while i < len(row):
                notes[int(row[i])] = {'note': labels[i], 'octave': octave}
                i += 1
            octave += 1
        return notes
