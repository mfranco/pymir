from pymir import settings
import matplotlib.pyplot as plt

import csv
import os
from scipy import arange

def compute():
    fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'time_series', 'frequency_domain', 'musicnet.csv'))
    KEYS = ('C+', 'E+', 'D#+', 'F+', 'G+', 'G#+', 'G#-')

    data = {}

    with open(fname, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if row[0] in KEYS and row[0] in data:
                data[row[0]].append( [ it for it in map(float, row[1:])  if it > 1 ])
            elif row[0] in KEYS:
                data[row[0]] = [[ it for it in map(float, row[1:])  if it > 1 ]]

    img_name = os.path.join(
        settings.IMG_DIR, 'key_detection', 'musicnet', 'frequencyGsharpM.png')

    c_len = arange(len(data['G#+'][0]))
    f, plots = plt.subplots(3, 1)
    plots[0].plot(c_len, data['G#+'][0])
    plots[0].set_xlabel('Frequency (Hz)')
    plots[0].set_ylabel('Magnitude')
    plots[0].set_xscale('log')
    plots[0].grid(True)
    plots[0].set_ylim([0, 15])
    c_len = arange(len(data['G#+'][1]))
    plots[1].plot(c_len, data['G#+'][1])
    plots[1].set_xlabel('Frequency (Hz)')
    plots[1].set_ylabel('Magnitude')
    plots[1].set_xscale('log')
    plots[1].grid(True)
    plots[1].set_ylim([0, 15])
    c_len = arange(len(data['G#+'][3]))
    plots[2].plot(c_len, data['G#+'][3])
    plots[2].set_xlabel('Frequency (Hz)')
    plots[2].set_ylabel('Magnitude')
    plots[2].set_xscale('log')
    plots[2].grid(True)
    plots[2].set_ylim([0, 15])
    plt.tight_layout()
    plt.savefig(img_name)


    img_name = os.path.join(
        settings.IMG_DIR, 'key_detection', 'musicnet', 'frequencyGsharpMDsharpM.png')

    c_len = arange(len(data['G#+'][0]))
    f, plots = plt.subplots(3, 1)
    plots[0].plot(c_len, data['G#+'][0])
    plots[0].set_xlabel('Frequency (Hz)')
    plots[0].set_ylabel('Magnitude')
    plots[0].set_xscale('log')
    plots[0].set_ylim([0, 15])
    plots[0].grid(True)
    c_len = arange(len(data['F+'][1]))
    plots[1].plot(c_len, data['F+'][1])
    plots[1].set_xlabel('Frequency (Hz)')
    plots[1].set_ylabel('Magnitude')
    plots[1].set_xscale('log')
    plots[1].set_ylim([0, 15])
    plots[1].grid(True)
    c_len = arange(len(data['D#+'][1]))
    plots[2].plot(c_len, data['D#+'][1])
    plots[2].set_xlabel('Frequency (Hz)')
    plots[2].set_ylabel('Magnitude')
    plots[2].set_xscale('log')
    plots[2].set_ylim([0, 15])
    plots[2].grid(True)

    plt.tight_layout()
    plt.savefig(img_name)


    img_name = os.path.join(
        settings.IMG_DIR, 'key_detection', 'musicnet', 'frequencyGsharpMCM.png')

    c_len = arange(len(data['G#+'][3]))
    f, plots = plt.subplots(3, 1)
    plots[0].plot(c_len, data['G#+'][3])
    plots[0].set_xlabel('Frequency (Hz)')
    plots[0].set_ylabel('Magnitude')
    plots[0].set_xscale('log')
    plots[0].grid(True)
    plots[0].set_ylim([0, 15])
    c_len = arange(len(data['C+'][0]))
    plots[1].plot(c_len, data['C+'][0])
    plots[1].set_xlabel('Frequency (Hz)')
    plots[1].set_ylabel('Magnitude')
    plots[1].set_xscale('log')
    plots[1].grid(True)
    plots[1].set_ylim([0, 15])
    c_len = arange(len(data['G#-'][0]))
    plots[2].plot(c_len, data['G#-'][0])
    plots[2].set_xlabel('Frequency (Hz)')
    plots[2].set_ylabel('Magnitude')
    plots[2].set_xscale('log')
    plots[2].grid(True)
    plots[2].set_ylim([0, 15])
    plt.tight_layout()
    plt.savefig(img_name)
