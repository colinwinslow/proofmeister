'''
Created on Oct 29, 2012

@author: colinwinslow
'''
import unittest
from model.InputReader import logicParse
from model.Search import search
from model.Equivalences import *

rules = [Negation(0.5),Identity(0.5),Domination(0.5),Idempotence(0.5),Associativity(),Exportation(),Distributivity(),Absorption(0.5),DoubleNegation(),DeMorgans(),ImplicationLaw(multiplier=2)]

class Test(unittest.TestCase):


    def testSimHash(self):
        s =         logicParse('(p -> q) & q')
        equiv =     logicParse('(a -> b) & b')
        notEquiv =  logicParse('(a -> b) & a')
        notEquiv2 = logicParse('(a -> b) v a')
        assert s.simHash() == equiv.simHash()
        assert s.simHash() != notEquiv.simHash()
        assert s.simHash() != notEquiv2.simHash()
        
    def testEquivalentDerivations(self):
        start = logicParse(' (~((p & p) -> q))')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('p & ~q',start.propMap)
        steps = search(start,goal,rules)
        
        start = logicParse(' (~((a & a) -> b))')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('a & ~b',start.propMap)
        steps2 = search(start,goal,rules)
        
        assert  hash(steps) == hash(steps2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()