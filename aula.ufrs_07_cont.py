# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

import random
import matplotlib.pyplot as gr

rand = []

for i in range(100):
    x = random.randint(-10,10)
    rand.append(x)
    
for i in range(100):
    x = random.random()
    rand.append(x)

gr.plot(rand)

rand1=[]
rand2=[]

for i in range(1000):
    x=random.uniform(-1,1)
    rand1.append(x)
    x=random.gauss(0,1)
    rand2.append(x)
    
gr.subplot(211)
gr.plot(rand1,'-b')
gr.plot(rand2,'-r')
gr.subplot(212)
gr.hist(rand1,bins=10)


    