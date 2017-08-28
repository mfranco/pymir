from pymir import settings
import matplotlib.pyplot as plt

import csv
import os
from scipy import arange

def compute():
    fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'time_series', 'time_domain', 'musicnet.csv'))
    KEYS = ('G+', 'E-', 'C+', 'E+')

    data = {}

    with open(fname, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if row[0] in KEYS and row[0] in data:
                data[row[0]].append(list(map(float, row[1:])))
            elif row[0] in KEYS:
                data[row[0]] = [list(map(float, row[1:]))]

    img_name = os.path.join(
        settings.IMG_DIR, 'key_detection', 'musicnet', 'amplitude_gM.png')

    c_len = arange(len(data['G+'][0]))
    f, plots = plt.subplots(2, 1)
    plots[0].plot(c_len, data['G+'][0])
    plots[0].set_xlabel('Time')
    plots[0].set_ylabel('Amplitude')

    plots[0].grid(True)
    c_len = arange(len(data['G+'][1]))
    plots[1].plot(c_len, data['G+'][1])
    plots[1].set_xlabel('Time')
    plots[1].set_ylabel('Amplitude')

    plots[1].grid(True)
    plt.tight_layout()
    plt.savefig(img_name)

    img_name = os.path.join(
        settings.IMG_DIR, 'key_detection', 'musicnet', 'amplitude_CM_EM.png')

    f, plots = plt.subplots(2, 1)


    c_len = arange(len(data['C+'][0]))
    plots[0].plot(c_len, data['C+'][0])
    plots[0].set_xlabel('Song in The Key of C+')
    plots[0].set_ylabel('Amplitude')

    plots[0].grid(True)
    c_len = arange(len(data['E+'][0]))
    plots[1].plot(c_len, data['E+'][0])
    plots[1].set_xlabel('Song in The Key of E+')
    plots[1].set_ylabel('Amplitude')

    plots[1].grid(True)
    plt.tight_layout()
    plt.savefig(img_name)
