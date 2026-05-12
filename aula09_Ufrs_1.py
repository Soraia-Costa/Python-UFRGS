# -*- coding: utf-8 -*-
"""
Created on Tue May 12 18:56:23 2026

@author: Soraia Costa
"""

import matplotlib.pyplot as gr
import random
import time
import numpy as np

n=20

x=np.zeros(n)
y=np.zeros(n)

for i in range (n):
    x[i]=i
    y[i]= random.gauss(0,1)
    
grafdin=gr.subplot(111)

for i in range(n):
    grafdin.plot(x[0:i],y[0:i],'-k')
    gr.pause(0.5)