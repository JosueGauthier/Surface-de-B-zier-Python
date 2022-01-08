
"""
%%
%%   Construction du point P(t) d'une courbe de Bézier pour 
%%   la valeur t du paramètre, par l'algorithme de Casteljau.
%%   
%%   Données : XP, YP, ZP coordonnées des points de contrôle
%%             t  valeur du paramètre 
%%
%%   Résultats : x,y,z coordonnées du point P(t) dans R^3
%%    
"""

import numpy as np

def cast3d(t,XP,YP,ZP): 

    m = (np.shape(XP)[0]) - 1

    xx = XP.copy()
    yy = YP.copy()
    zz = ZP.copy()

    for kk in range(0,m):

        xxx = xx.copy()
        yyy = yy.copy()
        zzz = zz.copy()

        for k in range(kk,m):

            xx[k+1] = (1-t)*xxx[k]+t*xxx[k+1]
            yy[k+1] = (1-t)*yyy[k]+t*yyy[k+1]
            zz[k+1] = (1-t)*zzz[k]+t*zzz[k+1]

    x=xx[m]
    y=yy[m]
    z=zz[m]  

    return(x,y,z)     







