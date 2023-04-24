import numpy as np
from math import *
#Definiowanie funkcji transformującej kod
def xyz2flh(X, Y, Z, a, self.e2):
    P = sqrt(X**2 + Y**2)
    f = np.arctan(Z/(P*(1 - self.e2)))
    
    while True:
        N = a / np.sqrt(1 - self.e2 * sin(f)**2)
        h = P / cos(f) - N
        fp = f
        f = np.arctan(Z/(P* (1 - self.e2 * N / (N + h))))
        if abs(fp - f) < (0.000001/206265):
            break
    
    l = np.arctan2(Y, X)
    return(f, l, h)
def dms(x):
    znak = ' '
    if x < 0:
        znak = '-'
        x = abs(x)
    x = x * 180/pi
    d = int(x)
    m = int((x - d) * 60)
    s = (x - d - m/60) *3600
    return(d, m, s)
#Użycie:
f = open('wsp_inp.txt')
lines = f.readlines()[4:]
dane = []
for line in lines:
    line = line.strip()
    wsp = line.split(',')
    dane.append(wsp)
macierzWSP = np.array(dane, dtype=float)
f.close
wynik= 'wynik.txt'
f1= open(wynik, 'w')
f1.write(f'fi                lambda        h\n')
for i in macierzWSP:
    fi, lam, h = xyz2flh(i[0], i[1], i[2], a = 6378137.000, self.e2 = 0.00669438002290)
    print(fi, lam, h)
    fid, fim, fis = dms(fi)
    lamd, lamm, lams = dms(lam)
    fis = round(fis, 5)
    lams = round(lams, 5)
    h = round(h, 3)
    f1.write(f'{fid}°{fim} {fis}, {lamd}°{lamm} {lams}, {h} m\n')