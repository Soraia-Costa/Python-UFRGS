# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:47:11 2026

@author: Soraia Costa
"""

import numpy as np

import matplotlib.pyplot as gr

from math import cos,exp

n=int(input('Número de pontos a serem impressos='))

x=np.zeros(n)
y=np.zeros(n)
z=np.zeros(n)

for i in range (n):
    x[i]=i*0.1
    y[i]=exp(-0.1*x[i])*cos(x[i])
    z[i]=cos(x[i])+1
    
'''gr.plot(x,y,'+g',x,z,'-r')
gr.title('Dois graficos')

gr.plot(x,y,'-b',x,z,'-r')
gr.title('Dois graficos')'''

gr.plot(x,y,'+g',x,z,'or')
gr.title('Dois graficos')
