'''
Created on Sep 13, 2012

@author: colinwinslow
'''
from Propositions import *


p = Proposition('p',True)
q = Proposition('q',False)

pimpliesq = Implication(p,q)
nested = Implication(pimpliesq,pimpliesq)

print nested.getSymbols()
