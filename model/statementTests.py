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
        print s.getLeft(0)
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()