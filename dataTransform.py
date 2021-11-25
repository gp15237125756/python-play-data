from sklearn import datasets
from sklearn import preprocessing
from sklearn.preprocessing import Binarizer
import pandas as pd


def data_transform():
    boston = datasets.load_boston()
    # print(boston.feature_names)
    # print(boston.data)
    # print(boston.target)
    # print(boston)
    # print(boston.data[:, 4:7])
    df = pd.DataFrame(boston.data[:, 4:7])
    df.columns = boston.feature_names[4:7]
    # print(df)
    """最大-最小规范化"""
    # print((df-df.min())/(df.max()-df.min()))
    # print(preprocessing.minmax_scale(df))
    """z-score规范化"""
    # print((df-df.mean())/df.std())
    """连续属性离散化"""
    print(pd.cut(df.AGE, 5, labels=range(5)))
    print(pd.qcut(df.AGE[:20], 5, labels=range(5)))
    """特征二值化"""
    # X = boston.target.reshape(-1, 1)
    # print(Binarizer(threshold=20).transform(X))


if __name__ == "__main__":
    data_transform()
