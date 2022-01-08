"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%%   Solution Matlab de l'exercice 2 du projet CAO
%%   Construction d'un point d'une surface de Bézier 
%%   selon l'algorithme De Boor -- Coox
%%

"""

import numpy as np
from cast3d import cast3d


def coox(t1,t2,XP,YP,ZP): 

    np1 = np.shape(XP)[0]
    np2 = np.shape(XP)[1]

    xx1 = np.zeros([np1,1])
    yy1 = np.zeros([np1,1])
    zz1 = np.zeros([np1,1])


    #  construction des points P_q1

    for k1 in range(0,np1):
        #initialisation : points P(k1,1:np2)
        xx2 = np.zeros([np2,1])
        yy2 = np.zeros([np2,1])
        zz2 = np.zeros([np2,1])

        for k2 in range(0,np2):
            
            xx2[k2]=XP[k1][k2]
            yy2[k2]=YP[k1][k2]
            zz2[k2]=ZP[k1][k2]
        
        [x,y,z]=cast3d(t2,xx2,yy2,zz2)

        xx1[k1]=x
        yy1[k1]=y
        zz1[k1]=z
        
    
    
    [x,y,z]=cast3d(t1,xx1,yy1,zz1) 

    return(x,y,z)

    








