'''
Created on Oct 15, 2012

@author: colinwinslow
'''
import unittest
from model.InputReader import logicParse
from model.Propositions import *
from model.Equivalences import *


class Test(unittest.TestCase):
    
    def testCommute(self):
        com = Commutativity()
        s = logicParse('p v (q v r)')
        assert com.getSuccessors(s, 2) == logicParse('p v (r v q)',s.propMap)
        suc = com.getSuccessors(s, 0)
        assert suc == logicParse('(q v r) v p', s.propMap)
    
    def testNegLaw(self):

        neg = Negation()
        s = logicParse('p & ~p') #contradiction
        t = logicParse('p v ~p') #tautology
        
        assert neg.getSuccessors(s, 0) == logicParse('False')
        assert neg.getSuccessors(t, 0) == logicParse('True')
    
    def testDomination(self):
        dom = Domination()
        
        s = logicParse('a -> (p & F)')
        t = logicParse('a -> (F & T)')
        u = logicParse('True v p')
        v = logicParse('T v F')
        
        
        assert dom.getSuccessors(s, 2) == logicParse('a -> False')
        assert dom.getSuccessors(t, 2) == logicParse('a -> False')
        assert dom.getSuccessors(u, 0) == logicParse('True')
        assert dom.getSuccessors(v, 0) == logicParse('True')
    
    def testIdentity(self):
        ident = Identity()
        
        s = logicParse('a -> (p v F)')
        t = logicParse('a -> (F v T)')
        u = logicParse('True & p')
        v = logicParse('p & T')
        
        assert ident.getSuccessors(s, 2) == logicParse('a -> p')
        assert ident.getSuccessors(t, 2) == logicParse('a -> True')
        assert ident.getSuccessors(u, 0) == logicParse('p')
        assert ident.getSuccessors(v, 0) == logicParse('p')
        


    
    def testReIndex(self):
        s = logicParse("q & (~(r -> s) | t)")
        assert set(s.d.keys()) == set([0, 1, 2, 5, 6, 11, 23, 24])
        s.reIndex(0, 1)
        assert set(s.d.keys()) == set([1, 4, 9, 3, 19, 39, 40, 10])
        
    def testNegationEquality(self):
        notp = logicParse("!p")
        othernotp = logicParse("~p")
        assert notp == othernotp
        
        
    def testEquality(self):
        ab = logicParse("a and b")
        ba = logicParse("a and b", ab.propMap)
        assert ab == ba
        aib = logicParse("a implies b")
        bia = logicParse("b implies a", aib.propMap)
        assert aib != bia
        c1 = logicParse("(a & b) -> c")
        c2 = logicParse("(b & a) -> c",c1.propMap)
        assert c1 != c2
        
    def testGraft(self):
        graftee = logicParse("a implies (b implies c)")
        graft = logicParse("~b or c",graftee.propMap)
        target = logicParse("a -> (~b or c)",graftee.propMap)
        new = graftee.graft(2, graft)
        assert new == target
        
    def testNegatedChildTree(self):
        s = logicParse("(a & b) -> ~(a & b)")
        n1 = s.negatedChildTree(1)
        n2 = s.negatedChildTree(2)
        assert n1 == s.childTree(2)
        assert n2 == s.childTree(1)
        
        
        
        
    def testTreeIndexing(self):
        
        s = logicParse("q & (~(r -> s) | t)")
        assert s[0] == s
        assert str(s[1]) == "q"
        assert str(s[2]) == "(~(r -> s) v t)"
        assert str(s[11]) == "(r -> s)"
    
    def testPropositionEquivalence(self):
        p = logicParse('p')
        q = logicParse('q',p.propMap)
        p2 = logicParse('p',q.propMap)


        assert p == p2
        assert q != p2
        
    def testNegation(self):

        notp = logicParse("~p")
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
        u = logicParse('(~p v q) & (~q v p)')
        dist = Distributivity()
        ssucs = logicParse('(p & q) v (p & r)',s.propMap)
        tsucs = logicParse('(p v q) & (p v r)',t.propMap)
        assert dist.getSuccessors(s, 0) == ssucs
        assert dist.getSuccessors(t, 0) == tsucs
        m = logicParse("(p & (q or r)) & m")
        mtarget = logicParse("((p & q) v (p & r)) & m")
        assert dist.getSuccessors(m, 1) == mtarget
        
    def testAbsorption(self):
        answer = logicParse("p")
        s = logicParse('p & (p v q)')
        t = logicParse('(p v q) & p')
        u = logicParse('p v (p & q)')
        v = logicParse('(p & q) v p')
        absorb = Absorption()
        assert absorb.getSuccessors(s, 0) == answer
        assert absorb.getSuccessors(t, 0) == answer
        assert absorb.getSuccessors(u, 0) == answer
        assert absorb.getSuccessors(v, 0) == answer
        
    def testDN(self):
        s = logicParse('~~p')
        answer = logicParse("p")
        dn = DoubleNegation()
        assert dn.getSuccessors(s, 0)==answer
        
    def testDeMorgan(self):
        s = logicParse('(p&q)&m')
        t = logicParse('(~pv~q)&m')
        dm= DeMorgans()
        assert dm.getSuccessors(s, 1) == logicParse('(~(~p v ~q) & m)')
        assert dm.getSuccessors(t, 1) == logicParse('(~(p & q) & m)')
        
    def testImplicationLaw(self):
        il = ImplicationLaw()
        s = logicParse('p -> q')
        t = logicParse('p v ~q', s.propMap)
        u = logicParse("a&(~p v ~q)", t.propMap)
        assert il.getSuccessors(s, 0) == logicParse('(~p v q)',u.propMap)
        assert il.getSuccessors(t, 0) == logicParse('q -> p',u.propMap)
        
    def testExportation(self):
        s = logicParse("(a -> b) -> c")
        t = logicParse("a -> (b -> c)")
        ex = Exportation()
        assert ex.getSuccessors(s, 0) == t
        assert ex.getSuccessors(t, 0) == s
        

        
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
