'''
Created on Oct 15, 2012

@author: colinwinslow
'''
from BProps import BinaryOperation, UnaryOperation, Proposition
class Statement(object):
    '''
    represents a parse tree as a dictionary
    '''


    def __init__(self, inDict):
        self.d = inDict
        
    def __getitem__(self,key):
        return self.childTree(key)
        
    def getParent(self,i):
        if i==0: return None
        return self.d.get((i-1)/2)
    
    def getLeft(self,i):
        return self.d.get(i*2+1)
    
    def getRight(self,i):
        return self.d.get(i*2+2)
    
    def __str__(self):
        return self.getSymbol(0)
        
    def getSymbol(self,i):
        if isinstance(self.d.get(i),BinaryOperation): 
            return "(" + self.getSymbol(i*2+1) + " " + self.d.get(i).getOperator() + " " + self.getSymbol(i*2+2) + ")"
        elif isinstance(self.d.get(i),UnaryOperation): 
            return "~" + self.getSymbol(i*2+1)
        elif isinstance(self.d.get(i),Proposition): 
            return str(self.d.get(i))
        
    def reIndex(self,i,newIndex):
        if newIndex < i: print "I wasn't designed to reindex downward!"
        self.d.get(i).reIndex(i,newIndex,self.d)
        
    def childTree(self,i):
        newDict = dict()
        self.d.get(i).childTree(i,0,self.d,newDict)
        return Statement(newDict)
    
    def __hash__(self):
        return self.d.get(0).hash(0,self.d)
    
    def __eq__(self,other):
        return hash(self)==hash(other)
    
    def __ne__(self,other):
        return hash(self)!=hash(other)
        
        
        
        
        
        