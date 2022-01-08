"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%%   Solution Matlab de l'exercice 1 du projet CAO
%%   Exemple de raccord G1 de deux courbes de Bézier
%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% Introduction au calcul scientifique par la pratique %%%%%%%
%%%%%%%    I. Danaila, P. Joly, S. M. Kaber et M. Postel    %%%%%%%
%%%%%%%                 Dunod, 2005                         %%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%"""
import numpy as np
import matplotlib.pyplot as plt
from cbezier import cbezier

np1=5

XP1=[ 0. , 1. , 2. , 3. , 3.5   ] 
YP1=[ 0. , 2.5 , 3. , 1.5 , 0.   ]

np2=4

XP2=[ 3.5,   4.5   , 5. , 6.  ] 
YP2=[ 0. ,  -3. , -4. , 0.  ] 

# % les courbes de Bézier

T = np.arange(0.0,1.05,0.05, dtype=float)

[X1,Y1]=cbezier(T,XP1,YP1)
[X2,Y2]=cbezier(T,XP2,YP2)


xmin1=min(XP1)
xmax1=max(XP1)
ymin1=min(YP1)
ymax1=max(YP1)
xmin2=min(XP2)
xmax2=max(XP2)
ymin2=min(YP2)
ymax2=max(YP2)
xmin=min(xmin1,xmin2)-0.75
xmax=max(xmax1,xmax2)+0.75
ymin=min(ymin1,ymin2)-0.75
ymax=max(ymax1,ymax2)+0.75

plt.axis([xmin,xmax,ymin,ymax])

plt.plot(X1,Y1,'b',XP1,YP1,'b:')
plt.plot(X2,Y2,'r',XP2,YP2,'r:')

#nommer les points

for k in range(0,np1):

    kk=k
    char=str(kk)
    P='P'+char
    epsx=0.1
    epsy=0.2

    if (k==1):
        epsx=0.
        epsy=-0.2
    
    if (k==np1):
        epsx=0.2
        epsy=0.
    
    plt.text(XP1[k]+epsx,YP1[k]+epsy,P)


for k in range(0,np2):
    
    kk=k
    char=str(kk)
    P='Q' + char 
    epsx=-0.4
    epsy=-.2

    if (k==1) :
        epsx=-0.4
        epsy=0.

    if (k==np2) :

        epsx=0.1
        epsy=0.
    
    plt.text(XP2[k]+epsx,YP2[k]+epsy,P)

#les vecteurs tangents

print(XP1[np1-2:np1])

plt.plot(XP1[np1-2:np1],YP1[np1-2:np1],'m--')
plt.plot(XP2[0:2],YP2[0:2],'c--')
plt.title('Raccord G1 de deux courbes')
plt.show()
