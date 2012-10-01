'''
Created on Sep 13, 2012

@author: colinwinslow
'''
import unittest
from model.Propositions import *
from model.Equivalences import *


class Test(unittest.TestCase):
    def testAlts(self):
        rules = [Idempotence(),DoubleNegativity(),DeMorgansSplit(),DeMorgansJoin(),ImplicationLaw(),Contraposition(),Distributivity(),Absorption(),Associativity()]
        p = Proposition('p')
        q = Proposition('q')
        r = Proposition('r')
        s = Proposition('s')
        t = Proposition('t')
        notT = Negation(t)
        rimps = Implication(r,s)
        rimpsornotT = Disjunction(rimps,notT)
        qor = Disjunction(q,rimpsornotT)
        
        print "*",[str(a) for a in qor.findAlts(rules)]
    
    
    
    def testPropositionEquivalence(self):
        p = Proposition('p')
        q = Proposition('q')
        p2 = Proposition('p')
        pT = Proposition('p', True)
        pF = Proposition('p', False)
        qT = Proposition('q', True)
        qF = Proposition('q', False)
        assert p == pT
        assert p == pF
        assert pT == pF
        assert p == p2
        assert q != p2
        assert qT != pT
        
    def testNegation(self):
        p = Proposition('p')
        notp = Negation(p)
        pt = str(notp)
        assert str(notp) == "~p"
        


    def testConjunctionEquivalence(self):
        p = Proposition('p', True)
        q = Proposition('q', False)
        pandq = Conjunction(p, q)
        qandp = Conjunction(q, p)
        assert pandq == qandp
        
    def testDisjunctionEquivalence(self):
        p = Proposition('p', True)
        q = Proposition('q', False)
        p2 = Proposition('p', False)
        q2 = Proposition('q', True)
        porq = Disjunction(p, q)
        qorp = Disjunction(p2, q2)
        assert porq == qorp
        
    def testConjunctionNonEquivalence(self):
        p = Proposition('p', True)
        q = Proposition('q', False)
        r = Proposition('r', True)
        pandq = Conjunction(p, q)
        randq = Conjunction(r, q)
        assert pandq != randq
        
    def testIdempotence(self):
        p = Proposition('p')
        q = Proposition('q')
        p2 = Proposition('p')
        q2 = Proposition('q')
        
        ifpthenq = Implication(p, q)
        ifp2thenq2 = Implication(p2, q2)
        
        pandp = Conjunction(ifpthenq, ifp2thenq2)
        
        
        idem = Idempotence()
        assert str(idem.getSuccessorNodes(pandp)) == '(p -> q)'
        
#    def testDoubleNegative(self):
#        p = Proposition('p')
#        notp = Negation(p)
#        doubleNeg = Negation(notp)
#        doubleNegativity = DoubleNegativity()
#        assert doubleNegativity.getSuccessorNodes(doubleNeg) == p
        
    def testDeMorganConjunctionSplit(self):
        p = Proposition('p')
        q = Proposition('q')
        notp = Negation(p)
        notq = Negation(q)
        pandq = Conjunction(p, q)
        negatedConj = Negation(pandq)
        dms = DeMorgansSplit()
        assert dms.getSuccessorNodes(negatedConj) == Disjunction(notp, notq)
        
    def testDeMorganDisjunctionSplit(self):
        p = Proposition('p')
        q = Proposition('q')
        notp = Negation(p)
        notq = Negation(q)
        porq = Disjunction(p, q)
        negatedDisj = Negation(porq)
        dms = DeMorgansSplit()
        assert dms.getSuccessorNodes(negatedDisj) == Conjunction(notp, notq)
        
    def testDeMorgansConjunctionJoin(self):
        p = Proposition('p')
        q = Proposition('q')
        notp = Negation(p)
        notq = Negation(q)
        pandq = Conjunction(p, q)
        negatedConj = Negation(pandq)
        dms = DeMorgansSplit()
        dmj = DeMorgansJoin()
        assert dmj.getSuccessorNodes(dms.getSuccessorNodes(negatedConj)) == negatedConj
        
    def testImplicationLaw(self):
        p = Proposition('p')
        q = Proposition('q')
        pimpliesq = Implication(p, q)
        
        imp = ImplicationLaw()
        assert imp.getSuccessorNodes(pimpliesq) == Disjunction(Negation(p), q)
        
    def testContraposition(self):
        p = Proposition('p')
        q = Proposition('q')
        notp = Negation(p)
        notq = Negation(q)
        pimpliesq = Implication(p, q)
        
        contra = Contraposition()
        
        assert contra.getSuccessorNodes(pimpliesq) == Implication(notp, notq)
        
    def testAssociativity(self):
        p = Proposition('p')
        q = Proposition('q')
        r = Proposition('r')
        
        pandq = Conjunction(p, q)
        qandr = Conjunction(q, r)
        porq = Disjunction(p, q)
        qorr = Disjunction(q, r)
        
        assoc = Associativity()
        assert assoc.getSuccessorNodes(Conjunction(pandq, r)) == Conjunction(p, qandr)
        assert assoc.getSuccessorNodes(Disjunction(porq, r)) == Disjunction(p, qorr)

        
    def testSucessorMechanism(self):
        successorFuncs = [Idempotence(), DoubleNegativity(), DeMorgansSplit(),
                          DeMorgansJoin(), ImplicationLaw(), Contraposition(),
                          Associativity()]
        p = Proposition('p')
        q = Proposition('q')
        r = Proposition('r')
        s = Proposition('s')
        complex = Disjunction(p, Implication(q, Conjunction(r, s)))
        
        
#        for f in successorFuncs:
#            print str(f.getSuccessorNodes(complex))
            
        LookinGood = True
        
        assert LookinGood
            
            
         
         
    def testAssociativityConjunction(self):
        p = Proposition('p')
        q = Proposition('q')
        r = Proposition('r')
        
        pandq = Conjunction(p, q)
        pandqANDr = Conjunction(pandq, r)
        
        assoc = Associativity()
        assert assoc.getSuccessorNodes(pandqANDr) == Conjunction(p, Conjunction(q, r))
        
    def testDistributive(self):
        p = Proposition('p')
        q = Proposition('q')
        r = Proposition('r')
        pandqORr = Conjunction(p, Disjunction(q, r))
        porqANDr = Disjunction(p, Conjunction(q, r))
        expandedOr = Conjunction(Disjunction(p, q), Disjunction(p, r))
        expandedAnd = Disjunction(Conjunction(p, q), Conjunction(p, r))
        distLaw = Distributivity()
        assert distLaw.getSuccessorNodes(pandqORr) == expandedAnd
        assert distLaw.getSuccessorNodes(porqANDr) == expandedOr
        assert distLaw.getSuccessorNodes(expandedAnd) == pandqORr
        assert distLaw.getSuccessorNodes(expandedOr) == porqANDr
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
