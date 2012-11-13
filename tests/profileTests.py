'''
Created on Nov 12, 2012

@author: colinwinslow
'''
import cProfile
from model.findDerivation import findDerivation
from model.Equivalences import *
import pstats



def main():
    profile = cProfile.run('searchProfile()')
    
    profile.sort()
    
def searchProfile():
    rules = [Negation(),Commutativity(),Identity(),Domination(),Idempotence(),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]
    s = '(p implies q) & (q -> p)'
    g = '(~p & ~q) v (q & p)'
    for i in range(20):
        steps = findDerivation(s,g,rules,cache=False)
    
    
if __name__ == '__main__': main()