import csv
import os


def transform_multiclass(fname, data_type='test'):
    class_dict = {}

    with open(fname, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if row[0] in class_dict:
                class_dict[row[0]].append(row)
            else:
                class_dict[row[0]] = [row]


    location, fn = os.path.split(fname)
    fdir = os.path.join(location, data_type)

    if not os.path.exists(fdir):
        os.makedirs(fdir)

    for k, v in class_dict.items():
        # creates a binary classification file by key
        fn = '{}.{}.txt'.format(data_type, k)
        fn = (
            os.path.join(fdir, fn))

        with open(fn, 'w') as f:
            writer = csv.writer(f, delimiter=' ')

            for k2, v2 in class_dict.items():
                if k == k2:
                    key = '+1'
                else:
                    key = '-1'

                for row in v2:
                    writer.writerow([key]  + row[1: -1])



def compute(train_fname, test_fname):
    """
    Tranform dataset into multiple binary classification sets
    """

    transform_multiclass(test_fname, data_type='test')
    transform_multiclass(train_fname, data_type='train')
