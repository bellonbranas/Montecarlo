#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:54:08 2020

@author: alejandrobellonbranas
"""

import numpy as np
import random as rd

R=1.5
Vcub=(2*R)**3
x=0
y=0
z=0
N=100000

suma=0
suma2=0
rd.seed(1)
def funcion(x,y,z,R):
    f=x**2+y**2+z**2
    if f < R**2:
        l=1
    elif f==R**2:
        l=1
    else:
        l=0     
    return l
def funcion2(x,y,z,R):
    f=(x**2+y**2+z**2)**2
    if f < R**4:
        l=1
    elif f==R**4:
        l=1
    else:
        l=0     
    return l
for i in range(N):
    x=rd.uniform(-R,R)
    y=rd.uniform(-R,R)
    z=rd.uniform(-R,R)
    suma+=funcion(x,y,z,R)
    suma2+=funcion2(x,y,z,R)
suma=suma/N
suma2=suma2/N
integral=Vcub*suma
error=Vcub*np.sqrt((suma2-suma**2)/N)
print('N: %10d, Volumen: %.10f, Error: %8.2e' %(N,integral,error))