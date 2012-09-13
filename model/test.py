'''
Created on Sep 13, 2012

@author: colinwinslow
'''
from Propositions import *



p = Proposition('p',True)
q = Proposition('q',False)

pimpliesq = Implication(p,q)
qimpliesp = Implication(q,p)
bimp = Conjunction(pimpliesq,qimpliesp)

print bimp.getSymbols()
