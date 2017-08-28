from pymir.analytics.key_detection import initial_extraction
import argparse


def run():
    """
    Run basic analisys for introduction
    """
    parser = argparse.ArgumentParser()
    args, extra_params = parser.parse_known_args()
    initial_extraction.compute()
