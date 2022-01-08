# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:47:31 2021

@author: vdeha
"""
from drectan import drectan

def rbezier(XP1,YP1,XP2,YP2):

    (xmin1,xmax1,ymin1,ymax1)=drectan(XP1,YP1)
    (xmin2,xmax2,ymin2,ymax2)=drectan(XP2,YP2)

    xmi=max(xmin1,xmin2)
    xma=min(xmax1,xmax2)
    ymi=max(ymin1,ymin2)
    yma=min(ymax1,ymax2)

    inter=0

    seuil=1*10**(-6)
    if (xma-xmi > seuil) :
        inter=inter+1
    if (yma-ymi > seuil) :
        inter=inter+1
    return(inter,xmi,xma,ymi,yma)
    
    