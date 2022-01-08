"""

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%%   function trectan(xmi,xma,ymi,yma,color) 
%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%%   Tracé d'un rectangle 
%%   
%%   Données  : xmin,xmax,ymin,ymax coordonnées des sommets
%%
%%   Résultats : tracé du rectangle 
%%    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% Introduction au calcul scientifique par la pratique %%%%%%%
%%%%%%%    I. Danaila, P. Joly, S. M. Kaber et M. Postel    %%%%%%%
%%%%%%%                 Dunod, 2005                         %%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%

"""

import numpy as np
import matplotlib.pyplot as plt

def trectan(xmi,xma,ymi,yma,color,title): 
    
    xx = np.zeros(5)
    yy = np.zeros(5)

    xx[0]=xmi
    xx[1]=xma
    xx[2]=xx[1]
    xx[3]=xx[0]
    xx[4]=xx[0]
    yy[0]=ymi
    yy[1]=yy[0]
    yy[2]=yma
    yy[3]=yy[2]
    yy[4]=yy[0]
    plt.plot(xx,yy,color)

    plt.title(title)
    


