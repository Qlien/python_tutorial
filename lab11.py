import numpy as np
import random
import timeit

from math import sin, cos

randoms = np.random.uniform(0, 1, size=1000000)
"""randoms = randoms + 1

randoms2 = [random.uniform(0, 1) + 1  for x in range(0, 10000)]


def f1(tab):
    for idx, val in enumerate(tab):
        tab[idx] = sin(val) + cos(val)

def f2(tab):
    np.sin(tab) + np.cos(tab)

tab = np.random.uniform(-1000, 1000, size=10000000)
f2(tab)




def cube_sum(x):
    result = 0
    for i in range(len(x)):
        result += x[i] ** 3
    return result

def almost_variance(x):
    m = sum(x) / len(x)
    result = 0
    for i in range(len(x)):
        result += (x[i] - m) ** 4
    result /= len(x)
    return result

def numpy_cube_sum(x):
    return np.sum(np.power(x, 3))

def numpy_almost_variance(x):
    x_mean = np.mean(x)
    return np.mean(np.power(x - x_mean, 4))


cube_sum(randoms)
almost_variance(randoms)
#numpy_cube_sum(randoms)
#numpy_almost_variance(randoms)

print(np.arange(101).reshape((101, 1)) * np.arange(101))


points = np.random.random(size=(10, 5))


# print(np.tile(points, (10, 1, 1)).T)

pointsMatrix = np.tile(points, (10,1,1))
tPoints = np.transpose(pointsMatrix, axes=(1,0,2))
diffMatrix = pointsMatrix - tPoints

# print(diffMatrix[:,:,0])

# print(np.power(diffMatrix, 2)[:,:,0])
res = np.sum(np.power(diffMatrix, 2), axis=2)
res = np.power(res, 0.5)


print(res)
print(res.shape)
print(np.all(res.T==res))


def white(x):
    return (x - np.mean(x, axis=0)) / np.std(x, axis=0)

x = np.random.rand(100, 2)
y = white(x)
print(y.shape)
print(np.mean(y), np.std(y))

"""



pts = np.random.uniform(0, 1, size=(100, 2))
a = [0.5, 0.5]

index = np.argmin(np.sum(np.abs(pts - a), axis=1))
print(index)
print(pts[index])