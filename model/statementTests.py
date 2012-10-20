'''
Created on Oct 15, 2012

@author: colinwinslow
'''
import unittest
from statement import Statement
from pyparseplayground import logicParse
from Propositions import *


class Test(unittest.TestCase):


    
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
        
        
        
    def testTreeIndexing(self):
        
        s = logicParse("q & (~(r -> s) | t)")
        assert s[0] == s
        assert str(s[1]) == "q"
        assert str(s[2])== "(~(r -> s) v t)"
        assert str(s[11]) == "(r -> s)"
    
    def testPropositionEquivalence(self):
        p = logicParse('p')
        q = logicParse('q')
        p2 = logicParse('p')


        assert p == p2
        assert q != p2
        
    def testNegation(self):

        notp = logicParse("~p")
        pt = str(notp)
        assert str(notp) == "~p"
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()