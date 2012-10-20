'''
Created on Oct 15, 2012

@author: colinwinslow
'''
import unittest
from statement import Statement
from pyparseplayground import logicParse
from Propositions import *


class Test(unittest.TestCase):


    def testStatementIndexing(self):
        s = logicParse("q & (~(r -> s) | t)")
        print s
    
    def testReIndex(self):
        s = logicParse("q & (~(r -> s) | t)")
        print s.d.keys()
        s.reIndex(0, 4)
        print s.d.keys()
        s.reIndex(4,0)
        print s.d.keys()
        
    def testNegationEquality(self):
        notp = logicParse("!p")
        othernotp = logicParse("~p")
        
    def testEquality(self):
        print "A"
        
        
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()