"""
%%
%%  Tracé d'une courbe de Bézier et de ses points de contrôle
%%
%%   Données  : X, Y coordonnées des points de l'échantillonage
%%              color couleur de la courbe tracée
%%              XP, YP coordonnées des points de contrôle
%%              pchar caractère associé aux points de contrôle
%%              pcolor couleur de la courbe de contrôle
%%              ptrait type de trait de la courbe de contrôle
%%
%%   Résultats : Tracé graphique de la courbe et des points
%%    

"""
import numpy as np
import matplotlib.pyplot as plt 

def tbezier(X,Y,color,XP,YP,pchar,pcolor,ptrait,title) :

    ligne= pcolor + ptrait #concatene couleur et forme de trait pour obtenir un champ 'b--' eg

    plt.plot(X,Y,color)
    plt.plot(XP,YP,ligne)

    a = np.shape(XP) # a taille en liste
    nb = a[0] # nb a en int coresspond au nombre de points de controles.

    for k in range(0,nb) : 

        kk = k
        charrIndice = str(kk) # trnasforme en str l'indice 1 eg '1'
        numP = pchar + charrIndice #forme un indice type 'P1'

        epsx = 0.1
        epsy = 0.2

        if (k==0) : 
            epsx =0.0
            epsy =-0.2

        if (k==nb-1) :
            epsx =0.1
            epsy =0.0

        plt.text(XP[k]+epsx, YP[k]+epsy, numP)         



    plt.title(title)

    plt.show()
