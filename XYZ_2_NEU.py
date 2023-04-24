from math import *
import numpy as np
def Rneu(f, l):
    R = np.array([[-sin(f) * cos(l), -sin(l), cos(f) * cos(l)],
                  [-sin(f) * sin(l), cos(l), cos(f) * sin(l)],
                  [cos(f), 0, sin(f)]])
def XYZ2neu(dX,f,l):
    R = Rneu(f,l)
    return(R.T @ dX)