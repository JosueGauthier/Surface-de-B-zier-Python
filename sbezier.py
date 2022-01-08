"""%%
%%   function [X,YZ,TRI]=sbezier(T,XP,YP,ZP)
%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%%   Construction d'un échantillonage de points d'une surface
%%   de Bézier par l'algorithme de Coox.
%%   
%%   Données : XP, YP, ZP coordonnées des points de contrôle
%%             T  ensemble des valeurs du paramètre 
%%
%%   Résultats : X, Y, Z coordonnées des points  P(T)
%%              TRI liste des facettes triangulaires de la surface
"""

import numpy as np
from coox import coox


def sbezier(T,XP,YP,ZP):
    
    n = np.shape(T)[0]

    n1=n-1
    n2=(n**2)

    X = np.zeros([n2,1])
    Y = np.zeros([n2,1])
    Z = np.zeros([n2,1])

    for k1 in range(0,n):
        for k2 in range(0,n):
            
            t1 = T[k1]
            t2 = T[k2]

            [x,y,z]=coox(t1,t2,XP,YP,ZP)

            k = (k1+1) +(k2)*n

            X[k-1]=x 
            Y[k-1]=y
            Z[k-1]=z 


    #  les triangles (facettes de la surface)

    m=n1*n1*2
    TRI = np.zeros([m,3])

    for k1 in range(0,n1):
        for k2 in range(0,n1):

            k=((k1+1)+(k2)*n1)-1
            kk=(k1+1)+(k2)*n

            # premier triangle

            TRI[2*k,0]=kk
            TRI[2*k,1]=kk+1
            TRI[2*k,2]=kk+1+n

            # 2eme triangle
            
            TRI[(2*k)+1,0]=kk
            TRI[(2*k)+1,1]=kk+n
            TRI[(2*k)+1,2]=kk+n+1



    return(X,Y,Z,TRI)















