# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:18:39 2026

@author: Soraia Costa
"""

import matplotlib.pyplot as gr
import pandas as pd
import time

df = pd.read_excel('XYZW3.xlsx','Planilha2')

n=len(df.DATA)

grafdin=gr.subplot(111)

for i in range(n):
    grafdin.plot(df[0:i].DATA.df[0:i].ABERTURA,'-k')
    gr.gcf().autofmt_xdate()
    gr.pause(0.1)
    
