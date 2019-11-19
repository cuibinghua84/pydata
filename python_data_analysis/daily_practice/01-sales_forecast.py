# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:28:23 2019

@author: p_bhcui
"""


import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

raw_data = pd.read_csv('D:/data/python_book_v2/chapter1/data.txt')

num = int(raw_data.shape[0] * 0.7)
x, y = raw_data[['money']], raw_data[['amount']]
x_train, x_test = x[:num], x[num:]
y_train, y_test = y[:num], y[num:]

plt.scatter(x_train, y_train)
plt.show()

model = linear_model.LinearRegression()
model.fit(x_train, y_train)

predict_test_y = model.predict(x_test)
print("Mean squared error: %.0f" % mean_squared_error(y_test, predict_test_y))
print("Variance score: %.2f" % r2_score(y_test, predict_test_y))

model_coef = model.coef_
model_intercept = model.intercept_
print("coef is: ", model_coef)
print("intercept is: ", model_intercept)

new_x = 84610
pre_y = model.predict([[new_x]])
print(pre_y)