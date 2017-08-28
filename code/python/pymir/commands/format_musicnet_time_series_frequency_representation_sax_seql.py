from pymir.analytics.key_detection.musicnet.transformations import time_domain_sax_formatter

import argparse
import textwrap


def transform(train_fname, test_fname):
    """
    Generates a split/test by key and then it merges all the data
    in order to create a test and a train set 
    """
    time_domain_sax_formatter.compute(train_fname, test_fname)


def run():
    parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(transform.__doc__))
    parser.add_argument(
        '--test_dataset', help='Test File name', required=True)

    parser.add_argument(
        '--train_dataset', help='Train File name', required=True)

    args, extra_params = parser.parse_known_args()
    transform(args.train_dataset, args.test_dataset)
