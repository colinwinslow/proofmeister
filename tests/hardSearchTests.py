'''
Created on Oct 24, 2012

@author: colinwinslow
'''
import unittest
from model.InputReader import logicParse
from model.Propositions import *
from model.Equivalences import *
from model.Search import Node, search



rules = [Negation(),Commutativity(),Identity(),Domination(),Idempotence(),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]
rules = [Negation(),Identity(),Distributivity(),ImplicationLaw()]
rules = [Negation(),Identity(),Domination(),Idempotence(),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]


class Test(unittest.TestCase):


    def testSearchHW1(self):
        
        
        print "\n\nHW1a***************"
        #(p -> q) & (q -> p) start 
        #(~p v q) & (~q v p) implication
        #((~p v q) & ~q)&((~p v q) & p) distribution
        # ((~p & ~q) v (q & ~q)) v ((p & ~p) v (q&p)) distribution
        # (~p & ~q) v (q&p) ???
        start = logicParse('(p -> q) & (q -> p)')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('(~p & ~q) v (q & p)')
        
        steps = search(start,goal,rules)
        print "\nDemonstrate that", start, "is logically equivalent to", goal
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()