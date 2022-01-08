"""

%%   Solution Matlab de l'exercice 2 du projet CAO
%%   Intersection de deux courbes de Bézier

"""

#% définition des points de contrôle 

import numpy as np
import matplotlib.pyplot as plt
import sys

from cbezier import cbezier
from drectan import drectan
from rbezier import rbezier
from tbezier import tbezier 
from trectan import trectan
from dbezier import dbezier
from casteljau import casteljau
from ktest import ktest
from tbezierintersec import tbezierintersec
from tbezierintersec1 import tbezierintersec1


Val_ktest = 1

[XP1,YP1,XP2,YP2] = ktest(Val_ktest)

T = np.arange(0.0,1.05,0.05, dtype=float) # rajout de 0.05 a 1 car arret a 0.95

# % échantillonage des courbes de Bézier

[X1,Y1]= cbezier(T,XP1,YP1)
[X2,Y2]= cbezier(T,XP2,YP2)

# % mise en place des rectangles

[xmin1,xmax1,ymin1,ymax1]=drectan(XP1,YP1)
[xmin2,xmax2,ymin2,ymax2]=drectan(XP2,YP2)

# % représentation graphique

dx=0.75;dy=0.75
xmin=min(xmin1,xmin2)-dx
xmax=max(xmax1,xmax2)+dx
ymin=min(ymin1,ymin2)-dy
ymax=max(ymax1,ymax2)+dy


# les courbes de Bézier

color1='r'
pchar1='P'
pcolor1='b'
ptrait1='--'



color2='g'
pchar2='Q'
pcolor2='b'
ptrait2='--'
title="Intersection de deux courbes : vue initiale'"





#  Première étape : test de l'intersection 

[test,xmi,xma,ymi,yma]=rbezier(XP1,YP1,XP2,YP2)

if (test==2) :


    colorRec = 'k'
    
    tbezierintersec(X1,Y1,color1,XP1,YP1,pchar1,pcolor1,ptrait1,title,X2,Y2,color2,XP2,YP2,pchar2,pcolor2,ptrait2,xmi,xma,ymi,yma,colorRec)

else :
    
    print('\n Pas d''intersection - Arrêt des calculs ')
    sys.exit("Error message")


# Deuxième étape : recherche du point d'intersection

color1='r'
pchar1='P'
pcolor1='b'
ptrait1='--'
color2='g'
pchar2='Q'
pcolor2='b'
ptrait2='--'


#iteraations

d1=0.0
f1=1.0
d2=0.0
f2=1.0
itera=0

[XQ1,YQ1,d1,f1,XQ2,YQ2,d2,f2,itera]=dbezier(XP1,YP1,d1,f1,XP2,YP2,d2,f2,itera)

titlei = 'Intersection de deux courbes : algorithme'

tbezierintersec1(X1,Y1,color1,XP1,YP1,pchar1,pcolor1,ptrait1,titlei,X2,Y2,color2,XP2,YP2,pchar2,pcolor2,ptrait2)

plt.show()


#Troisième étape : calcul du point d'intersection 
#comme point de concours des segments de droite

#A=zeros(2,2);b=zeros(2,1)

A = np.zeros((2,2))
b = np.zeros((2,1))

#np1=size(XQ1,2)
#np2=size(XQ2,2)

np1 = (np.shape(A)[0]) 
np2 = (np.shape(A)[0]) 

A[0,0]=XQ1[np1]-XQ1[0]
A[0,1]=-XQ2[np2]+XQ2[0]
b[0]=XQ2[0]-XQ1[0]

A[1,0]=YQ1[np1]-YQ1[0]
A[1,1]=-YQ2[np2]+YQ2[0]
b[1]=YQ2[0]-YQ1[0]

delta=A[0,0]*A[1,1]-A[1,0]*A[0,1]
delt1=b[0]*A[1,1]-b[1]*A[0,1]
delt2=A[0,0]*b[1]-A[1,0]*b[0]

c=[]

c.append(delt1/delta)
c.append(delt2/delta)
XI1=XQ1[0]+c[0]*(XQ1[np1]-XQ1[0])
YI1=YQ1[0]+c[0]*(YQ1[np1]-YQ1[0])
XI2=XQ2[0]+c[1]*(XQ2[np2]-XQ2[0])
YI2=YQ2[0]+c[1]*(YQ2[np2]-YQ2[0])

#print('\n Point d''intersection  %8.5f %8.5f %8.5f %8.5f ',XI1,YI1,XI2,YI2);

#Quatrième étape : vérification graphique locale

[test,xmi,xma,ymi,yma]=rbezier(XQ1,YQ1,XQ2,YQ2)
dx=(xma-xmi)*0.1
dy=(yma-ymi)*0.1
#axis([xmi-dx,xma+dx,ymi-dy,yma+dy])
T = np.arange(0.0,1.1,0.1, dtype=float)

[X1,Y1]=cbezier(T,XQ1,YQ1)
[X2,Y2]=cbezier(T,XQ2,YQ2)

color1='r'
pchar1='P'
pcolor1='b'
ptrait1='--'



color2='g'
pchar2='Q'
pcolor2='b'
ptrait2='--'



# Tracé du point d'intersection
#text(XI1,YI1,'X');text(XI2,YI2,'O')
titlel='Intersection de deux courbes : vue locale' 

tbezierintersec1(X2,Y2,color1,XQ2,YQ2,pchar1,pcolor1,ptrait1, titlel,X1,Y1,color2,XQ1,YQ1,pchar2,pcolor2,ptrait2)

plt.show()


#Cinquième étape : recherche  des paramètres associés

#print('\n Intersection : formule locale (doite) ')

tx1=(XI1-XQ1[0])/(XQ1[np1]-XQ1[0])
ty1=(YI1-YQ1[0])/(YQ1[np1]-YQ1[0])

[XXI1,YYI1]=casteljau(tx1,XQ1,YQ1)
[XXXI1,YYYI1]=casteljau(ty1,XQ1,YQ1)

#print('\n Le point sur la courbe 1 calculé avec x : %8.5f %8.5f %8.5f %8.5f %8.5f ',tx1,XI1,YI1,XXI1,YYI1)
#print('\n Le point sur la courbe 1 calculé avec y : %8.5f %8.5f %8.5f %8.5f %8.5f ',ty1,XI1,YI1,XXXI1,YYYI1)
tx2=(XI2-XQ2[0])/(XQ2[np2]-XQ2[0])
ty2=(YI2-YQ2[0])/(YQ2[np2]-YQ2[0])
[XXI2,YYI2]=casteljau(tx2,XQ2,YQ2)
[XXXI2,YYYI2]=casteljau(ty2,XQ2,YQ2)


#print('\n Le point sur la courbe 2 calculé avec x : %8.5f %8.5f %8.5f %8.5f %8.5f ',tx2,XI2,YI2,XXI2,YYI2);
#print('\n Le point sur la courbe 2 calculé avec y : %8.5f %8.5f %8.5f %8.5f %8.5f ',ty2,XI2,YI2,XXXI2,YYYI2);

#Sixième étape : vérification  graphique globale
#les courbes de Bézier

T = np.arange(0.0,1.05,0.05, dtype=float)
[X1,Y1]=cbezier(T,XP1,YP1)
[X2,Y2]=cbezier(T,XP2,YP2)

[test,xmi,xma,ymi,yma]=rbezier(XP1,YP1,XP2,YP2)


color1='r'
pchar1='P'
pcolor1='b'
ptrait1='--'

color1='g'
pchar1='Q'
pcolor1='b'
ptrait1='--'


xx=(XXI1+XXI2)*0.5
yy=(YYI1+YYI2)*0.5
dx=(xmax-xmin)/100
dy=(ymax-ymin)/100




titleg = 'Intersection de deux courbes : vue globale'

tbezierintersec(X1,Y1,color1,XP1,YP1,pchar1,pcolor1,ptrait1,titleg,X2,Y2,color2,XP2,YP2,pchar2,pcolor2,ptrait2,xx-dx,xx+dx,yy-dy,yy+dy,'r')


# Septième étape : recherche  des paramètres globaux

print('\n Intersection : formule globale (courbe) ')

T = np.arange(0.0,1.02,0.02, dtype=float)

[X1,Y1]=cbezier(T,XP1,YP1)
[X2,Y2]=cbezier(T,XP2,YP2)

[xmin1,xmax1,ymin1,ymax1]=drectan(XP1,YP1)
[xmin2,xmax2,ymin2,ymax2]=drectan(XP2,YP2)

seuilx=1.e-03
seuily=1.e-03
test1=0
test2=0

lenT= np.shape(T)[0] -1

for k in range(0, lenT) :

    if abs((X1[k]-XI1)*(XI1-X1[k])) < seuilx * (xmax1-xmin1) * (xmax1-xmin1):
        if abs((Y1[k]-YI1)*(YI1-Y1[k+1])) < seuily * (ymax1-ymin1) * (ymax1-ymin1):

            tx1=T[0,k+1]*(XI1-X1[k])/(X1[k+1]-X1[k])+T[0,k]*(X1[k+1]-XI1)/(X1[k+1]-X1[k])
            ty1=T[0,k+1]*(YI1-Y1[k])/(Y1[k+1]-Y1[k])+T[0,k]*(Y1[k+1]-YI1)/(Y1[k+1]-Y1[k])
            test1=1
            # fprintf('\n Le point sur la courbe 1 : %8.5f %8.5f %d ',tx1,ty1,k);

#s fprintf('\n Test sur la courbe 1 : %d ',test1);

for k in range(0, lenT) :
    if abs((X2[k]-XI2)*(XI2-X2[k+1])) < seuilx * (xmax2-xmin2) * (xmax2-xmin2) :
        if abs((Y2[k]-YI2)*(YI2-Y2[k+1])) < seuily * (ymax2-ymin2) * (ymax2-ymin2) :
            tx2=T[0,k+1]*(XI2-X2[k])/(X2[k+1]-X2[k])+T[0,k]*(X2[k+1]-XI2)/(X2[k+1]-X2[k])
            ty2=T[0,k+1]*(YI2-Y2[k])/(Y2[k+1]-Y2[k])+T[0,k]*(Y2[k+1]-YI2)/(Y2[k+1]-Y2[k])
            test2=1
            # fprintf('\n Le point sur la courbe 2 : %8.5f %8.5f %d ',tx2,ty2,k)

#printf('\n Test sur la courbe 2 : %d ',test2)

[XXI1x,YYI1x]=casteljau(tx1,XP1,YP1)
[XXI1y,YYI1y]=casteljau(ty1,XP1,YP1)

#fprintf('\n Le point sur la courbe 1 calculé avec x : %8.5f %8.5f %8.5f %8.5f %8.5f ',tx1,XI1,YI1,XXI1x,YYI1x);
#fprintf('\n Le point sur la courbe 1 calculé avec y : %8.5f %8.5f %8.5f %8.5f %8.5f ',ty1,XI1,YI1,XXI1y,YYI1y);

[XXI2x,YYI2x]=casteljau(tx2,XP2,YP2)
[XXI2y,YYI2y]=casteljau(ty2,XP2,YP2)


#fprintf('\n Le point sur la courbe 2 calculé avec x : %8.5f %8.5f %8.5f %8.5f %8.5f ',tx2,XI2,YI2,XXI2x,YYI2x);

#fprintf('\n Le point sur la courbe 2 calculé avec y : %8.5f %8.5f %8.5f %8.5f %8.5f ',ty2,XI2,YI2,XXI2y,YYI2y);




[test,xmi,xma,ymi,yma]=rbezier(XP1,YP1,XP2,YP2)

color1='r'
pchar1='P'
pcolor1='b'
ptrait1='--'


titre = 'Intersection de deux courbes : vue globale'

color2='g'
pchar2='Q'
pcolor2='b'
ptrait2='--'

tbezierintersec1(X1,Y1,color1,XP1,YP1,pchar1,pcolor1,ptrait1,titre,X2,Y2,color2,XP2,YP2,pchar2,pcolor2,ptrait2)

dx=(xmax-xmin)/100
dy=(ymax-ymin)/100

XCr = []
YCr =[]

XCr.append(XXI1x-dx)
XCr.append(XXI1x+dx)
YCr.append(YYI1x)
YCr.append(YYI1x)
plt.plot(XCr,YCr,'r')

XCr[0]=XXI1x
XCr[1]=XXI1x
YCr[0]=YYI1x-dy
YCr[1]=YYI1x+dy
plt.plot(XCr,YCr,'r')

XCr[0]=XXI2x-dx
XCr[1]=XXI2x+dx
YCr[0]=YYI2x-dy
YCr[1]=YYI2x+dy
plt.plot(XCr,YCr,'b')

XCr[0]=XXI2x-dx
XCr[1]=XXI2x+dx
YCr[0]=YYI2x+dy
YCr[1]=YYI2x-dy
plt.plot(XCr,YCr,'b')

plt.show()


#title('Intersection de deux courbes : vue globale'); 
