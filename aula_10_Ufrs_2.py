# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:50:32 2026

@author: Soraia Costa
"""

import numpy as np
import numpy_financial as npf

FC = np.zeros(3)
FC[0]=-1000

for i in range(2):
    FC[i+1]=650
    
tir=npf.irr(FC)

print("TIR+",str(round(100*tir,2)),"%")