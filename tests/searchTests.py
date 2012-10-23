'''
Created on Oct 22, 2012

@author: colinwinslow
'''
import unittest
from model.InputReader import logicParse
from model.Propositions import *
from model.Equivalences import *
from model.Search import Node, search

class Test(unittest.TestCase):

    def testNode(self):
        rules = [Idempotence(),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]
        
        start = logicParse('~((p -> q))')
        start.action = None
        start.cost = 0
        goal = logicParse('p & ~q')
        
        n = Node(start,None)
        s = n.successors(rules)
        assert s[0].state == logicParse('~(~p v q)')
        
        
        #should be solvable by implication law, demorgans, and double negation. 
        
    def testSearch(self):
        rules = [Idempotence(0.9),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(0.9),DeMorgans(),ImplicationLaw()]
        
        start = logicParse(' (~((p & p) -> q))')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('p & ~q')
        
        steps = search(start,goal,rules)
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."
            
    def testSearch2(self):
        rules = [Idempotence(),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]
        
        start = logicParse('~(b v c) & (~b & ~c)')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('~(b v c)')
        
        steps = search(start,goal,rules)
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."
        
    def testSearch3(self):
        print "\n\n******************"
        rules = [Idempotence(),Associativity(),Exportation(),Distributivity(2),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]
        
        start = logicParse('(~(b -> c) v d) & a')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('a & (b -> (~c v d))')
        
        steps = search(start,goal,rules,True)
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."
        
#    def testSearch4(self):
#        # this one needs truth constants to work. 
#        
#        rules = [Idempotence(),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]
#        
#        start = logicParse('~(p v (~p & q))')
#        start.action = "Beginning Premise"
#        start.cost = 0
#        goal = logicParse('~p & ~q')
#        
#        steps = search(start,goal,rules)
#        print"\nCost:\tRule:\t\t\t\tStatement:"
#        for s in steps:
#            print s.cost, "\t", s.action,"\t\t", s.state
#        print "\nTherefor, ",start," = ", goal,"."
        
#    def testNotEquivalentSearch(self):
#        # this one will get stuck forever until we figure out how to know when to quit
#        
#        rules = [DoubleNegation(1),DeMorgans(1),ImplicationLaw(1)]
#        
#        start = logicParse('p -> q')
#        start.action = "Beginning Premise"
#        start.cost = 0
#        goal = logicParse('q -> p')
#        
#        steps = search(start,goal,rules,True)
#        print"\nCost:\tRule:\t\t\t\tStatement:"
#        for s in steps:
#            print s.cost, "\t", s.action,"\t\t", s.state
#        print "\nTherefor, ",start," = ", goal,"."
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()