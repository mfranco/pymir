from sklearn.model_selection import train_test_split

from pymir import settings

from pymir.common import EXISTING_KEYS


import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def generate_ds(test_fname, train_fname, test_size=0.2):

    musicnet_fname = (
        os.path.join(
        settings.DATA_DIR, 'musicnet', 'representations',
        'sequence_of_notes', 'musicnet.csv'))

    songs = {}
    i = 0
    with open(musicnet_fname) as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            if row[0] not in songs:
                songs[row[0]] = [row]
            else:
                songs[row[0]].append(row)
            i += 1

    train_list = []
    test_list = []

    for k in EXISTING_KEYS:
        if k in songs:
            df = pd.Series(songs[k])
            train, test = train_test_split(df, test_size=test_size)
            train_list.append(train)
            test_list.append(test)

    train = pd.concat(train_list)
    test = pd.concat(test_list)


    # generate train and test sets, first note in every line is key  of the song

    with open(test_fname, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for a in test:
            writer.writerow(a)


    with open(train_fname, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for a in train:
            writer.writerow(a)

def plot_train_test_data(test_fname, train_fname):
    test_keys = {}
    train_keys = {}

    with open(test_fname, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if row[0] in test_keys:
                test_keys[row[0]] +=1
            else:
                test_keys[row[0]] =1


    with open(train_fname, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if row[0] in train_keys:
                train_keys[row[0]] +=1
            else:
                train_keys[row[0]] =1

    test_keys_list = [
        test_keys[k] if k in test_keys else 0 for k in EXISTING_KEYS
    ]

    train_keys_list = [
        train_keys[k] if k in train_keys else 0 for k in EXISTING_KEYS
    ]

    ind = np.arange(len(EXISTING_KEYS))  # the x locations for the groups
    width = 0.35       # the width of the bars

    fig, ax = plt.subplots()
    train = ax.bar(ind, train_keys_list, width, color='r')
    test = ax.bar(ind + width, test_keys_list, width, color='y')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Frequency')
    ax.set_title('Keys frequency by set')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(EXISTING_KEYS, rotation=60)

    ax.legend((train[0], test[0]), ('Train Set', 'Test Set'))

    fname = (
        os.path.join(
            settings.IMG_DIR,
            'key_detection', 'musicnet', 'train_test_keys_distribution.png'))

    ax.set_xticks(ind + width)
    plt.tight_layout()
    plt.savefig(fname)

def plot_ds_duration_by_song(test_fname, train_fname):
    durations = []

    with open(test_fname, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            durations.append(len(row) - 1)

    with open(train_fname, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            durations.append(len(row) - 1)


    # the histogram of the data
    n, bins, patches = plt.hist(durations, 50, normed=0, facecolor='green', alpha=0.75)
    plt.grid(True)
    plt.xlabel('Songs')
    plt.ylabel('Probability')
    fname = (
        os.path.join(
            settings.IMG_DIR,
            'key_detection', 'musicnet', 'sequence_len.png'))
    plt.tight_layout()
    plt.savefig(fname)



def compute(train_size=0.8):
    """
    Splits musicnet dataset into train and test sets
    """
    test_size = 1 - train_size

    test_fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'sequence_of_notes', 'musicnet_test.csv'))

    train_fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'sequence_of_notes', 'musicnet_train.csv'))

    generate_ds(test_fname, train_fname, test_size=test_size)
    plot_train_test_data(test_fname, train_fname)
    plot_ds_duration_by_song(test_fname, train_fname)
