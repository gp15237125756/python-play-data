import pandas_datareader.data as web
from sklearn import datasets


def DataReader():
    iris = datasets.load_iris()
    print(iris.feature_names)
    print(iris.data)
    print(iris.target)


if __name__ == "__main__":
    DataReader()
