"""
Command that runs an initial diagnose in the songs database to
extract relevant information about the data
"""

from pymir.analytics.riffstation import run_diagnose
import argparse


def run():
    description = 'Initial diagnose of riffstation songs dataset'
    parser = argparse.ArgumentParser(description=description)
    args, extra_params = parser.parse_known_args()
    run_diagnose()
