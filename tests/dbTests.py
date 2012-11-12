'''
Created on Nov 11, 2012

@author: colinwinslow
'''
import unittest
from model.findDerivation import findDerivation
from model.InputReader import logicParse
from model.Equivalences import *


class Test(unittest.TestCase):


    def testParseHash(self):
        s = '(a implies q) & (q -> a)'
        g = '(~a & ~q) v (q & a)'
        startParse = logicParse(s)
        goalParse = logicParse(g, startParse.propMap)
        
        assert hash((startParse,goalParse))==-1223974109378650937
        
    def testFD(self):
        rules = [Negation(),Commutativity(),Identity(),Domination(),Idempotence(),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]
        s = '(p implies q) & (q -> p)'
        g = '(~p & ~q) v (q & p)'
        steps = findDerivation(s,g,rules)
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testParseHash']
    unittest.main()