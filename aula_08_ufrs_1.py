# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:02:01 2026

@author: Soraia Costa
"""
import pandas as pd

info=pd.DataFrame({'Produto':['Tijolo','Tinta','Solvente','Telhas','Cimento'],'Preço':[3.3,4.5,12,27,45],'Qntde':[10,12,23,34,4],'Custo':[0.5,1.2,1.4,12,11]})

print(info)

info['Produto']

info['Preço']

info.Produto

info.Preço

info.columns

info.sort_values(by='Produto')
info.sort_values(by='Preço')

info['Custo']>1.2

info[info['Custo']>1.2]

# %%
info[ (info['Custo']>1.2) & (info['Qntde']>10)]
