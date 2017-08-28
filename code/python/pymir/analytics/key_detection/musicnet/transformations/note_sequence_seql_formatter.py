from pymir import settings

import csv
import os



def transform_multiclass(fname, data_type='test'):
    """
    Initial dataset contains all songs in the dataset, first character of every line is
    the key of the song, seql learn expects a one file by every key.
    All files will have the same number of lines
    """

    class_dict = {}


    location, fn = os.path.split(fname)
    fdir = os.path.join(location, data_type)

    if not os.path.exists(fdir):
        os.makedirs(fdir)

    with open(fname, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if row[0] in class_dict:
                class_dict[row[0]].append(row)
            else:
                class_dict[row[0]] = [row]

    for k, v in class_dict.items():
        fn = '{}.{}.txt'.format(data_type, k)
        fn = (
            os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
            'sequence_of_notes', data_type, fn))

        with open(fn, 'w') as f:
            writer = csv.writer(f, delimiter=' ')

            for k2, v2 in class_dict.items():
                if k == k2:
                    key = '+1'
                else:
                    key = '-1'

                for row in v2:
                    writer.writerow([key]  + row[1: -1])


def generate_ds(test_fname, train_fname):
    # transform multiclass dataset into several binary classification datasets
    transform_multiclass(test_fname, data_type='test')
    transform_multiclass(train_fname, data_type='train')




def compute():
    """
    Transform musicnet dataset into multiple binary
    classification datasets suitable for SEQL Learner
    """
    test_fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'sequence_of_notes',  'musicnet_test.csv'))

    train_fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'sequence_of_notes', 'musicnet_train.csv'))

    generate_ds(test_fname, train_fname)
