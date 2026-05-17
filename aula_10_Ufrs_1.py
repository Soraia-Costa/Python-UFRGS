# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:31:05 2026

@author: Soraia Costa
"""

import numpy as np
import numpy_financial as npf

vi= -60000 #valor_inicial
rs=40000-10000 #receita

FC=np.array([vi,rs,rs,rs,rs,rs])#Fluxo_Caixa

inv=npf.npv(0.12,FC)

print("VPL=",inv)

#investimento viavel#