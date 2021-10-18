import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom


def Empirical_F(x):
    total = len(x)
    xdict = {}
    for y in x:
        if not y in xdict:
            xdict[y] = 1
        else:
            xdict[y] += 1
    probability_dict = {k: v / total for k, v in xdict.items()}
    x = np.array(x)
    x.sort()
    y = []
    summ = 0
    for i in range(total):
        if i > 0 and x[i - 1] == x[i]:
            y.append(y[i - 1])
        else:
            y.append(summ + probability_dict[x[i]])
            summ = y[i]
    y = np.array(y)
    sol = np.matrix([x, y]).T
    return sol


def Q2_b(size):
    return binom.rvs(n=5, p=1 / 6, size=size)


def Q2_c(X):
    return Empirical_F(X)


def Q2_d(xemp):
    plt.scatter([xemp[:, 0]], [xemp[:, 1]])
    plt.step(xemp[:, 0], xemp[:, 1])
    plt.ylim(0, 1)


def Q2_e():
    y = [0, 1, 2, 3, 4, 5]
    y_cdf = binom.cdf(y, 5, 1 / 6)
    plt.scatter(y, y_cdf)
    plt.plot(y, y_cdf)


def Q2_g(figure, num):
    plt.figure(figure)
    plt.title("x = " + str(num))
    x = Q2_b(num)
    x_emp = Q2_c(x)
    Q2_d(x_emp)
    Q2_e()


if __name__ == '__main__':
    plt.figure(0)
    plt.title("x = 20")
    # Q2.b
    X = Q2_b(20)
    # Q2.c
    x_emp = Q2_c(X)
    # Q2.d
    Q2_d(x_emp)
    # Q2.e + f
    Q2_e()

    # Q2.g
    Q2_g(1, 100)
    Q2_g(2, 200)
    Q2_g(3, 1000)

    plt.show()
