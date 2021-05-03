#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:05:24 2020

@author: alejandrobellonbranas
"""

import numpy as np
import random as rd


def funcion(x):
    f=(1-x**2)**1.5
    return f
def funcion2(x):
    g=(1-x**2)**3
    return g
N=100000
rd.seed(1)
a=0.
b=1.
V=b-a
x=0
integral=0
s1=0
s2=0
error=0
for i in range (N):
    x=rd.uniform(0,1)
    s1+=funcion(x)
    s2+=funcion2(x)
    
s1=s1/N
s2=s2/N
integral=V*s1
error=V*np.sqrt((s2-s1**2)/N)
print('N: %10d, Integral: %.10f, Error: %8.2e' %(N,integral,error))