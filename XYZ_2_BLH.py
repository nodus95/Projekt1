import numpy as np
from math import *
def Np(f, a, e2):
    N = a / np.sqrt(1 - e2 * sin(f)**2)
    return(N)
def xyz2flh(X, Y, Z, a, e2):
    P = sqrt(X**2 + Y**2)
    f = np.arctan(Z/(P*(1 - e2)))
    
    while True:
        N = Np(f, a, e2)
        h = P / cos(f) - N
        fp = f
        f = np.arctan(Z/(P* (1 - e2 * N / (N + h))))
        if abs(fp - f) < (0.000001/206265):
            break
    
    l = np.arctan2(Y, X)
    return(f, l, h)