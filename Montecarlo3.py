#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:34:25 2020

@author: alejandrobellonbranas
"""

import numpy as np
import random as rd

R=4
r=2
x=0
y=0
z=0
N=100000
Vtor=(2*np.pi**2)*R*r**2
suma=0
suma2=0
rd.seed(1)
def funcion(x,y,z,R,r):
    f=(np.sqrt(x**2+y**2)-R)**2+z**2 
    if f < r**2:
        l=1
    elif f==r**2:
        l=1
    else:
        l=0     
    return l
def funcion2(x,y,z,R,r):
    g=((np.sqrt(x**2+y**2)-R)**2+z**2)**2
    if g < r**4:
        m=1
    elif g==r**4:
        m=1
    else:
        m=0     
    return m
for i in range(N):
    x=rd.uniform(1,4)
    y=rd.uniform(-3,4)
    z=rd.uniform(-1,1)
    suma+=funcion(x,y,z,R,r)
    suma2+=funcion2(x,y,z,R,r)
suma=suma/N
suma2=suma2/N
integral=Vtor*suma
error=Vtor*np.sqrt((suma2-suma**2)/N)
print('N: %10d, Volumen: %.10f, Error: %8.2e' %(N,integral,error))
