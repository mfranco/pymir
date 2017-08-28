from pymir.analytics.key_detection.musicnet.transformations import time_series_transformation


import argparse
import textwrap


def transform(resample_size=1024):
    """
    Transform Musicnet Dataset into another dataset of time series
    representation with the format:

    key, time series
    """
    time_series_transformation.compute(resample_size=resample_size)


def run():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(transform.__doc__))
    parser.add_argument(
        '--resample_size', required=False, type=int, default=1024)
    args, extra_params = parser.parse_known_args()
    transform(resample_size=args.resample_size)
