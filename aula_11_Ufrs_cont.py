# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:25:34 2026

@author: Soraia Costa
"""

import yfinance as yf
import matplotlib.pyplot as gr
import numpy as np
from scipy import stats
import math as m

ticker =['DIVO11.SA','KFOF11.SA']#ativo do mercado financeiro,indice brasileiro que paga dividendos da bolsa de valores

start_date='2024-01-01'
end_date='2025-12-15'

res=[]

for i in range(len(ticker)):
    res.append(yf.download(ticker[i],start=start_date,end=end_date))

lin=len(res[0].Close)
mat=np.zeros((lin,2)) #matriz

for i in range(lin):
    for j in range(2):
        mat[i,j] = res[j].iloc[i,j]
print(mat)

eixox=np.arange(lin)
axl=gr.subplot(211)

axl.plot(eixox,mat[:,0],'--k',label='DIVO11')
axl.set_title("Comparação entre DIVO11 e o KFOF11 em 2024 -2025")

ax2=axl.twinx() #Twinx - é um compremento ao outro grafico, compartilha o mesmo eixo
ax2.plot(eixox,mat[:,1],'-b',label='KFOF11')
ax2.grid()

res[0]['Retorno']=res[0].Close.pct_change(1)#o 1 significa uma unidade de tempo,no exemplo a avaliação diaria, se fosse ex anual eo intervalo fosse mensal seria 12
res[1]['Retorno']=res[1].Close.pct_change(1) #esse é para o KFOF11 -O anterior é do DIVO11

ret1=res[0]['Retorno']
ret2=res[1]['Retorno']


eixoR=np.arange(len(ret1))

ax1=gr.subplot(212)
ax1.plot(eixoR,ret1,'--ok',label='DIVO11')
ax1.set_title('Retornos')
ax2=ax1.twinx()
ax2.plot(eixoR,ret2,'-b',linewidth=1,label='KFOF11')
gr.grid()


mi1=ret1.mean()
mi2=ret2.mean()
sigma1=ret1.std() #desvio padrão
sigma2=ret2.std()
correl, pval = stats.pearsonr(ret1[1:], ret2[1:])

pa=0.6
pb=1-pa

risco_cart=m.sqrt(pa**2*sigma1**2+pb**2*sigma2**2+2*pa*pb*correl*sigma1*sigma2)

print('Média retorno(DIVO11)=',mi1)
print('Média retorno(KFOF11)=',mi2)
print('Desvio padrão(DIVO11)=',sigma1)
print('Desvio padrão(KFOF11)=',sigma2)
print('Coeficiênte de correlação dos ativos =',correl)
print('Risco da carteira',risco_cart)



p=np.arange(0,1,0.01)
rc=np.zeros(len(p))
eixoCart=np.zeros(len(p))

i=0
for x in p:
    y=1-x
    rc[i]=m.sqrt(x**2*sigma1**2+y**2*sigma2**2+2*x*y*correl*sigma1*sigma2)
    eixoCart[i]=x
    i=i+1

gr.figure()
gr.plot(rc,eixoCart,'-k')
gr.grid()
gr.xlabel('Risco',fontsize=14)
gr.ylabel('Retorno da Carteira',fontsize=14)
gr.title('Fronteira eficiete -( DIVO11, KFOF11)',fontsize=14)
















