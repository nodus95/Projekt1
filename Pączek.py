import numpy as np
from math import *
from argparse import ArgumentParser

class Transformations:
    def __init__(self, elipsoida):
        self.elipsoida = elipsoida
        if elipsoida == 'GRS80':
            self.a = 6378137
            self.e2 = 0.00669438002290
        elif elipsoida == 'WGS84':
            self.a = 6378137
            self.e2 = 0.00669438
        elif elipsoida == 'Krasowski':
            self.a = 6378245
            self.e2 = 0.00669342162296
        else:
            raise NotImplementedError(f"{elipsoida} niestety nie obsługujemy takiej elipsoidy... ")

    def XYZ2BLH(self, X, Y, Z,):
        a = self.a
        e2 = self.e2
        P = sqrt(X**2 + Y**2)
        f = np.arctan(Z/(P*(1 - self.e2)))
    
        while True:
            N = a/ np.sqrt(1 - e2 * sin(f)**2)
            h = P / cos(f) - N
            fp = f
            f = np.arctan(Z/(P* (1 - e2 * N / (N + h))))
            if abs(fp - f) < (0.000001/206265):
                break
    
        l = np.arctan2(Y, X)
        return(f, l, h)
    
    def XYZ2NEU(self, xa, ya, za, xb, yb, zb):
        dwsp = np.array([xb - xa, yb - ya, zb - za])
        fi, lam, ha = XYZ2BLH(xa, ya, za)
        R = np.array([[-sin(fi) * cos(lam), -sin(lam), cos(fi) * cos(lam)],
                      [-sin(fi) * sin(lam), cos(lam), cos(fi) * sin(lam)],
                      [cos(fi), 0, sin(fi)]])
        dx = R.T @ dwsp
        n = dx[1]
        e = dx[0]
        u = dx[2]
        return(n, e, u)
    
    def BLH2XYZ(self, f, l, h):
        a = self.a
        e2 = self.e2
        N = a/ np.sqrt(1 - e2 * sin(f)**2)
        X = (N + h) * cos(f) * cos(l)
        Y = (N + h) * cos(f) * sin(l)
        Z = (N + h - N * e2) * sin(f)
        return(X, Y, Z)
    
    def BL2PL2000(self, f, l):
        a = self.a
        e2 = self.e2
        if l <= 16.5:
            l0 = radians(15)
            ns = 5
        elif 16.5 < l <= 19.5:
            l0 = radians(18)
            ns = 6
        elif 19.5 < l <= 22.5:
            l0 = radians(21)
            ns = 7
        elif l > 22.5:
            l0 = radians(24)
            ns = 8
        m0 = 0.999923
        b2 = a**2*(1 - e2)
        ep2 = (a**2 - b2)/b2
        dl = l - l0
        t = tan(f)
        n2 = ep2 * cos(f)**2
        N = a/ np.sqrt(1 - e2 * sin(f)**2)
        A0 = 1 - e2/4 - 3 * e2**2/64 - 5 * e2**3/256
        A2 = (3/8) * (e2 + e2**2/4 + 15*e2**3/128)
        A4 = (15/256) * (e2**2 + (3 * e2**3)/4)
        A6 = 35 * e2**3/3072
        sigma = a* (A0*f - A2*sin(2*f) + A4*sin(4*f) - A6*sin(6*f))
        xgk = sigma + (dl**2/2) * N * sin(f)*cos(f)*(1 + (dl**2/12)*cos(f)**2*(5-t**2+9*n2+4*n2**2)+ ((dl**4)/360)*cos(f)**4*(61 - 58*t**2 + t**4 + 270*n2 - 330*n2*t**2))
        ygk = dl*N*cos(f)*(1+(dl**2/6)*cos(f)**2*(1 - t**2 + n2) + (dl**4/120)*cos(f)**4*(5 - 18*t**2 + t**4 + 14*n2 - 58*n2*t**2))
        x2000 = xgk * m0
        y2000 = ygk * m0 + ns * 1000000 + 500000
        return x2000,y2000
    
    def BL2PL1992(self, f, l):
        l0=radians(19)
        m0 = 0.9993
        a = self.a
        e2 = self.e2
        b2 = a**2*(1 - e2)
        ep2 = (a**2 - b2)/b2
        dl = l - l0
        t = tan(f)
        n2 = ep2 * cos(f)**2
        N = a/ np.sqrt(1 - e2 * sin(f)**2)
        A0 = 1 - e2/4 - 3 * e2**2/64 - 5 * e2**3/256
        A2 = (3/8) * (e2 + e2**2/4 + 15*e2**3/128)
        A4 = (15/256) * (e2**2 + (3 * e2**3)/4)
        A6 = 35 * e2**3/3072
        sigma = a* (A0*f - A2*sin(2*f) + A4*sin(4*f) - A6*sin(6*f))
        xgk = sigma + (dl**2/2) * N * sin(f)*cos(f)*(1 + (dl**2/12)*cos(f)**2*(5-t**2+9*n2+4*n2**2)+ ((dl**4)/360)*cos(f)**4*(61 - 58*t**2 + t**4 + 270*n2 - 330*n2*t**2))
        ygk = dl*N*cos(f)*(1+(dl**2/6)*cos(f)**2*(1 - t**2 + n2) + (dl**4/120)*cos(f)**4*(5 - 18*t**2 + t**4 + 14*n2 - 58*n2*t**2))
        x92 = xgk * m0 - 5300000
        y92 = ygk * m0 + 500000
        return x92,y92
    
if __name__ == '__main__':
    argpars = ArgumentParser()
    argpars.add_argument('-file', type=str, help='Tutaj należy podać ścieżkę pliku z danymi wejściowego')
    argpars.add_argument('-elip', type=str, help='Tutaj należy podać elipsoidę na której mają być przeliczane współrzędne. Obsługiwane elipsoidy: WGS84, GRS80 lub Krasowski')
    argpars.add_argument('-trans', type=str, help='Tutaj podać nazwę wybranej transformacji. Obsługiwane transformacje: XYZ2BLH, XYZ2NEU, BLH2XYZ, Bl2PL2000, BL2PL1992')
    args = argpars.parse_args()

