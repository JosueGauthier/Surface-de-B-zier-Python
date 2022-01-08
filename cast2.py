"""

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%%   function [XPP,YPP]=cast2(t,XP,YP)
%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%%   Enveloppe convexe d'une courbe de Bézier
%%   Construction des points de contrôle 
%%   Deuxième partie t dans [0.5,1.]
%%   
%%   Données : t  valeur du paramètre 
%%             XP, YP coordonnées des points de contrôle
%%
%%   Résultats : XPP,YPP coordonnées des points de contrôle 
%%    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% Introduction au calcul scientifique par la pratique %%%%%%%
%%%%%%%    I. Danaila, P. Joly, S. M. Kaber et M. Postel    %%%%%%%
%%%%%%%                 Dunod, 2005                         %%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  

"""

import numpy as np

def cast2(t,XP,YP):
    
    m = (np.shape(XP)[0]) - 1

    xx = np.zeros(m)
    yy = np.zeros(m)
        
    for k in range(0,m):
            
        xx[m-1-k] = XP[k]
        yy[m-1-k] = YP[k]

    XPP = np.zeros(m)
    YPP = np.zeros(m)

    for kk in range(0,m):

        xxx = xx.copy()
        yyy = yy.copy()

        XPP[m-1-kk] = xx[kk]
        YPP[m-1-kk] = yy[kk]
        
        for k in range(kk,m):

            xx[k]=t*xxx[k]+(1-t)*xxx[k]
            yy[k]=t*yyy[k]+(1-t)*yyy[k]

    XPP[0]=xx[m-1]
    YPP[0]=yy[m-1]


    return (XPP,YPP)