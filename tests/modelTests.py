'''
Created on Sep 13, 2012

@author: colinwinslow
'''
import unittest
from model.Propositions import *
from model.Equivalences import *
from model.InputReader import logicParse


class Test(unittest.TestCase):
    
    def testParser(self):
        test = [
        "(q or (r | x)) | (s | t)",
        "((q implies r) -> not(s -> ~t))",
        "p&(q|((r->s)|~t))",
        "(q or r) | (s | t)",
        "(a | b) | (c | d)",
        "p & ~ q",
        "not not p",
        "not(p and q) or r",
        "q or not p and r",
        "q or not (p and r)",
        "p or q"
        ]
        correct = [
        "((q v (r v x)) v (s v t))",
        "((q -> r) -> ~(s -> ~t))",
        "(p & (q v ((r -> s) v ~t)))",
        "((q v r) v (s v t))",
        "((a v b) v (c v d))",
        "(p & ~q)",
        "~~p",
        "(~(p & q) v r)",
        "((q v ~p) & r)",
        "(q v ~(p & r))",
        "(p v q)"
        ]
        for i in range(len(test)):
            print logicParse(test[i])
            print correct[i]
            print str(logicParse(test[i]))==(correct[i])
            assert str(logicParse(test[i]))==(correct[i])
        
            
            
    def testAlts(self):
        rules = [Idempotence(),DoubleNegativity(),DeMorgansSplit(),DeMorgansJoin(),ImplicationLaw(),Contraposition(),Distributivity(),Absorption(),Associativity()]
        qor = logicParse("q | ((r -> s) | ~t)")
        porq = logicParse("p | q")
        
        
        print qor.findAlts(rules)
        
    
    
    def testPropositionEquivalence(self):
        p = Proposition('p')
        q = Proposition('q')
        p2 = Proposition('p')


        assert p == p2
        assert q != p2

        
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
        
        pandq = logicParse("p and q")
        qandr = logicParse("q and r")
        porq = logicParse("p or q")
        qorr = logicParse("p or r")
        
        assoc = Associativity()
        print logicParse("(p and q) and r)")
        print assoc.getSuccessorNodes(logicParse("(p and q) and r)"))
        assert assoc.getSuccessorNodes(logicParse("(p and q) and r)")) == logicParse("p and (q and r)")
        assert assoc.getSuccessorNodes(logicParse("(p or q) or r)")) == logicParse("p or (q or r)")

        
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
