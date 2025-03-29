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