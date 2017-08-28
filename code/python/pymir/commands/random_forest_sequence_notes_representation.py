from pymir.analytics.key_detection.musicnet.ml.note_sequence.base import random_forest

import argparse
import textwrap


def compute(n_estimators=100):
    """
    Base model of key detection for
    Musicnet metadata based in TF-IDF and Random Forest
    """
    random_forest.compute(n_estimators=n_estimators)


def run():

    parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(compute.__doc__))
    parser.add_argument(
        '--n_estimators', help='Number of estimators for Random Forest',
        type=int, default=100,  required=False)
    parser.add_argument(
        '--ngram_size', help='Size of ngrams',
        type=int, default=5,  required=False)
    args, extra_params = parser.parse_known_args()
    random_forest.compute(n_estimators=args.n_estimators, ngram_size=args.ngram_size)
