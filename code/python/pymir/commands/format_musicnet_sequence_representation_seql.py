from pymir.analytics.key_detection.musicnet.transformations import note_sequence_seql_formatter
import argparse
import textwrap


def transform():
    """
    Transform musicnet dataset into multiple binary
    classification datasets suitable for SEQL Learner
    """
    note_sequence_seql_formatter.compute()


def run():
    parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(transform.__doc__))
    args, extra_params = parser.parse_known_args()
    transform()
