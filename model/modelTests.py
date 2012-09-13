'''
Created on Sep 13, 2012

@author: colinwinslow
'''
import unittest
from Propositions import *
from Equivalences import *


class Test(unittest.TestCase):
    
    def testPropositionEquivalence(self):
        p = Proposition('p')
        q = Proposition('q')
        p2 = Proposition('p')
        pT = Proposition('p',True)
        pF = Proposition('p',False)
        qT = Proposition('q',True)
        qF = Proposition('q',False)
        assert p == pT
        assert p == pF
        assert pT == pF
        assert p == p2
        assert q != p2
        assert qT != pT


    def testConjunctionEquivalence(self):
        p = Proposition('p',True)
        q = Proposition('q',False)
        pandq = Conjunction(p,q)
        qandp = Conjunction(q,p)
        assert pandq == qandp
        
    def testConjunctionNonEquivalence(self):
        p = Proposition('p',True)
        q = Proposition('q',False)
        r = Proposition('r',True)
        pandq = Conjunction(p,q)
        randq = Conjunction(r,q)
        assert pandq != randq
        
    def testIdempotence(self):
        p = Proposition('p')
        q = Proposition('q')
        p2 = Proposition('p')
        q2 = Proposition('q')
        
        ifpthenq = Implication(p,q)
        ifp2thenq2 = Implication(p2,q2)
        
        pandp = Conjunction(ifpthenq, ifp2thenq2)
        
        
        idem = Idempotence()
        assert idem.getSucessors(pandp)[0].getPlainText() == ('p','implies','q')
    
    def testAssociativityConjunction(self):
        p = Proposition('p')
        q = Proposition('q')
        r = Proposition('r')
        
        pandq = Conjunction(p,q)
        pandqANDr = Conjunction(pandq,r)
        
        assoc = Associativity()
        print assoc.getSucessors(pandqANDr)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()