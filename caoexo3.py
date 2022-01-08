"""
%%   Solution Matlab de l'exercice 3 du projet CAO
%%   Construction d'une surface de Bézier

"""

import numpy as np
import math
import matplotlib.pyplot as plt

from sbezier import sbezier
from ubezier import ubezier

#Exemple d'un polygone de contrôle convexe

nb1 =4
nb2 =5

XP = np.array([[0. , 0. , 0. , 0. , 0.],
     [1. , 1. , 1. , 1. , 1.],
     [2. , 2. , 2. , 2. , 2.],
     [3. , 3. , 3. , 3. , 3. ]])


YP = np.array([[ 0. , 1. , 2. , 3. , 4],
     [0. , 1. , 2. , 3. , 4.],
     [0. , 1. , 2. , 3. , 4.],
     [0. , 1. , 2. , 3. , 4. ]])

#  plusieurs choix de ZP
#Choix 1 Une surface plane

ZPp=np.array([[ 0. , 0. , 0. , 0. , 0.],
     [1. , 1. , 1. , 1. , 1.],
     [2. , 2. , 2. , 2. , 2.],
     [3. , 3. , 3. , 3. , 3. ]])

#Choix 2 Une surface aléatoire 
# creation d'une matrice 4x5 aletoire

ZPr = np.random.rand(nb1,nb2)

#Choix 3 Une surface cylindrique

ZPc = np.zeros([nb1,nb2])

for k1 in range(0,nb1):
    for k2 in range(0,nb2):

        d = ((XP[k1][k2])-1)**2
        d = d + ((YP[k1][k2])-0.5)**2
        ZPc[k1][k2] = math.sqrt(d)

# échantillonage de la surface de Bézier
T = np.arange(0.0,1.05,0.05, dtype=float)

[X,Y,Z,TRI]=sbezier(T,XP,YP,ZPr)

# le tracé de la surface

ubezier(X,Y,Z,XP,YP,ZPc,'P')

