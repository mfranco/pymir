from pymir import settings
from pymir.utils import (
    load_riffstation_dataset, load_riffstation_detected_chords)
from . import (
    existing_chords, chords_by_song, mayor_minor_chords, segment_duration,
    chords_changes_by_song, total_accuracy_by_chord, accuracy_by_chord
)


def run_diagnose():
    db = load_riffstation_dataset()
    detected_chords_by_song = load_riffstation_detected_chords()
    #existing_chords.compute(db)
    #mayor_minor_chords.compute(db)
    #chords_by_song.compute(db)
    #segment_duration.compute(db)
    #audio_sample.compute()
    #chords_changes_by_song.compute(db)
    #total_accuracy_by_chord.compute(db, detected_chords_by_song)
    #accuracy_by_chord.compute(db, detected_chords_by_song)
