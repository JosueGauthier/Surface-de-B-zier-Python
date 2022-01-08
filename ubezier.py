"""
%%
%%   function  ubezier(TRI,X,Y,Z,XP,YP,ZP,pchar,color)
%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%%   Tracé d'une surface de Bézier et de ses points de contrôle
%%   
%%   Données : TRI liste des facettes triangulaires de la surface
%%   Données : X, Y, Z coordonnées des points de l'échantillonage
%%   Données : XP, YP, ZP coordonnées des points de contrôle
%%             T  ensemble des valeurs du paramètre 
%%              pchar caractère associé aux points de contrôle
%%              pcolor couleur de la courbe de contrôle
%%   

"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import matplotlib.cm as cm


def ubezier(X,Y,Z,XP,YP,ZP,pchar): 

      # % tracé de la surface

    Xr = X.ravel()
    Yr = Y.ravel()
    Zr = Z.ravel()
  
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1,projection='3d')
    
    #ax.plot_trisurf(Xr,Yr, Zr,lw=0.1,edgecolor="black",cmap = cm.get_cmap("Spectral"),alpha=0.5)
    
    ax.plot_trisurf(Xr,Yr, Zr,lw=0.1,edgecolor=None ,cmap = cm.get_cmap("Spectral"),alpha=0.8)
    
    XrP = XP.ravel()
    YrP = YP.ravel()
    ZrP = ZP.ravel()
  
    #fig = plt.figure()
    #ax = fig.add_subplot(1,1,1,projection='3d')
    #ax.plot_trisurf(XrP,YrP, ZrP,lw=0.1,edgecolor="black",cmap = cm.get_cmap("magma"),alpha=0.5)
    


    # trace des points 

    a = np.shape(XP) # a taille en liste
    nb1 = a[0] # nb a en int coresspond au nombre de points de controles.
    nb2 = a[1]

    for k1 in range(0,nb1) : 

        kk1 = k1
        charrIndice1 = str(kk1) # trnasforme en str l'indice 1 eg '1'
        numP1 = pchar + charrIndice1 #forme un indice type 'P1'

        for k2 in range(0,nb2):

            kk2 = k2
            charrIndice2 = str(kk2) # trnasforme en str l'indice 1 eg '1'
            numP2 = numP1 + charrIndice2 #forme un indice type 'P1'

            epsx = 0.0
            epsy = 0.0
            epsz = 0.0

            ax.text(XP[k1][k2]+epsx,YP[k1][k2]+epsy,ZP[k1][k2]+epsz, numP2)         

    plt.title('Une surface de Bézier')
    
    plt.show()  







    
    
    


