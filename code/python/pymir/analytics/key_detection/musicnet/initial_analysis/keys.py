from pymir import settings
from pymir.common import EXISTING_KEYS

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


def compute(metadata):
    """
    Counts keys by song
    """
    keys = {
        note: 0 for note in EXISTING_KEYS
    }
    for k, song in metadata.items():
        keys[song['armony']] += 1
    # generating image
    fname = (
        os.path.join(
            settings.IMG_DIR,
            'key_detection', 'musicnet', 'keys.png'))

    df = pd.Series(keys)
    fig, ax = plt.subplots()
    total = df.values.tolist()
    labels =  df.keys().tolist()
    ind = np.arange(len(labels))  # the x locations for the groups
    fig, ax = plt.subplots()
    width = 0.3
    ax.bar(ind, total, width)
    ax.grid(True)
    plt.ylabel('Number of Songs')
    plt.xlabel('Key')
    ax.set_xticklabels(labels, rotation=60)
    ax.set_xticks(ind + width)
    plt.tight_layout()
    plt.savefig(fname)
