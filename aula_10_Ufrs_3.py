# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:57:14 2026

@author: Soraia Costa
"""

import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as gr

FC = np.zeros(6)
FC[0]=-60000

for i in range(5):
    FC[i+1]=40000 -10000
    
tir =npf.irr(FC)

print("TIR=",str(round(100*tir,2)),"%")

eixox=np.linspace(0,0.5,200)

vpl=np.array([npf.npv(i,FC) for i in eixox])
gr.plot(eixox,vpl,'--k',linewidth=2)
gr.plot(tir,0, 'k*',markersize=15)
gr.xlabel('Juros -i')
gr.title('TIR - taxa interna de retorno',fontsize=16)
gr.grid()