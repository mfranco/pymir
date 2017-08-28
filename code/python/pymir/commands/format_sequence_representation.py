from pymir.analytics.key_detection.musicnet.transformations import note_sequence_transformation

import argparse
import textwrap


def transform():
    """
    Transform Musicnet Dataset into another dataset of sequence of notes
    representation with the format:

    key, sequence of notes
    """
    note_sequence_transformation.compute()


def run():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(transform.__doc__))
    args, extra_params = parser.parse_known_args()
    transform()
