# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%
# %%  function pbezier(X,Y,XP,YP,color,pchar,pcolor,ptrait)
# %%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%
# %%  Tracé d'une courbe de Bézier et de son polygone de contrôle
# %%
# %%   Données : X, Y coordonnées des points de l'échantillonage
# %%             XP, YP coordonnées des points de contrôle
# %%             color couleur de la courbe tracée
# %%             pchar caractère associé aux points de contrôle
# %%             pcolor couleur de la courbe de contrôle
# %%             ptrait type de trait de la courbe de contrôle
# %%
# %%   Résultats : Tracé graphique de la courbe et du polygone
# %%    
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%% Introduction au calcul scientifique par la pratique %%%%%%%
# %%%%%%%    I. Danaila, P. Joly, S. M. Kaber et M. Postel    %%%%%%%
# %%%%%%%                 Dunod, 2005                         %%%%%%%



import numpy as np
import matplotlib.pyplot as plt

def pbezier(X,Y,XP,YP,color,pchar,pcolor,ptrait):

    ligne= pcolor+ptrait

    #signifie que tu rajoute le premier element de la liste XP a la fin de XP0, si XP = [1,2,3], donc XP0 =[1,2,3,1]
    XP0=XP[:]
    YP0=YP[:]
    XP0.extend([XP[0]])
    YP0.extend([YP[0]])



    plt.plot(X,Y,color)
    plt.plot(XP0,YP0,ligne)


    np1= np.shape(XP)[0]

    for k in range (0,np1):
        kk=k
        char=str(kk)
        P= pchar+char
        epsx=0.1
        epsy=0.2
        if (k==0) :
            epsx=0.
            epsy=-0.2
        if (k==np1-1):
            epsx=0.1
            epsy=0.0
        plt.text(XP[k]+epsx,YP[k]+epsy,P)

    

