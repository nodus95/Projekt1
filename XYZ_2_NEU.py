from math import *
import numpy as np
def XYZ2neu(dX,f,l):
    R = np.array([[-sin(f) * cos(l), -sin(l), cos(f) * cos(l)],
                  [-sin(f) * sin(l), cos(l), cos(f) * sin(l)],
                  [cos(f), 0, sin(f)]])
    return(R.T @ dX)