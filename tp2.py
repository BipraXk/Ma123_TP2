# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:23:51 2021

@author: crist
"""

import math as m 
import fonctions as f 

def g(x):
    x=(m.sin(x)+1)/2
    return x

def PointFixe(g,x0,epsilon,Nitermax):
    n=0
    xold=x0
    xnew=g(xold)
    dif=xold-xnew
    while abs(dif) > epsilon and n < Nitermax :
        n+=1
        xnew=g(xold)
        dif=xold-xnew
        xold=xnew
        print(n,xnew)
    return xnew

    if abs(dif)<= epsilon:
        print("test reussi")
    else :
        print("test raté")
        return xold,n



print(PointFixe(f.g82, 0, 1e-10, 100))