# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:55:40 2026

@author: Soraia Costa
"""

import matplotlib.pyplot as gr #biblioteca de grafico
import datetime as dt  #biblioteca de data
import pandas_datareader.data as web #auxilio na transfomaçãode dataframe

inicio=dt.datetime(1970,1,1)
fim=dt.datetime(2026,2,1)

df1= web.DataReader('DGS10','fred',inicio,fim) #dataframe

df1['med_mov']=df1['DGS10'].rolling(window=300,min_periods=0).mean() #vai criar uma coluna nova comas taxas do periodo de 300 dias 

ax=gr.subplot(111)
ax.plot(df1.index,df1['DGS10'],color='black',alpha=0.5)
ax.plot(df1.index,df1['med_mov'],color='blue')
ax.set_title('Tesouro EUA -venc 10 anos')
