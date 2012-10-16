'''
Created on Oct 15, 2012

@author: colinwinslow
'''
from Propositions import BinaryOperation
class Statement(object):
    '''
    represents a parse tree as a dictionary
    '''


    def __init__(self, inDict):
        self.d = inDict
        
    def __getitem__(self,key):
        return self.d.get(key)
        
    def getParent(self,i):
        if i==0: return None
        return self.d.get((i-1)/2)
    
    def getLeft(self,i):
        return self.d.get(i*2+1)
    
    def getRight(self,i):
        if isinstance(self.d.get(i),BinaryOperation): return self.d.get(i*2+2)
        else: return self.d.get(i*2+1) #negations always stored in left child
        
        
        
        