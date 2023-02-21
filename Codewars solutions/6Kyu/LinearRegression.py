#https://www.codewars.com/kata/5515395b9cd40b2c3e00116c/train/python
import numpy as np
def regressionLine(x, y):
    #OLS from definition
    X = np.hstack((np.ones((len(x), 1)), np.matrix(x).T))
    y = np.matrix(y).T
    beta = np.linalg.inv(X.T @ X) @ X.T @ y
    return tuple(np.round(beta, 4).flat)

import scipy.stats as stats
def regressionLine2(x, y):
    slope, intercept = stats.linregress(x, y)[:2]
    return (round(intercept, 4), round(slope, 4))