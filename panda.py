import numpy as np
import pandas as pd


def cal():
    aArray = np.ones((3, 4))
    print(aArray)


def ndarray():
    aArray = np.array([(1, 2, 3), (4, 5, 6)])
    print(aArray.shape)
    print(aArray.ndim)
    print(aArray.itemsize)
    r = np.arange(1, 10, 0.5)
    print(r)
    print(r[0:2])
    f = np.full((10, 10), np.pi)
    print(f)
    print(np.full_like(f, 8))
    print(np.eye(4, k=1))
    A = np.random.rand(3, 5)
    x = np.arange(0, 101)
    print(x)
    print(x[x < 50])
    print(x[(x > 50) & (x % 2 == 0)])
    x[(x % 2 == 0)] = -1
    print(x)
    np.where(x % 2 == 0, -1, x)
    print(x)
    score = np.array([(98, 85, 73), (84, 75, 56)])
    mean = score.mean(axis=1, keepdims=True)
    print(mean)
    print(score - mean)


def series():
    s = pd.Series(data=[1, 2, 6], index=[1, 2, 3])
    print(s)
    print(s.index)
    print(s.values)
    print(s[2])
    print(s * 2)
    print(np.exp(s))
    a = {'A': '1', 'B': '2'}
    idx = ['A', 'B', 'C']
    ss = pd.Series(a, idx)
    print(ss)
    print(pd.isnull(ss))


def dataframes():
    data = {'name': ['x', 'y', 'z'], 'pay': [100, 200, 300]}
    d = pd.DataFrame(data)
    print(d.shape)
    print(d.ndim)
    print(d['name'])
    print(d.name)
    print(d.iloc[:2, 1])
    # del d['pay']
    print(d['pay'].min())
    print(d['pay'].max())
    print(d[d.pay > 200])


if __name__ == "__main__":
    # cal()
    ndarray()
    # series()
    # dataframes()
