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


def ubezier_raccord(X1,Y1,Z1,XP1,YP1,ZP1,pchar1,X2,Y2,Z2,XP2,YP2,ZP2,pchar2, title_raccord): 

      #tracé de la surface

    Xr1 = X1.ravel()
    Xr2 = X2.ravel()

    
    Yr1 = Y1.ravel()
    Yr2 = Y2.ravel()
    Zr1 = Z1.ravel()
    Zr2 = Z2.ravel()

    """
    
    Xr2 = X2.ravel()
    Yr2 = Y2.ravel()
    Zr2 = Z2.ravel()

    """
  
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1,projection='3d')
    ax.plot_trisurf(Xr1,Yr1, Zr1,lw=0.1,edgecolor="black",cmap = cm.get_cmap("Spectral"),alpha=0.5)
    ax.plot_trisurf(Xr2,Yr2, Zr2,lw=0.1,edgecolor="black",cmap = cm.get_cmap("Spectral"),alpha=0.5)
   
    # trace des points 

    ap = np.shape(XP1) # a taille en liste
    aq = np.shape(XP2)
    nb1_p = ap[0] # nb a en int coresspond au nombre de points de controles P.
    nb2_p = ap[1]

    nb1_q = aq[0] # nb a en int coresspond au nombre de points de controles Q.
    nb2_q = aq[1]

    for k1 in range(0,nb1_p) : 

        kk1 = k1
        charrIndice1_p = str(kk1) # trnasforme en str l'indice 1 eg '1'
        numP1 = pchar1 + charrIndice1_p #forme un indice type 'P1'

        for k2 in range(0,nb2_p):

            kk2 = k2
            charrIndice2 = str(kk2) # trnasforme en str l'indice 1 eg '1'
            numP2 = numP1 + charrIndice2 #forme un indice type 'P1'

            epsx = 0.0
            epsy = 0.0
            epsz = 0.0

            ax.text(XP1[k1][k2]+epsx,YP1[k1][k2]+epsy,ZP1[k1][k2]+epsz, numP2)         


    
    for k1 in range(0,nb1_q):
        
        kk1 = k1
        charrIndice1_q = str(kk1) # trnasforme en str l'indice 1 eg '1'
        numP1 = pchar2 + charrIndice1_q #forme un indice type 'P1'

        for k2 in range(0,nb2_q):

            kk2 = k2
            charrIndice2 = str(kk2) # trnasforme en str l'indice 1 eg '1'
            numP2 = numP1 + charrIndice2 #forme un indice type 'P1'

            epsx = 0.0
            epsy = 0.0
            epsz = 0.0

            ax.text(XP2[k1][k2]+epsx,YP2[k1][k2]+epsy,ZP2[k1][k2]+epsz, numP2)         


    plt.title(title_raccord)
    
    plt.show()  







    
    
    


