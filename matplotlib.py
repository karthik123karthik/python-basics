import numpy as np
import matplotlib.pyplot as plt
plt.style.use('./deeplearning.mplstyle')

import numpy as np
%matplotlib widget
import matplotlib.pyplot as plt
from lab_utils_uni import plt_intuition, plt_stationary, plt_update_onclick, soup_bowl
plt.style.use('./deeplearning.mplstyle')

# using numpy to create dataset
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

# getting number of size of dataset
m = x_train.shape[0]
print(m)

# getting ith data in the dataset
print(x_train[0], y_train[0])

# define compute function
def compute_func(x_train, w, b):
    m = x_train.shape[0]
    temp_y_train = np.zeros(m)
    for i in range(m):
        temp_y_train[i] = w*x_train[i]+b
    return temp_y_train

# w and b parameters
w = 100
b = 100
temp_y_train = compute_func(x_train, w, b)
# draw the line
plt.plot(x_train, temp_y_train, c='b', lable="our prediction")

#plot the data
plt.scatter(x_train, y_train, marker='X', c='r')
plt.title("house pricing")
plt.xlabel("size of the house in square feet")
plt.ylabel("price of house in 1000's of dollars")
plt.legend()
plt.show()
