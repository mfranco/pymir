from sklearn.model_selection import train_test_split

from pymir import settings

from pymir.common import EXISTING_KEYS


import csv
import os
import pandas as pd



def generate_ds(train_fname, test_fname, test_size=0.2):

    musicnet_fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'time_series', 'frequency_domain',  'musicnet.csv'))

    i = 0
    songs = {}
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


def compute(train_size=0.8):
    """
    Each song in the dataset is represented by metadata and a time series
    that represents samples taken at a given sample rate. 
    """
    train_fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'time_series', 'frequency_domain',  'musicnet_train.csv'))

    test_fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'time_series', 'frequency_domain',  'musicnet_test.csv'))

    test_size = 1 - train_size

    generate_ds(train_fname, test_fname, test_size=test_size)
