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

def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0
    for i in range(m):
        f_wb = w*x[i]+b
        cost = cost + (f_wb-y[i])**2
     cost = cost/2*m
    return cost

def compute_gradient(x, y, w, b):
    m = x.shape[0]
    dj_dw = 0 ,dj_db = 0
    for i in range(m):
        dj_dw_i = (w*x[i]+b - y[i])*x[i]
        dj_db_i = (w*x[i]+b - y[i])
        dj_dw += dj_dw_i
        dj_db += dj_db_i
    dj_dw = dj_dw/m
    dj_db = dj_db/m
    
    return dj_dw,dj_db;

def gradient_descent(x, y, w_in, b_in, alpha, num_iters, cost_func, gradient_func):
    w = w_in
    b = b_in
    J_history = []
    p_history = []
    
    for i in range(num_iters):
        dj_dw, dj_db = comput_gradient(x, y, w, b)
        b = b-alpha*dj_db
        w = w- alpha*dj_dw
        if i<100000:      # prevent resource exhaustion 
            J_history.append( cost_function(x, y, w , b))
            p_history.append([w,b])
        # Print cost every at intervals 10 times or as many iterations if < 10
        if i% math.ceil(num_iters/10) == 0:
            print(f"Iteration {i:4}: Cost {J_history[-1]:0.2e} ",
                  f"dj_dw: {dj_dw: 0.3e}, dj_db: {dj_db: 0.3e}  ",
                  f"w: {w: 0.3e}, b:{b: 0.5e}")
        return w, b, J_history, p_history
    

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
