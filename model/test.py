'''
Created on Sep 13, 2012

@author: colinwinslow
'''
import unittest
from Propositions import *


class Test(unittest.TestCase):


    def testConjunction(self):
        p = Proposition('p',True)
        q = Proposition('q',False)
        pandq = Conjunction(p,q)
        qandp = Conjunction(q,p)
        assert pandq == qandp

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()