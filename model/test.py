'''
Created on Sep 13, 2012

@author: colinwinslow
'''
from Propositions import *



p = Proposition('p',True)
q = Proposition('q',False)

aandb = Conjunction(p,q)
banda = Conjunction(q,p)

print "b&a == a&b", banda == aandb

pimpliesq = Implication(p,q)
qimpliesp = Implication(q,p)
pimpliesqagain = Implication(p,q)

bimp = Conjunction(pimpliesq,qimpliesp)

print bimp.getSymbols()
print pimpliesq == pimpliesqagain