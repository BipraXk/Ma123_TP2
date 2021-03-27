# -*- coding: utf-8 -*-
"""
fonctions
"""
import math as m


def g0(x):
    return (1+m.sin(x))/2

def g1(x):
    return -(9-3*x)**(1/4)

def g2(x):
    return m.acos((x+2)/3)

def g3(x):
    return m.log(7/x)

def g41(x):
    return m.exp(x)-10
def g42(x):
    return m.log(10+x)

def g5(x):
    return m.atan((x+5)/2)

def g6(x):
    return m.log((x**2)+3)

def g7(x):
    return (7-4*m.log(x))/3

def g81(x):
    return ((2*(x**2)-(4*x)+17)**(1/4))
def g82(x):
    return -((2*(x**2)-(4*x)+17)**(1/4))

def g9(x):
    return m.log(7+2*m.sin(x))

def g10(x):
    return m.log(10/m.log(x**2+4))

