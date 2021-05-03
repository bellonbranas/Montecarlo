#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:54:08 2020

@author: alejandrobellonbranas
"""
import numpy as np
import random as rd

def dm(x,y):
    
    if ((x-b+R)**2+y**2)>R**2:
        z=1.
        
    else:
        z=0.
    
    return z

def xdm(x,y):
    
    if ((x-b+R)**2+y**2)>R**2:
        z=x
    else:
        z=0.
    
    return z

def ydm(x,y):
    
    if ((x-b+R)**2+y**2)>R**2:
        z=y
    else:
        z=0.
    
    return z
R=2.
a=6. 
b=8. 
n=1000000
suma=0.
sumacuad=0.
sumax=0.
sumaxcuad=0.
sumay=0.
sumaycuad=0.
rd.seed(1)

for j in range(n):
      
    xj=rd.uniform(0.,b) 
    yj=rd.uniform(0.,a)
    dm1=dm(xj,yj)
    suma+=dm1
    dmcuad=(dm(xj,yj))**2
    sumacuad+=dmcuad
    xdm1=xdm(xj,yj)
    sumax+=xdm1
    xdmcuad=(xdm(xj,yj))**2
    sumaxcuad+=xdmcuad
    ydm1=ydm(xj,yj)
    sumay+=ydm1
    ydmcuad=(ydm(xj,yj))**2
    sumaycuad+=ydmcuad
    
fcuad=(sumacuad/n)  
f=(suma/n)
f2=(suma/n)**2     
error=(a*b)*(np.sqrt((fcuad-f2)/n))
Idm=(a*b)*f
    
fxcuad=(sumaxcuad/n)  
fx=(sumax/n)
fx2=(sumax/n)**2        
xerror=(a*b)*(np.sqrt((fxcuad-fx2)/n))
Ixdm=(a*b)*fx
    
fycuad=(sumaycuad/n)  
fy=(sumay/n)
fy2=(sumay/n)**2        
yerror=(a*b)*(np.sqrt((fycuad-fy2)/n))
Iydm=(a*b)*fy
      
xG=Ixdm/Idm
errorxG=np.sqrt((xerror/Idm)**2+((Ixdm*error)/(Idm**2))**2)
yG=Iydm/Idm
erroryG=np.sqrt((yerror/Idm)**2+((Iydm*error)/(Idm**2))**2)
    
print('n:',n)
print('xG:',xG)
print('Error xG: %8.2e'%(errorxG))
print('yG:',yG)
print('ErroryG: %8.2e'%(erroryG))