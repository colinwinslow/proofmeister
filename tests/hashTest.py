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


    def testcohash(self):
        s1 =  logicParse('p v (q&r)')
        s2 = logicParse('(r&q) v p', s1.propMap)
        
        assert s1.cohash()== s2.cohash()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()