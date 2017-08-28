from pymir.analytics.key_detection.musicnet.transformations import time_series_frequency_split

import argparse
import textwrap


def transform(train_size):
    """
    Generates a split/test by key and then it merges all the data
    in order to create a test and a train set 
    """
    time_series_frequency_split.compute(train_size=train_size)


def run():
    parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(transform.__doc__))
    parser.add_argument(
        '--train_size', help='size of the train set (float)', required=False,
        type=float, default=0.8)
    args, extra_params = parser.parse_known_args()
    transform(args.train_size)
