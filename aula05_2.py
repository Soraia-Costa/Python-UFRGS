# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:10:20 2026

@author: Soraia Costa
"""


import numpy as np

import matplotlib.pyplot as gr

from math import cos,exp

import statistics as st

from scipy.stats import norm

x=[4,2,1,0,4,10,9,8,11,14]

gr.hist(x,bins=5,density= True)

media=st.mean(x)
desvio=st.stdev(x)

xmin,xmax= gr.xlim()

eixox=np.linspace(xmin,xmax,100)
eixoy=norm.pdf(eixox,media,desvio)

gr.plot(eixox,eixoy)
