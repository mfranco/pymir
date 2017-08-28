from pymir import settings
from pymir.utils.readers import (
    load_musicnet_metadata, load_musicnet_ds, load_midi_map,
    load_midi_notes_map)
from pymir.common import EXISTING_KEYS

import csv
import os
import subprocess


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
seql_learn_cmd = os.path.join(
    BASE_DIR, '../../../../../../../c/seql-sequence-learner/seql_learn')

seql_mkmodel_cmd = os.path.join(
    BASE_DIR, '../../../../../../../c/seql-sequence-learner/seql_mkmodel')


def seql_classify(input_name):
    """

    3. Classify using ./seql_classify (apply the learned model on new examples).
        Usage:  ./seql_classify [-n token_type: 0 word tokens, 1 char tokens; by default set to 1]
        [-t classif_threshold: default 0] [-v verbosity level: default 0] test_file binary_model_file

        Example call:
        ./seql_classify -n 1 -v 2 data/toy.char.test toy.seql.char.model.bin

        Optionally one can tune the classification threshold on the training set, to minimize the
        number of training errors:
      ./seql_classify_tune_threshold_min_errors -n 1 -v 2 data/toy.char.train toy.seql.char.model.bin

        Best threshold:0.0746284

    and use the best theshold for classifying the test set:
      ./seql_classify -n 1 -t 0.0746284 -v 2 data/toy.char.test toy.seql.char.model.bin
    """
    seql_classify_cmd = os.path.join(
        BASE_DIR, '../../../../../../../c/seql-sequence-learner/seql_classify')


    location, fn = os.path.split(input_name)
    model_dir = os.path.join(location, '../', 'models', fn.split('.')[1])
    model_bin = os.path.join(model_dir, 'model.bin')
    results_txt = os.path.join(model_dir, 'results.txt')

    cmd = [
        seql_classify_cmd, '-n', '0', '-v', '1', input_name, model_bin
    ]


    with open(results_txt, 'w') as f:
        subprocess.call(cmd, stdout=f)






def seql_mkmodel(input_name):
    """
    2. Prepare the final model using ./seql_mkmodel (this builds a trie on the features of the model for fast classification).
        Usage: ./seql_mkmodel [-i model_file] [-o binary_model_file] [-O predictors_file]
        Example call:
        ./seql_mkmodel -i toy.seql.char.model -o toy.seql.char.model.bin -O toy.seql.char.model.predictors
    """
    location, fn = os.path.split(input_name)
    model_dir = os.path.join(location, '../', 'models', fn.split('.')[1])


    cmd = [
        'mkdir', '-p', model_dir
    ]

    subprocess.call(cmd)

    binary_model_file = os.path.join(model_dir, 'model.bin')
    predictors_file = os.path.join(model_dir, 'model.predictors')

    cmd = [
        seql_mkmodel_cmd, '-i', input_name, '-o' , binary_model_file, '-O', predictors_file
    ]


    subprocess.call(cmd)


def seql_learn(input_name):
    """
    1. Train using ./seql_learn
      Usage:
        ./seql_learn    [-o objective_function] [-m minsup] [-l minpat] [-L maxpat] [-g maxgap] [-r traversal_strategy ]
                        [-T #round] [-n token_type] [-c convergence_threshold] [-C regularizer_value] [-a l1_vs_l2_regularizer_weight]
                        [-v verbosity] train_file model_file

      Default values for parameters:
        [-o objective: 0 or 2] Objective function. Choice between logistic regression (-o 0) and squared-hinge support vector ma-
         chines (-o 2). By default set to logistic regression.
        [-g maxgap >= 0] Maximum number of consecutive gaps or wildcards allowed in a feature, e.g., a**b,
         is a feature of size 4 with any 2 characters from the input alphabet in the middle. By default
         set to 0.
        [-C regularizer value > 0] Value of the regularization parameter. By default set to 1.
        [-a alpha in [0,1]] Weight of l1 vs l2 regularizer for the elastic-net penalty. By default set to 0.2, i.e., 0.8*l1 + 0.2*l2 regularization.
        [-l minpat >= 1] Threshold on the minimum length of any feature. By default set to 1.
        [-L maxpat] Threshold on the maximum length of any feature. By default the maximum length
         is unrestricted, i.e., at most as long as the longest sequence in the training set.
        [-m minsup >= 1] Threshold on the minimum support of features, i.e., number of sequences containing
         a given feature. By default set to 1.
        [-n token type: 0 or 1] Word or character-level token. Words are delimited by white spaces. By default
         set to 1, character-level tokens.
        [-r traversal strategy: 0 or 1] Breadth First Search or Depth First Search traversal of the search tree.
         By default set to BFS.
        [-c convergence threshold >= 0] Stopping threshold based on change in aggregated score predictions.
         By default set to 0.005.
        [-T maxitr] Number of optimization iterations. By default set to the maximum between 5,000
         and the number of iterations resulting by using a convergence threshold on the aggregated
         change in score predictions.
        [-v verbosity: 1 to 5] Amount of printed detail about the training of the classifier. By default set to 1
         (light profiling information).

        Example call for char-token representation: (all other parameters set to their default values):
        ./seql_learn -n 1 -v 2 data/toy.char.train toy.seql.char.model

    """
    location, fn = os.path.split(input_name)
    model_dir = os.path.join(location, '../', 'models', fn.split('.')[1])


    cmd = [
        'mkdir', '-p', model_dir
    ]

    subprocess.call(cmd)


    model_name = os.path.join(model_dir, 'model.txt')

    cmd = [
        seql_learn_cmd, '-n', '0', input_name, model_name
    ]
    subprocess.call(cmd)


def sql_results():
    """
    Parse result file in order to get confusion matrix
    """
    model_path = os.path.join(settings.DATA_DIR, 'musicnet', 'selq', 'models')

    data = {}
    for key in os.listdir(model_path):
        fname = os.path.join(model_path, key, 'results.txt')
        if os.path.isfile(fname):
            for l in open(fname).readlines():
                if l.startswith('System/Answer'):
                    data[key] = list( map(int, l.split(' ')[5: 9]))
                    break

    matrix = []

    for n in EXISTING_KEYS:
        if n in data:
            d = [n]
            d.extend(data[n])
            matrix.append(d)
        else:
            matrix.append([n, 0, 0, 0, 0])

    fresults = os.path.join(settings.DATA_DIR, 'musicnet', 'selq', 'models', 'results.txt')

    with open(fresults, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['Key', 'TP', 'FP', 'FN', 'TN', ])
        for r in matrix:
            if '#' in r[0]:
                r[0] = r[0].replace('#', '\#')
            writer.writerow(r)



def compute():
    """
    https://github.com/heerme/seql-sequence-learner
    """
    train_path = os.path.join(settings.DATA_DIR, 'musicnet', 'selq', 'train')

    train_files = [
        os.path.join(train_path, f) for f in os.listdir(train_path) if
            os.path.isfile(os.path.join(train_path, f))]

    for f in train_files:
        seql_learn(f)
        seql_mkmodel(f)


    test_path = os.path.join(settings.DATA_DIR, 'musicnet', 'selq', 'test')

    test_files = [
        os.path.join(test_path, f) for f in os.listdir(test_path) if
            os.path.isfile(os.path.join(test_path, f))]

    for f in test_files:
        seql_classify(f)

    sql_results()
