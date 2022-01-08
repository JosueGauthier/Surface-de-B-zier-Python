# Solution Python de l'exercice 1 du projet CAO
# Construction d'une courbe de Bézier

# Exemple d'un polygone de contrôle convexe

# 0 Import des bibliotheques    

import numpy as np
import matplotlib.pyplot as plt
from cbezier import cbezier
from tbezier import tbezier

# 1 Definition des points de controles
# XP = abscisse des pts de ctrl
# XP = ordonnees des pts de ctrl

qte = 5 
XP= [0,1,2,3,3.5] 
YP= [0,2.5,5,1.5,0]

## 2 échantillonage de la courbe de Bézier

# T=[0:0.05:1.]
T = np.arange(0.0,1.05,0.05, dtype=float) # rajout de 0.05 a 1 car arret a 0.95


[X,Y]=cbezier(T,XP,YP)


## 3 représentation graphique
##  a) définition de la figure

# On place des marges de 0.5 à chaque extremite

xmin=min(XP)-0.5
#print("xmin :",xmin)
xmax=max(XP)+0.5
#print("ymin :",xmin)

ymin=min(YP)-0.5
ymax=max(YP)+0.5

# set axis to = axis([xmin,xmax,ymin,ymax])

plt.axis([xmin,xmax,ymin,ymax])

# def parameters for tbezier function
color='r'
pchar='P'
pcolor='b'
ptrait= '-.'
title = 'Une courbe de Bezier'


tbezier(X,Y,color,XP,YP,pchar,pcolor,ptrait,title)











