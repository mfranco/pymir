from pymir.analytics.key_detection.musicnet.transformations import time_frequency_transformation
import argparse
import textwrap


def transform(window_size=512):
    """
    Transform musicnet dataset into time series
    in frequency domain
    """
    time_frequency_transformation.compute(window_size=window_size)


def run():
    parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(transform.__doc__))
    parser.add_argument(
        '--window_size', help='fourier window size', required=False,
        type=int, default=512)

    args, extra_params = parser.parse_known_args()


    transform(window_size=args.window_size)
