'''
Created on Oct 15, 2012

@author: colinwinslow
'''
import unittest
from statement import Statement
from pyparseplayground import logicParse
from Propositions import *


class Test(unittest.TestCase):


    def testStatementIndexing(self):
        s = logicParse("q & (~(r -> s) | t)")
        print s
        subs = s.childTree(2)
        print subs
    
    def testReIndex(self):
        s = logicParse("q & (~(r -> s) | t)")
        assert set(s.d.keys())==set([0,1,2,5,6,11,23,24])
        s.reIndex(0, 1)
        assert set(s.d.keys())==set([1,4,9,3,19,39,40,10])
        
    def testNegationEquality(self):
        notp = logicParse("!p")
        othernotp = logicParse("~p")
        
        
    def testEquality(self):
        ab = logicParse("a and b")
        ba = logicParse("b and a")
        assert ab==ba
        aib = logicParse("a implies b")
        bia = logicParse("b implies a")
        assert aib != bia
        
        
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()