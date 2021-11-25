from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn import datasets
import pandas as pd


def data_reduction():
    boston = datasets.load_boston()
    X = preprocessing.scale(boston.data)
    pca = PCA(n_components=5)
    pca.fit(X)
    print(pca.explained_variance_ratio_)


if __name__ == "__main__":
    # data_reduction()
    print(10 % 3)
    print(10 / 3)
