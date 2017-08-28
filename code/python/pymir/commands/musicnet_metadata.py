from pymir.analytics.key_detection.musicnet import initial_analysis
import argparse


def run():
    """
    Musicnet metadata information
    """
    parser = argparse.ArgumentParser()
    args, extra_params = parser.parse_known_args()
    initial_analysis.compute()
