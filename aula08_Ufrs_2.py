# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:51:46 2026

@author: Soraia Costa
"""

import pandas as pd

dados=pd.read_excel('XYZW3.xlsx',sheet_name='Planilha2']
                    
df = pd.DataFrame(dados)

print(df)

print (df.head(n=10))

print(df.FECHAMENTO.head(n=10))

df['FECHAMENTO']>29.5 

df[df['FECHAMENTO']>29.5]# para saber qual linhas sao verdadeiras, neste ex nao vai acusar resposta pois o valor é alto#

df[df['FECHAMENTO']>29.0]# neste exemplo apresenta  resultados 

df2=df[ (df['FECHAMENTO']<29) & (df['ABERTURA']>29)]

df.sort_values(by='ABERTURA',ascending=False)
