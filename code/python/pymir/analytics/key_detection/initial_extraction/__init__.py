from pymir import settings
from . import (
    audio_sample, amplitude_envelop, amplitude_frequency, spectrogram
)

import os


def compute():
    """
    Basic initial diagnose that compares an electric guitar
    audio signal and synthetized drums across different
    audio signal representations
    """


    bass_source_fname = os.path.join(
        settings.DATA_DIR, 'audio', 'shuffleblues',
        'bass_Selection.wav')

    guitar_source_fname = os.path.join(
        settings.DATA_DIR, 'audio', 'shuffleblues',
        'guitar_Selection.wav')

    drums_source_fname = os.path.join(
        settings.DATA_DIR, 'audio', 'shuffleblues',
        'drum_Selection.wav')

    mix_source_fname = os.path.join(
        settings.DATA_DIR, 'audio', 'shuffleblues',
        'mix_Selection.wav')

    # amplitude and frequency analisys
    amplitude_frequency_guitar = (
        os.path.join(
            settings.IMG_DIR, 'key_detection',
            'initial_diagnose', 'amplitude_frequency_guitar.png'))

    amplitude_frequency_drums = (
        os.path.join(
            settings.IMG_DIR, 'key_detection',
            'initial_diagnose', 'amplitude_frequency_drums.png'))

    amplitude_frequency_bass = (
        os.path.join(
            settings.IMG_DIR, 'key_detection',
            'initial_diagnose', 'amplitude_frequency_bass.png'))

    amplitude_frequency_mix = (
        os.path.join(
            settings.IMG_DIR, 'key_detection',
            'initial_diagnose', 'amplitude_frequency_mix.png'))


    #amplitude_frequency.plot(guitar_source_fname, amplitude_frequency_guitar)
    #amplitude_frequency.plot(drums_source_fname, amplitude_frequency_drums)
    #amplitude_frequency.plot(bass_source_fname, amplitude_frequency_bass)
    #amplitude_frequency.plot(mix_source_fname, amplitude_frequency_mix)

    # plotting a fragment of an audio signal as a waveform
    #audio_sample.plot(
    #    guitar_source_fname,
    #    os.path.join(settings.IMG_DIR, 'key_detection', 'initial_diagnose', 'sample_wave_guitar.png')
    #)


    ## plotting spectrograms
    spectrogram_guitar = (
        os.path.join(
            settings.IMG_DIR, 'key_detection',
            'initial_diagnose', 'frequency_guitar.png'))

    #spectrogram_drums = (
    #    os.path.join(
    #        settings.IMG_DIR, 'key_detection',
    #        'initial_diagnose', 'spectrogram_drums.png'))

    spectrogram.plot(guitar_source_fname, spectrogram_guitar)
    #spectrogram.plot(drums_source_fname, spectrogram_drums)


    ## plots amplitued envelop
    #amplitude_envelop_guitar = (
    #    os.path.join(
    #        settings.IMG_DIR, 'key_detection',
    #        'initial_diagnose', 'amplitude_envelop_guitar.png'))

    #amplitude_envelop_drums = (
    #    os.path.join(
    #        settings.IMG_DIR, 'key_detection',
    #        'initial_diagnose', 'amplitude_envelop_drums.png'))

    #amplitude_envelop.plot(guitar_source_fname, amplitude_envelop_guitar)
    #amplitude_envelop.plot(drums_source_fname, amplitude_envelop_drums)
