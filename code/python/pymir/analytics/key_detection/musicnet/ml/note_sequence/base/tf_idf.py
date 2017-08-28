from pymir import settings
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sklearn.metrics import confusion_matrix, recall_score, precision_score, f1_score

from pymir.common import EXISTING_NOTES, EXISTING_KEYS
from statistics import mean


import os
import numpy as np
import itertools
import matplotlib.pyplot as plt
import csv


EXCLUDE_KEYS = ('F#-', 'F#+', 'G#-', 'B+', 'A#-')

def tokenize(text):
    return [tok.strip().upper() for tok in text.split(' ') if tok]


def build_model(train_fname, clf, ngram_size=5):
    """
    http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
    """
    corpus = []
    labels = []

    with open(train_fname, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if row[0] not in EXCLUDE_KEYS:
                labels.append(row[0])
                corpus.append(' '.join(row[1: ]) )
            else:
                print(row[0])
    vectorizer = CountVectorizer(
        tokenizer=tokenize, ngram_range=(1, ngram_size),
        )

    # Occurrence count is a good start but there is an issue: longer documents will have
    # higher average count values than shorter documents, even though they might talk about the same topics.
    X_counts = vectorizer.fit_transform(corpus)


    # To avoid these potential discrepancies it suffices to divide the number of occurrences
    # of each word in a document by the total number of words in the document: these new features
    # are called tf for Term Frequencies.
    tfidf_transformer = TfidfTransformer(use_idf=True).fit(X_counts)
    X_tf = tfidf_transformer.transform(X_counts)
    print('Matrix shape: {} Labels X {} Features'.format(X_tf.shape[1], X_tf.shape[0]))

    return {
        'X_tf': X_tf,
        'vectorizer': vectorizer,
        'model': clf.fit(X_tf, labels),
        'labels': labels,
        'tfidf_transformer': tfidf_transformer
    }


def  test_model(
        model=None, vectorizer=None, test_fname=None, X_tf=None, labels=None, tfidf_transformer=None):
    test_corpus = []
    test_labels = []
    with open(test_fname, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            test_labels.append(row[0])
            test_corpus.append(' '.join(row[1: ]) )

    test_data = vectorizer.transform(test_corpus)
    test_data_tfidf = tfidf_transformer.transform(test_data)
    predicted = model.predict(test_data_tfidf).tolist()


    fig, ax = plt.subplots()
    tick_marks = np.arange(len(EXISTING_NOTES))
    plt.xticks(tick_marks, EXISTING_NOTES, rotation=45)
    plt.yticks(tick_marks, EXISTING_NOTES)
    matrix = confusion_matrix(test_labels, predicted, labels=EXISTING_KEYS)
    thresh = 500

    for i, j in itertools.product(range(matrix.shape[0]), range(matrix.shape[1])):
            plt.text(j, i, matrix[i, j],
                     horizontalalignment="center",
                     size=5,
                     color="black" if matrix[i, j] > thresh else "white")
    plt.ylabel('True Keys')
    plt.xlabel('Predicted Keys')
    plt.tight_layout()

    fname = (
        os.path.join(
            settings.IMG_DIR,
            'key_detection', 'musicnet', 'tfidf_confusion_matrix.png'))

    plt.imshow(matrix, interpolation='nearest')
    plt.colorbar()
    plt.savefig(fname)

    hit = []
    miss = []

    for x, y in zip(test_labels, predicted):
        if x == y:
            hit.append(1)
        else:
            miss.append(1)
    print('total hits: {} \n'.format(len(hit)))
    print('total misses: {} \n'.format(len(miss)))

    recall = recall_score(
        test_labels,
        predicted,
        average=None, labels=EXISTING_KEYS)

    precision = precision_score(
        test_labels, predicted, average=None, labels=EXISTING_KEYS)

    f1 = f1_score(
        test_labels, predicted, average=None, labels=EXISTING_KEYS)

    print('Average Recall: {0:.4f}'.format(mean(recall)))
    print('Avegare Precision: {0:.4f}'.format(mean(precision)))
    print('Average F1: {0:.4f}'.format(mean(f1)))

    print('\nPerformance by Key: \n')
    
    print('Key  Recall  Precision   F1')
    for key, rc, pc, f in zip(EXISTING_KEYS, recall, precision, f1):
        print('{0} {1:.4f} {2:.4f} {3:.4f}'.format(key, rc, pc, f))

def compute(clf, ngram_size=5):
    """
    Base model of key detection for Musicnet metadata based in TF-IDF and
    Random forest or KNN
    """
    test_fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'sequence_of_notes', 'musicnet_test.csv'))

    train_fname = (
        os.path.join(settings.DATA_DIR, 'musicnet', 'representations',
        'sequence_of_notes', 'musicnet_train.csv'))
    model = build_model(train_fname, clf, ngram_size=ngram_size)
    model['test_fname'] = test_fname
    test_model(**model)
