from pymir import settings
from pymir.common import EXISTING_NOTES

from sklearn.metrics import confusion_matrix

import numpy as np
import matplotlib.pyplot as plt

import itertools
import os


def compute(db, detected_chords_by_song):
    """
    compares predicted chord vs real chord for every song and
    builds a confusion matrix
    """
    detected = {}
    ground = {}
    detected_chords = []
    ground_chords = []

    for s in detected_chords_by_song:
        detected[s['title']] = s['detected_chords']

    for s in db:
        ground[s['title']] = s['chord_vector']

    for k, v in ground.items():
        if k in detected:
            if len(v) == len(detected[k]):
                detected_chords.extend(detected[k])
                ground_chords.extend(v)

    # ignore chors represented with dash given that are not suppoted by the algorithm
    ground = []
    detected = []
    i = 0
    while i < len(ground_chords): 
        if '-' != ground_chords[i]:
            ground.append(ground_chords[i])
            detected.append(detected_chords[i])
        i += 1

    fig, ax = plt.subplots()
    tick_marks = np.arange(len(EXISTING_NOTES))
    plt.xticks(tick_marks, EXISTING_NOTES, rotation=45)
    plt.yticks(tick_marks, EXISTING_NOTES)

    matrix = confusion_matrix(ground, detected, labels=EXISTING_NOTES)
    thresh = 500

    for i, j in itertools.product(range(matrix.shape[0]), range(matrix.shape[1])):
            plt.text(j, i, matrix[i, j],
                     horizontalalignment="center",
                     size=5,
                     color="black" if matrix[i, j] > thresh else "white")
    plt.ylabel('True chords')
    plt.xlabel('Predicted chords')
    plt.tight_layout()

    fname = (
        os.path.join(
            settings.IMG_DIR,
            'initial_diagnose', 'total_accuracy_confusion_matrix.png'))

    plt.imshow(matrix, interpolation='nearest')
    plt.colorbar()
    plt.savefig(fname)
