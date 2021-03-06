# This code is inspired from this post:
# http://www.kdnuggets.com/2015/10/neural-network-python-tutorial.html?utm_content=buffer2cfea&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
# Python 3 code

import numpy as np

from sigmoid import sigmoid

np.random.seed(314)

# Feature matrix and targets
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = np.array([[0, 1, 1, 0]]).T


# Random initialization of first and second hidden layers
syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

print(syn0.shape, syn1.shape)

# Number of back-propagation steps
N_STEPS = 60000

for step in range(N_STEPS):
    l1 = sigmoid(X, syn0)
    l2 = sigmoid(l1, syn1)
    l2_delta = (y - l2) * (l2 * (1 - l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1 - l1))
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)

print(syn0)
print(syn1)
