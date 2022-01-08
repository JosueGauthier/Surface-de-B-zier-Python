#        Construction du point P(t) d'une courbe de Bézier pour 
#        la valeur t du paramètre, par l'algorithme de Casteljau.
  
#        Données : XP, YP coordonnées des points de contrôle
#            t  valeur du paramètre 

#        Résultats : x,y coordonnées du point P(t)

import numpy as np

def casteljau(t,XP,YP) : 
    
    a = np.shape(XP)
    m = a[0] 
    m = m-1  #m = nombre de points de contrôle


    xx = XP.copy()
    yy= YP.copy()

    for kk in range(0,m):
        
        xxx = xx.copy()
        yyy = yy.copy()

        for k in range(kk,m):
            
            xx[k+1] = (1-t)*xxx[k] +t*xxx[k+1]
            yy[k+1] = (1-t)*yyy[k] +t*yyy[k+1]
    x=xx[m]
    y=yy[m]

    return(x,y)



