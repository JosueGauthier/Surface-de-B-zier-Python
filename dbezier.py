"""%%   Recherche de l'intersection de deux courbes de Bézier
%%   
%%   Données : T  ensemble des valeurs du paramètre 
%%             XP1, YP1 coordonnées des points de contrôle
%%             XP2, YP2 coordonnées des points de contrôle
%%             d1,f1  paramètres des points de contrôle (début-fin)
%%             d2,f2  paramètres des points de contrôle (début-fin)
%%             itera   nombre d'appel de la procédure
%%             
%%
%%   Résultats :  
%%
%%             XQ1, YQ1 nouvelles coordonnées des points de contrôle
%%             XQ2, YQ2 nouvelles coordonnées des points de contrôle
%%             td1,tf1  nouveaux paramètres des points de contrôle  
%%             td2,tf2  nouveaux paramètres des points de contrôle  
%%             itera    itera + 1 
%%    
"""

from rbezier import rbezier
from trectan import trectan
from convexe import convexe
from cast1 import cast1
from cast2 import cast2

import matplotlib.pyplot as plt


def dbezier(XP1,YP1,d1,f1,XP2,YP2,d2,f2,itera):
    
    [test,xi,xa,yi,ya]=rbezier(XP1,YP1,XP2,YP2)
    XQ1=XP1
    YQ1=YP1
    XQ2=XP2
    YQ2=YP2
    td1=d1
    tf1=f1
    td2=d2
    tf2=f2

    # Non convergence en itérations ?
    # compteur d'itérations
    
    itera=itera+1
    itmax=20

    if ( itera > itmax ) : 

        print('Arrêt de la récursivité : non convergence ')
        title_recus = "non convergence"
        trectan(xi,xa,yi,ya,'b', title_recus)
        return(XQ1,YQ1,td1,tf1,XQ2,YQ2,td2,tf2,itera)
        

    #Convergence en convexité ?

    h1=convexe(XP1,YP1)
    h2=convexe(XP2,YP2)
    h=max(h1,h2)
    seuilc=5*(10**(-0.5))

    if ( h < seuilc ): 
        print('Convergence en convexité h = %f \n',h)
        print('Itération %d ',itera)
        return(XQ1,YQ1,td1,tf1,XQ2,YQ2,td2,tf2,itera)


    #  Convergence en abscisse ?

    seuil=1*(10**(-4))
    if ( abs(xa-xi) < seuil ):

        print('\n Convergence en x')
        print('\n Itération %d ',itera)
        return(XQ1,YQ1,td1,tf1,XQ2,YQ2,td2,tf2,itera)

    #Convergence en ordonnée ?

    if ( abs(ya-yi) < seuil ):

        print('\n Convergence en y')
        print('\n Itération %d ',itera)
        return(XQ1,YQ1,td1,tf1,XQ2,YQ2,td2,tf2,itera)

    #%% Subdivision des courbes

    char=str(itera)
    
    char='RI: '+ char

    #le paramètre t
    
    tm1=(d1+f1)*0.5
    [XP1a,YP1a]=cast1(tm1,XP1,YP1)
    [XP1b,YP1b]=cast2(tm1,XP1,YP1)

    tm2=(d2+f2)*0.5

    [XP2a,YP2a]=cast1(tm2,XP2,YP2)
    [XP2b,YP2b]=cast2(tm2,XP2,YP2)

    #les tests d'intersection

    [test1,xmi1,xma1,ymi1,yma1]=rbezier(XP1a,YP1a,XP2a,YP2a)
    [test2,xmi2,xma2,ymi2,yma2]=rbezier(XP1b,YP1b,XP2a,YP2a)
    [test3,xmi3,xma3,ymi3,yma3]=rbezier(XP1a,YP1a,XP2b,YP2b)
    [test4,xmi4,xma4,ymi4,yma4]=rbezier(XP1b,YP1b,XP2b,YP2b)
    
    if (test1==2) : 

        trectan(xmi1,xma1,ymi1,yma1,'k','Intersection 1 - 1')
        char1= char + '-1'
        plt.text(xma1*1.05,ymi1*1.05,char1)
        [XQ1,YQ1,td1,tf1,XQ2,YQ2,td2,tf2,itera]=dbezier(XP1a,YP1a,d1,tm1,XP2a,YP2a,d2,tm2,itera)

    
    elif (test2==2):

        trectan(xmi2,xma2,ymi2,yma2,'k', 'Intersection 2 - 1')
        char2=char + '-2'
        plt.text(xma2*1.05,ymi2*1.05,char2)
        [XQ1,YQ1,td1,tf1,XQ2,YQ2,td2,tf2,itera]=dbezier(XP1b,YP1b,tm1,f1,XP2a,YP2a,d2,tm2,itera)


    elif (test3==2) :

        trectan(xmi3,xma3,ymi3,yma3,'k', 'Intersection 1 - 2' )
        char3= char +'-3'
        plt.text(xma3*1.05,ymi3*1.05,char3)
        [XQ1,YQ1,td1,tf1,XQ2,YQ2,td2,tf2,itera]=dbezier(XP1a,YP1a,d1,tm1,XP2b,YP2b,tm2,f2,itera)

    elif (test4==2): 

      trectan(xmi4,xma4,ymi4,yma4,'k','Intersection 2 - 2')
      char4= char + '-4'
      plt.text(xma4*1.05,ymi4*1.05,char4)
      [XQ1,YQ1,td1,tf1,XQ2,YQ2,td2,tf2,itera]=dbezier(XP1b,YP1b,tm1,f1,XP2b,YP2b,tm2,f2,itera)

    
    
    return(XQ1,YQ1,td1,tf1,XQ2,YQ2,td2,tf2,itera)
   



    






    



    



    




    





    


