import numpy as np
from math import *
#Definiowanie funkcji transformującej kod
def xyz2flh(X, Y, Z, a, e2):
    P = sqrt(X**2 + Y**2)
    f = np.arctan(Z/(P*(1 - e2)))
    
    while True:
        N = a / np.sqrt(1 - e2 * sin(f)**2)
        h = P / cos(f) - N
        fp = f
        f = np.arctan(Z/(P* (1 - e2 * N / (N + h))))
        if abs(fp - f) < (0.000001/206265):
            break
    
    l = np.arctan2(Y, X)
    return(f, l, h)
#Użycie:

f = open('wspXYZ.txt')
lines = f.readlines()[1:]
dane = []
for line in lines:
    line = line.strip()
    line = line.replace(',', '.')
    wsp = line.split()
    dane.append(wsp)
macierzWSP = np.array(dane, dtype=float)
f.close
for i in macierzWSP:
    fi, lam, h = xyz2flh(i[0], i[1], i[2], a = 6378137.000, e2 = 0.00669438002290)
    print(fi, lam, h)