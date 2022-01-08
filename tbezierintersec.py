"""
%%
%%  Tracé d'une courbe de Bézier et de ses points de contrôle
%%
%%   Données  : X, Y coordonnées des points de l'échantillonage
%%              color couleur de la courbe tracée
%%              XP, YP coordonnées des points de contrôle
%%              pchar caractère associé aux points de contrôle
%%              pcolor couleur de la courbe de contrôle
%%              ptrait type de trait de la courbe de contrôle
%%
%%   Résultats : Tracé graphique de la courbe et des points
%%    

"""
import numpy as np
import matplotlib.pyplot as plt 

def tbezierintersec(X1,Y1,color1,XP1,YP1,pchar1,pcolor1,ptrait1,title,X2,Y2,color2,XP2,YP2,pchar2,pcolor2,ptrait2,xmi,xma,ymi,yma,colorRec) :

    ligne1= pcolor1 + ptrait1 #concatene couleur et forme de trait pour obtenir un champ 'b--' eg
    ligne2= pcolor2 + ptrait2

    plt.plot(X1,Y1,color1)
    plt.plot(XP1,YP1,ligne1)
    plt.plot(X2,Y2,color2)
    plt.plot(XP2,YP2,ligne2)


    a1 = np.shape(XP1) # a taille en liste
    nb1 = a1[0] # nb a en int coresspond au nombre de points de controles.

    a2 = np.shape(XP2) # a taille en liste
    nb2 = a2[0] # nb a en int coresspond au nombre de points de controles.

    for k in range(0,nb1) : 

        kk = k
        charrIndice = str(kk) # trnasforme en str l'indice 1 eg '1'
        numP = pchar1 + charrIndice #forme un indice type 'P1'

        epsx = 0.1
        epsy = 0.2

        if (k==0) : 
            epsx =0.0
            epsy =-0.2

        if (k==nb1-1) :
            epsx =0.1
            epsy =0.0

        plt.text(XP1[k]+epsx, YP1[k]+epsy, numP) 


    for k in range(0,nb2) : 

        kk = k
        charrIndice = str(kk) # trnasforme en str l'indice 1 eg '1'
        numP = pchar2 + charrIndice #forme un indice type 'P1'

        epsx = 0.1
        epsy = 0.2

        if (k==0) : 
            epsx =0.0
            epsy =-0.2

        if (k==nb1-1) :
            epsx =0.1
            epsy =0.0

        plt.text(XP2[k]+epsx, YP2[k]+epsy, numP)              

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
    plt.plot(xx,yy,colorRec)

    plt.title(title)


    plt.title(title)

    plt.show()
