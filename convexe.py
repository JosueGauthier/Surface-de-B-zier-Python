"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%%   function h=convexe(X,Y) 
%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%%   Mesure de la convexité d'une courbe de Bézier
%%   
%%   Données : XP, YP coordonnées des points de la courbe            
%%
%%   Résultats : h estimation de la convexite de la courbe
%%    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% Introduction au calcul scientifique par la pratique %%%%%%%
%%%%%%%    I. Danaila, P. Joly, S. M. Kaber et M. Postel    %%%%%%%
%%%%%%%                 Dunod, 2005                         %%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%

"""
import numpy as np

def convexe(X,Y):

    n = np.shape(X)[0]

    h = 0
    seuil = 1*(10**(-6))

    for k in range(1,n-1):

        xx = X[k-1]-X[k+1]
        yy = Y[k-1]-Y[k+1]

        if (abs(xx) > seuil):

            yy = Y[k-1]*(X[k]-X[k+1])-Y[k+1]*(X[k]-X[k-1])
            yk=yy/xx
            h = max(h,abs(yk-Y[k]))

        elif (abs(yy) > seuil):

            xx = X[k-1]*(Y[k]-Y[k+1])-X[k+1]*(Y[k]-Y[k-1])
            xk=xx/yy
            h = max(h,abs(xk-X[k]))

    return(h)