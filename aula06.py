# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:30:14 2026

@author: Soraia Costa
"""

import numpy as np

n=int(input('Numero de termos ='))

x=np.zeros(n)
y=np.zeros(n)

soma=0

for i in range (n):
    x[i]=float(input('x='))
    y[i]=10*x[i]
    soma=soma+x[i]+y[i]
    
print('Soma das coordenadas de x e y =',soma)

print('Soma dos elementos de x=',x.sum())

print('Média  dos elementos de x=',x.mean())

print('Desvio padrao de x=',x.std())

print('Valor minimo de x=', x.min())

print('Valor máximo de x=',x.max())

print('Posição do menor valor de x=',x.argmin())

print('Posição do maior valor de x=',x.argmax())