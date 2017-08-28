from sklearn.ensemble import RandomForestClassifier

from . import tf_idf


def compute(n_estimators=100, ngram_size=5):
    forest = RandomForestClassifier(n_estimators=n_estimators)
    tf_idf.compute(forest, ngram_size=ngram_size)
