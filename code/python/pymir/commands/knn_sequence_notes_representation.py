from pymir.analytics.key_detection.musicnet.ml.note_sequence.base import knn

import argparse
import textwrap


def compute(k=1):
    """
    Base model of key detection for
    Musicnet metadata based in TF-IDF and KNN
    """
    knn.compute(k=k)


def run():

    parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(compute.__doc__))
    parser.add_argument(
        '--k', help='Number of Neighbours KNN',
        type=int, default=1,  required=False)
    parser.add_argument(
        '--ngram_size', help='Size of ngrams',
        type=int, default=5,  required=False)


    args, extra_params = parser.parse_known_args()
    knn.compute(k=args.k, ngram_size=args.ngram_size)
