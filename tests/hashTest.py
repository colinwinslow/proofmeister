'''
Created on Oct 29, 2012

@author: colinwinslow
'''
import unittest
from model.InputReader import logicParse
from model.Search import search
from model.Equivalences import *

rules = [Negation(),Commutativity(),Identity(),Domination(),Idempotence(),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]


class Test(unittest.TestCase):

    def testcohash(self):
        s1 =  logicParse('p v (q&r)')
        s2 = logicParse('(r&q) v p', s1.propMap)
        
        assert s1.cohash()== s2.cohash()
        
    def testVariability(self):
        print "commute"
        for i in range(10):
            self.searchHW1noCache()
#        print "no commute"
#        for i in range(100):
#            self.searchHW1noCacheNoCommute()
            
    def searchHW1noCache(self):
        start = logicParse('(p -> q) & (q -> p)')
        goal = logicParse('(p & q)v(~p & ~q)',start.propMap)
        
        steps = search(start,goal,rules)
        
    def searchHW1noCacheNoCommute(self):
        start = logicParse('(p -> q) & (q -> p)')
        goal = logicParse('(~p & ~q) v (q &p)',start.propMap)
        rules = [Negation(),Identity(),Domination(),Idempotence(),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]
        steps = search(start,goal,rules)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()