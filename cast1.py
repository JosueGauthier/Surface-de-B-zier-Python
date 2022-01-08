# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:03:32 2021

@author: etien
"""

"""Enveloppe convexe d'une courbe de Bézier
   Construction des points de contrôle 
   Première partie t dans [0.,0.5]
   
   Données : t  valeur du paramètre 
             XP, YP coordonnées des points de contrôle

   Résultats : XPP, YPP coordonnées des points de contrôle
"""

import numpy as np

def cast1(t,XP,YP):
    
    m = (np.shape(XP)[0]) - 1
    
    XPP = XP.copy()
    YPP = YP.copy()
    xx = XP.copy()
    yy = YP.copy()
    
    XPP[0] = xx[0]
    YPP[0] = yy[0]
    
    for kk in range(0,m+1):
        
        xxx = xx.copy()
        yyy = yy.copy()
        
        for k in range(kk,m):
            
            xx[k+1]=(1-t)*xxx[k]+t*xxx[k+1]
            yy[k+1]=(1-t)*yyy[k]+t*yyy[k+1]
            
        XPP[kk] = xx[kk]
        YPP[kk] = yy[kk]
    
    return (XPP,YPP)