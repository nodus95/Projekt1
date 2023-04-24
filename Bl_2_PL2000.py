import numpy as np
from math import *
def fl2pl2000(f,l,a,e2,ns,m0= 0.999923):
    if ns == 5:
        l0 = radians(15)
    elif ns == 6:
        l0 = radians(18)
    elif ns == 7:
        l0 = radians(21)
    elif ns == 8:
        l0 = radians(24)
    b2 = a**2*(1 - e2)
    ep2 = (a**2 - b2)/b2
    dl = l - l0
    t = tan(f)
    n2 = ep2 * cos(f)**2
    N = a / np.sqrt(1 - e2 * sin(f)**2)
    A0 = 1 - e2/4 - 3 * e2**2/64 - 5 * e2**3/256
    A2 = (3/8) * (e2 + e2**2/4 + 15*e2**3/128)
    A4 = (15/256) * (e2**2 + (3 * e2**3)/4)
    A6 = 35 * e2**3/3072
    sigma = a * (A0*f - A2*sin(2*f) + A4*sin(4*f) - A6*sin(6*f))
    xgk = sigma + (dl**2/2) * N * sin(f)*cos(f)*(1 + (dl**2/12)*cos(f)**2*(5-t**2+9*n2+4*n2**2)+ ((dl**4)/360)*cos(f)**4*(61 - 58*t**2 + t**4 + 270*n2 - 330*n2*t**2))
    ygk = dl*N*cos(f)*(1+(dl**2/6)*cos(f)**2*(1 - t**2 + n2) + (dl**4/120)*cos(f)**4*(5 - 18*t**2 + t**4 + 14*n2 - 58*n2*t**2))
    x2000 = xgk * m0
    y2000 = ygk * m0 + ns * 1000000 + 500000
    return x2000,y2000