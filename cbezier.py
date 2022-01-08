#Construction d'un échantillonage de points d'une courbe
#de Bézier par l'algorithme de Casteljau.

#Données : XP, YP coordonnées des points de contrôle
#          T  ensemble des valeurs du paramètre 

#Résultats : X, Y coordonnées des points  P(T)


import numpy as np
from casteljau import casteljau


def cbezier(T,XP,YP): 

    a = np.shape(T) # a = array a=(21.,) eg
    n = a[0] # recuperer la valeur de l'array un int

    X = np.array([])
    Y = np.array([])

    for k in range(0,n) :

        t = T[k]
        [x,y] = casteljau(t,XP, YP)
        X = np.append(X,x)
        Y = np.append(Y,y)

    return(X,Y)
