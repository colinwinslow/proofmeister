'''
Created on Oct 15, 2012

@author: colinwinslow
'''
import unittest
from model.statement import Statement
from model.InputReader import logicParse
from model.Propositions import *
from model.Equivalences import *


class Test(unittest.TestCase):


    
    def testReIndex(self):
        s = logicParse("q & (~(r -> s) | t)")
        assert set(s.d.keys()) == set([0, 1, 2, 5, 6, 11, 23, 24])
        s.reIndex(0, 1)
        assert set(s.d.keys()) == set([1, 4, 9, 3, 19, 39, 40, 10])
        
    def testNegationEquality(self):
        notp = logicParse("!p")
        othernotp = logicParse("~p")
        
        
    def testEquality(self):
        ab = logicParse("a and b")
        ba = logicParse("b and a")
        assert ab == ba
        aib = logicParse("a implies b")
        bia = logicParse("b implies a")
        assert aib != bia
        c1 = logicParse("(a & b) -> c")
        c2 = logicParse("(b & a) -> c")
        assert c1 == c2
        
    def testGraft(self):
        graftee = logicParse("a implies (b implies c)")
        graft = logicParse("~b or c")
        target = logicParse("a -> (~b or c)")
        new = graftee.graft(2, graft)
        assert new == target
        
        
        
        
    def testTreeIndexing(self):
        
        s = logicParse("q & (~(r -> s) | t)")
        assert s[0] == s
        assert str(s[1]) == "q"
        assert str(s[2]) == "(~(r -> s) v t)"
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
        
    def testIdempotence(self):
        s = logicParse("a & (b or b)")
        idem = Idempotence()
        assert logicParse("a & b") == idem.getSuccessors(s, 2)
        assert idem.getSuccessors(s, 1) == None
        assert idem.getSuccessors(s, 0) == None
        
    def testAssoc(self):
        # single successor cases
        s = logicParse("(a & b) & c")
        t = logicParse("a or (b or c)")
        assoc = Associativity()
        assert assoc.getSuccessors(s, 0) == logicParse("a & (b &c)")
        assert assoc.getSuccessors(t, 0) == logicParse("(a or b) or c)")
        #multi successor
        u = logicParse("(a or b) or (c or d)")
        us1 = logicParse("a or (b or (c or d))")
        us2 = logicParse("((a or b) or c) or d")
        assert assoc.getSuccessors(u, 0) == [us1, us2]
        
    def testDist(self):
        
        s = logicParse("p & (q or r)")
        t = logicParse("(q & r) v p")
        dist = Distributivity()
        assert dist.getSuccessors(s, 0) == logicParse('(p & q) v (p & r)')
        assert dist.getSuccessors(t, 0) == logicParse('(p v q) & (p v r)')
        
        
        
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
