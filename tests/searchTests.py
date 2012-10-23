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
        print"Cost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
            
#    def testSearch2(self):
#        rules = [Idempotence(),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]
#        
#        start = logicParse('~(b v c) & (~b & ~c)')
#        start.action = "starting point"
#        start.cost = 0
#        goal = logicParse('(~b v c)')
#        
#        steps = search(start,goal,rules)
#        print steps
#        for s in steps:
#            print s, "\t", s.action
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()