from pymir import settings

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


def compute(metadata):
    """
    Compute number of songs by composer
    """
    artists = {}

    for record in metadata[1:]:
        if len(record) < 2:
            continue

        if record[1] not in artists:
            artists[record[1]] = 1
        else:
            artists[record[1]] += 1
    fname = (
        os.path.join(
            settings.IMG_DIR,
            'feature_extraction', 'musicnet', 'composers.png'))
    df = pd.Series(artists)
    fig, ax = plt.subplots()
    total = df.values.tolist()
    labels =  df.keys().tolist()
    ind = np.arange(len(labels))  # the x locations for the groups
    fig, ax = plt.subplots()
    width = 0.3
    ax.bar(ind, total, width)
    ax.grid(True)
    plt.ylabel('Number of Songs')
    plt.xlabel('Composer')
    ax.set_xticklabels(labels, rotation=60)
    ax.set_xticks(ind + width)
    plt.tight_layout()
    plt.savefig(fname)
