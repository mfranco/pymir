from pymir.utils.readers import (
    load_musicnet_metadata, load_musicnet_ds, load_midi_map,
    load_midi_notes_map)

from . import (
    composer, instruments, notes, keys, durations
)

def compute():
    metadata = load_musicnet_metadata()
    musicnet_ds =  load_musicnet_ds()
    midi_map = load_midi_map()
    notes_map = load_midi_notes_map()

    # number of songs by composer
    # composer.compute(metadata)

    # number of songs by instrument
    #instruments.compute(musicnet_ds, midi_map)

    # existing notes in songs
    notes.compute(metadata, musicnet_ds, notes_map)

    # Keys by song
    keys.compute(metadata)

    # durations in the dataset
    #durations.compute(musicnet_ds)

    #fs = 44100      # samples/second
    #X,Y = musicnet_ds['2494']
    #(start,end,(instrument,note,measure,beat,note_value)) = sorted(Y[fs*5])[0]

    #import ipdb; ipdb.set_trace()
