import numpy as np
import pandas as pd
import matplotlib

data = pd.read_csv('./kaggle/input/digit-recognizer/train.csv')

# print(data)

data = np.array(data)

# print(data)

m, n = data.shape

# print(m) # 42000
# print(n) # 785

"""
Question: Why is n 785?
Answer: In the dataset, each row represents a digit image, and each image is 28x28 pixels (total 784 pixels). Each pixel's value is stored in a separate column. Additionally, there’s one extra column for the label (the digit itself).

So, n = 784 (pixels) + 1 (label) = 785.
"""

np.random.shuffle(data) # shuffle before splitting into dev and training sets

# Test data
data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]
X_dev = X_dev / 255.

# Train data
data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.
_,m_train = X_train.shape

# print(X_train.shape) # (784, 41000)
# print(m_train) # 41000

# print(Y_train) # [7 1 7 ... 0 1 9]
# print(Y_train.size) # 41000

def init_params():
    W1 = np.random.rand(10, 784) - 0.5
    b1 = np.random.rand(10, 1) - 0.5
    W2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10, 1) - 0.5
    return W1, b1, W2, b2

def ReLU(Z):
    return np.maximum(Z, 0)

def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A    