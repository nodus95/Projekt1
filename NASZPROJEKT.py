# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 23:09:24 2023

@author: krzys
"""
import numpy as np
from math import *
from argparse import ArgumentParser
    
class Transformations:
    
    def __init__(self,elipsoida):
        
        self.a = elipsoida[0]
        
        self.e2 = elipsoida[1]

    def XYZ2BLH(self, X, Y, Z,):
        wynik = []
        for X, Y, Z in zip(X, Y, Z):
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
            wynik.append([np.rad2deg(f), np.rad2deg(l), h])
        return(wynik)

    def XYZ2NEU(self, X, Y, Z, X0, Y0, Z0):
        wyniki = []
        a = self.a
        e2 = self.e2
        p = np.sqrt(X0**2+Y0**2)
        fi = np.arctan(Z0/(p*(1-e2)))
        while True:
            N = a/ np.sqrt(1 - e2 * sin(fi)**2)
            h = (p/np.cos(fi)) - N
            fi1 = fi
            fi = np.arctan((Z0/p)/(1-((N*e2)/(N+h))))
            if abs(fi1-fi)<(0.000001/206265):
                break 
        N = a/ np.sqrt(1 - e2 * sin(fi)**2)
        h = p/np.cos(fi) - N
        lam = np.arctan(Y0/X0)
        R_neu = np.array([[-np.sin(fi)*np.cos(lam), -np.sin(lam), np.cos(fi)*np.cos(lam)],
                         [-np.sin(fi)*np.sin(lam), np.cos(lam), np.cos(fi)*np.sin(lam)],
                         [np.cos(fi), 0, np.sin(fi)]])

        for X, Y, Z in zip(X, Y, Z):
            X_sr = [X-X0, Y-Y0, Z-Z0] 
            X_rneu = R_neu.T@X_sr
            wyniki.append(X_rneu.T)
        return wyniki
    
    def BLH2XYZ(self, f, l, h):
        wynik = []
        for f, l, h in zip(f, l, h):
            a = self.a
            e2 = self.e2
            N = a/ np.sqrt(1 - e2 * sin(f)**2)
            X = (N + h) * np.cos(f) * np.cos(l)
            Y = (N + h) * np.cos(f) * np.sin(l)
            Z = (N + h - N * e2) * np.sin(f)
            wynik.append([X, Y, Z])
        return(wynik)

    
    def BL2PL2000(self, f, l):
        wynik = []
        for f, l in zip (f,l):
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
            wynik.append([x2000, y2000])
        return (wynik)
    
    def BL2PL1992(self, f, l):
        wynik = []
        for f, l in zip (f,l):
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
            wynik.append([x92, y92])
        return (wynik)
    
    def wczytywanie_wspolrzednych(self,plik_dane, trans):
            wsp = np.genfromtxt(plik_dane,delimiter = " ")
            if trans == 'XYZ2BLH':
                transformed = self.XYZ2BLH(wsp[:,0], wsp[:,1], wsp[:,2])
                np.savetxt(f"twoje_wyniki_{trans}_{args.elip}.txt", transformed, delimiter=' ', fmt='%0.10f %0.10f %0.3f')
            elif trans == 'BLH2XYZ':
                transformed = self.BLH2XYZ(np.deg2rad((wsp[:,0])), np.deg2rad(wsp[:,1]), wsp[:,2])
                np.savetxt(f"twoje_wyniki_{trans}_{args.elip}.txt", transformed, delimiter=' ',fmt='%0.3f %0.3f %0.3f')
            elif trans == 'XYZ2NEU':
                transformed = self.XYZ2NEU(wsp[1:,0], wsp[1:,1], wsp[1:,2], wsp[0,0], wsp[0,1], wsp[0,2])
                np.savetxt(f"twoje_wyniki_{trans}._{args.elip}.txt", transformed, delimiter=' ', fmt='%0.3f %0.3f %0.3f')
            elif trans == 'BL2PL2000':
                transformed = self.BL2PL2000(np.deg2rad(wsp[:,0]), np.deg2rad(wsp[:,1]))
                np.savetxt(f"twoje_wyniki_{trans}_{args.elip}.txt", transformed, delimiter=' ', fmt='%0.3f %0.3f')
            elif trans == 'BL2PL1992':
                transformed = self.BL2PL1992(np.deg2rad(wsp[:,0]), np.deg2rad(wsp[:,1]))
                np.savetxt(f"twoje_wyniki_{trans}_{args.elip}.txt", transformed, delimiter=' ',fmt='%0.3f %0.3f')
        

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-file', type=str, help='Tutaj konieczne jest podanie sciezki do pliku z danymi wejsciowymi ktore chcemy przetransformowac')
    parser.add_argument('-elip', type=str, help='Tutaj konieczne jest podanie elipsoidy. Obslugiwane elisoidy: WGS84, GRS80 lub Krasowski')
    parser.add_argument('-trans', type=str, help='Tutaj konieczne jest podanie transormacji. Obslugiwane transformacje: XYZ2BLH, BLH2XYZ, XYZ2NEU, BL2PL2000, BL2PL1992') 
    args = parser.parse_args()
    el = {'WGS84':[6378137.000, 0.00669438002290], 'GRS80':[6378137.000, 0.00669438002290], 'KRASOWSKI':[6378245.000, 0.00669342162296]}
    trans = {'XYZ2BLH': 'XYZ2BLH','BLH2XYZ': 'BLH2XYZ', 'BL2PL2000':'BL2PL2000','BL2PL1992':'BL2PL1992','XYZ2NEU':'XYZ2NEU'}
 
    try:
        xyz = Transformations(el[args.elip.upper()])
        xtytzt = xyz.wczytywanie_wspolrzednych(args.file, trans[args.trans.upper()])
        print('Plik z twoimi przetransformowanymi wspolrzednymi zostal utworzony ;)')
        
    except FileNotFoundError:
        print('Niestety podales bledny lub nieistniejacy plik')
    except KeyError:
        print('Zle wpisales nazwe elipsoidy lub transformacji lub podales nieobslugiwana elipsoide lub transformacje.')
    except IndexError:
        print('Dane w pliku wejsciowym sa blednie podane.')
    except ValueError:
        print('Dane w pliku wejsciowym sa blednie podane.')
    finally:
        print('To już wszytko. Dziękujemy za skorzystanie z naszego programu.')

