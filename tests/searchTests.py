'''
Created on Oct 22, 2012

@author: colinwinslow
'''
import unittest
from model.InputReader import logicParse, propMap
from model.Propositions import *
from model.Equivalences import *
from model.Search import Node, search


rules = [Negation(0.5),Identity(0.5),Domination(0.5),Idempotence(0.5),Associativity(),Exportation(),Distributivity(),Absorption(0.5),DoubleNegation(),DeMorgans(),ImplicationLaw(multiplier=2)]
#rules = [Negation(),Identity(),Domination(),Idempotence(),Associativity(),Exportation(),Distributivity(),Absorption(),DoubleNegation(),DeMorgans(),ImplicationLaw()]



class Test(unittest.TestCase):
    
#    def testPropMapFreakOut(self):
#        start = logicParse('(((a & b) v (c & d)) -> ((e & g) v (h & i))) -> j')
#        print start
    
    def testPropMap(self):
        pm = propMap()
        assert pm.convert('p') == 'a'
        assert pm.convert('q') == 'b'
        assert pm.convert('p')
        
    
    def testNode(self):
        
        start = logicParse('~((p -> q))')
        start.action = None
        start.cost = 0
        goal = logicParse('p & ~q')
        
        n = Node(start,None)
        s = n.successors(rules)
        assert s[0].state == logicParse('~(~p v q)')
        
        
        #should be solvable by implication law, demorgans, and double negation. 
        
    def testSearch(self):
        
        start = logicParse(' (~((p & p) -> q))')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('p & ~q',start.propMap)
        
        steps = search(start,goal,rules)
        print "\nDemonstrate that", start, "is logically equivalent to", goal
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."
#            
    def testSearch2(self):
        
        start = logicParse('~(b v c) & (~b & ~c)')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('~(b v c)',start.propMap)
        
        steps = search(start,goal,rules)
        print "\nDemonstrate that", start, "is logically equivalent to", goal
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."
        
    def testSearch3(self):
        print "\n\n******************"
        
        start = logicParse('(~(b -> c) v d) & a')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('a & (b -> (~c v d))',start.propMap)
        
        steps = search(start,goal,rules)
        print "\nDemonstrate that", start, "is logically equivalent to", goal
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."
        
    def testSearch4(self):
        # this one needs truth constants to work. 
        
        
        start = logicParse('~(p v (~p & q))')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('~p & ~q',start.propMap)
        goal.action = "Goal"
        
        steps = search(start,goal,rules)
        print "\nDemonstrate that", start, "is logically equivalent to", goal
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."
    
    def testSearch5(self):
        print "\n\n******************"
        
        start = logicParse('(p & F) v (q v T)')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('T',start.propMap)
        
        steps = search(start,goal,rules)
        print "\nDemonstrate that", start, "is logically equivalent to", goal
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."
        
    def testSearchHW1a(self):
        
        
        print "\n\nHW1a***************"
        #(p -> q) & (q -> p) start 
        #(~p v q) & (~q v p) implication
        #((~p v q) & ~q)&((~p v q) & p) distribution
        # ((~p & ~q) v (q & ~q)) v ((p & ~p) v (q&p)) distribution
        # (~p & ~q) v (q&p) ???
        start = logicParse('(p -> q) & (q -> p)')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('((~p & ~q) v (q & ~q)) v ((p & ~p) v (q&p))',start.propMap)
        
        steps = search(start,goal,rules)
        print "\nDemonstrate that", start, "is logically equivalent to", goal
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."
        
    def testSearchHW1b(self):
        
        
        print "\n\nHW1b***************"
        #(p -> q) & (q -> p) start 
        #(~p v q) & (~q v p) implication
        #((~p v q) & ~q)&((~p v q) & p) distribution
        # ((~p & ~q) v (q & ~q)) v ((p & ~p) v (q&p)) distribution
        # (~p & ~q) v (q&p) ???
        start = logicParse('((~p & ~q) v (q & ~q)) v ((p & ~p) v (q&p))')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('(~p & ~q) v (q&p)',start.propMap)
        
        steps = search(start,goal,rules)
        print "\nDemonstrate that", start, "is logically equivalent to", goal
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."
        
    def testSearch3H(self):
        print "\n\n******************"
        
        start = logicParse('~(p -> q)')
        start.action = "Beginning Premise"
        start.cost = 0
        goal = logicParse('p & ~q',start.propMap)
        
        steps = search(start,goal,rules)
        print "\nDemonstrate that", start, "is logically equivalent to", goal
        print"\nCost:\tRule:\t\t\t\tStatement:"
        for s in steps:
            print s.cost, "\t", s.action,"\t\t", s.state
        print "\nTherefor, ",start," = ", goal,"."
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