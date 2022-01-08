# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:10:28 2021

@author: Chauvat
"""
"""
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%
 %%   Solution Matlab de l'exercice 1 du projet CAO
 %%   Construction d'une courbe de Bézier 
 %%   avec tracé du polygone de contrôle
 %%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%% Introduction au calcul scientifique par la pratique %%%%%%%
 %%%%%%%    I. Danaila, P. Joly, S. M. Kaber et M. Postel    %%%%%%%
 %%%%%%%                 Dunod, 2005                         %%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%
 %%   Exemple d'un polygone de contrôle convexe
 %%

"""
 
import numpy as np
import matplotlib.pyplot as plt
from pbezier import pbezier
from cbezier import cbezier
# % définition des points de contrôle 

np1=5
XP=[ 0. , 1. , 2. , 3. , 3.5   ]
YP=[ 0. , 2.5 , 3. , 1.5 , 0.   ]
# % échantillonage de la courbe de Bézier
T = np.arange(0.0,1.05,0.05,dtype=float)
[X,Y]=cbezier(T,XP,YP)
# %
# % représentation graphique  
# %
# % a) définition de la figure 
nf=1
xmin=min(XP)-0.5
xmax=max(XP)+0.5
ymin=min(YP)-0.5
ymax=max(YP)+0.5
plt.axis([xmin,xmax,ymin,ymax])
# % b) tracé de la courbe de Bézier
color='r'
pchar='P'
pcolor='b'
ptrait='--'
pbezier(X,Y,XP,YP,color,pchar,pcolor,ptrait)
plt.title('Une courbe de Bézier avec son polygone de contrôle')
plt.show()