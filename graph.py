import matplotlib.pyplot as plt
import numpy as np


def plot():
    # plt.plot([1, 5, 2, 6, 8, 6])
    # plt.show()
    # plt.savefig('test.png')
    # t = np.arange(0, 4, 0.1)
    # plt.plot(t, t, t, t*2, t**2)
    # plt.show()

    # plt.scatter(range(7), [1, 5, 2, 6, 8, 6, 8], 'rD')
    # plt.show()
    # plt.bar(range(7), [1, 5, 2, 6, 8, 6, 9])
    # plt.show()
    plt.figure(figsize=(8, 6), dpi=100)
    t = np.arange(0., 4, 0.1)
    plt.plot(t, t, color='red', label='l1')
    plt.plot(t, t**2, color='green', label='l2')
    plt.legend(loc='upper left')
    plt.title('graph')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    # x = np.linspace(0, 1)
    # y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
    # plt.plot(x, y)
    # plt.show()


if __name__ == "__main__":
    plot()
