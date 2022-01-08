"""%%
%%   Solution Matlab de l'exercice 3 du projet CAO
%%   Exemple de raccord C0 de deux surfaces de Bézier
%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% Introduction au calcul scientifique par la pratique %%%%%%%
%%%%%%%    I. Danaila, P. Joly, S. M. Kaber et M. Postel    %%%%%%%
%%%%%%%                 Dunod, 2005                         %%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%

"""

import numpy as np
import math
import cmath
import matplotlib.pyplot as plt

from sbezier import sbezier
from ubezier_raccord import ubezier_raccord

# surface 1 

nb1_1=4
nb2_1=5

XP1 = np.array(
    [[0. , 0. , 0. , 0. , 0.],
    [.5 , .5 , .5 , .5 , .5],
    [1. , 1. , 1. , 1. , 1. ],
    [2. , 2. , 2. , 2. , 2. ]])

YP1 = np.array(
    [[ 0. , 1. , 2. , 3. , 4],
    [0. , 1. , 2. , 3. , 4.],
    [0. , 1. , 2. , 3. , 4.],
    [0. , 1. , 2. , 3. , 4. ]])

#  plusieurs choix de ZP

choix = "cyl"

#Choix 1 Une surface plane


if (choix == "plan") :
    ZP1=np.array(
        [[ 0. , 0. , 0. , 0. , 0.],
        [1. , 1. , 1. , 1. , 1.],
        [2. , 2. , 2. , 2. , 2.],
        [3. , 3. , 3. , 3. , 3. ]])

#Choix 2 Une surface aléatoire 
# creation d'une matrice 4x5 aletoire

if (choix == "rand") :
    
    ZP1 = np.random.rand(nb1_1,nb2_1)

#Choix 3 Une surface cylindrique

if (choix == "cyl") :

    xc1=0
    yc1=4
    zc1=1
    r1=4


    ZP1 = np.zeros([nb1_1,nb2_1], dtype= complex)

    for k1 in range(0,nb1_1):

        r1=r1-(k1)*0.2
    
    
        for k2 in range(0,nb2_1):

            ddx = ((XP1[k1][k2])-xc1)**2
            ddy = ((YP1[k1][k2])-yc1)**2        
            ZP1[k1][k2] = zc1 + cmath.sqrt(r1**2 - ddy)

#surface 2

nb1_2=4
nb2_2=5

XP2 = np.array(
    [[2. , 2. , 2. , 2. , 2.],
    [3.5 , 3.5 , 3.5 , 3.5 , 3.5 ],
    [4. , 4. , 4. , 4. , 4. ],
    [5. , 5. , 5. , 5. , 5. ]])

YP2 = np.array(
    [[ 0. , 1. , 2. , 3. , 4],
    [0. , 1. , 2. , 3. , 4.],
    [0. , 1. , 2. , 3. , 4.],
    [0. , 1. , 2. , 3. , 4. ]])

# plusieurs choix de ZP
#  Une surface plane
#  plusieurs choix de ZP
#Choix 1 Une surface plane

if (choix == "plan") :
    ZP2=np.array(
        [[ 0. , 0. , 0. , 0. , 0.],
        [1. , 1. , 1. , 1. , 1.],
        [2. , 2. , 2. , 2. , 2.],
        [3. , 3. , 3. , 3. , 3. ]])

#Choix 2 Une surface aléatoire 
# creation d'une matrice 4x5 aletoire

if (choix == "rand") :

    ZP2 = np.random.rand(nb1_2,nb2_2)

#Choix 3 Une surface cylindrique

if (choix == "cyl") :

    xc2=0
    yc2=4
    zc2=1
    r2=r1

    ZP2 = np.zeros([nb1_2,nb2_2], dtype= complex)

    for k1 in range(0,nb1_2):

        r2=r2-(k1)*0.4

        for k2 in range(0,nb2_2):

            ddx = ((XP2[k1][k2])-xc2)**2
            ddy = ((YP2[k1][k2])-yc2)**2        
            ZP2[k1][k2] = zc2 + cmath.sqrt(r2**2 - ddy)

#les surfaces de Bézier

T1 = np.arange(0.0,1.05,0.05, dtype=float)
T2 = np.arange(0.0,1.1,0.1, dtype=float)


[X1,Y1,Z1,TRI1]=sbezier(T1,XP1,YP1,ZP1)
[X2,Y2,Z2,TRI2]=sbezier(T2,XP2,YP2,ZP2)

#Le tracé

XP=[XP1,XP2]
YP=[YP1,YP2]
ZP=[ZP1,ZP2]

title_raccord = "Un raccord C0 entre surfaces de Bezier"

ubezier_raccord(X1,Y1,Z1,XP1,YP1,ZP1,'P',X2,Y2,Z2,XP2,YP2,ZP2,'Q', title_raccord)













