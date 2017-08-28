from sklearn import neighbors

from . import tf_idf

def compute(k=1, ngram_size=5):
    knn = neighbors.KNeighborsClassifier(k)
    tf_idf.compute(knn, ngram_size=ngram_size)
