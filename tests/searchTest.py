'''
Created on Sep 30, 2012

@author: colinwinslow
'''
import unittest
from model.Propositions import *
from model.Equivalences import *
from model.Search import *





class Test(unittest.TestCase):


    def testNodeSuccessors(self): 
        
        results = testNode.getSuccessorNodes(rules)
        print results
        for r in results:
            print(str(r))
        results2 = testNode2.getSuccessorNodes(rules)
        print results2
        for r in results2:
            print(str(r))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()