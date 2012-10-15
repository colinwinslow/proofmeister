'''
Created on Sep 12, 2012
This is the class heirarchy. Everything inherits from Proposition. Pay close
attention to __eq__ and __hash__ and such as these need to be equivalent in 
many cases.


@author: colinwinslow
'''
from copy import deepcopy,copy

from LogicalOperators import *


def removeNones(inlist):
    output = []
    for i in inlist:
        if i!=None: output.append(i)
    return output

    

class Proposition(object):
        
    
    def __getitem__(self,key):
        return self.parseSearch(key)
    
    def parseSearch(self,key):
        if key == self.index: return self
        else: return None
                
       
    def __init__(self, symbol, parent=None):
        self.index = None
        self.note = None
        self.action=None
        self.symbol = (symbol)
        self.operator = None
        self.successors = set()
        self.parent = parent
        self.treeList = []
    
    def indexTree(self, i=None, treeList = None ):
        if treeList == None: treeList = self.treeList
        if i==None:
            self.index=0
            treeList.append(0)
        else: 
            self.index=i
            treeList.append(i)
            
            
    def getAllIndices(self):
        self.treeList.sort()
        return self.treeList
        
        
    def __eq__(self, other):
        if type(self)!=type(other): return False
        else: return self.symbol==other.symbol
    
    def __ne__(self, other):
        if type(self)!=type(other): return True
        return self.symbol!=other.symbol
    
    def __hash__(self):
        return hash(self.symbol)

    def getLaTeX(self):
        return self.symbol
    
    def getMathML(self):
        return self.symbol
    
    def findAlts(self,rules):
        if type(self).__name__=="Proposition":
            return []
        else:
            altz = removeNones([r.getSuccessorNodes(self) for r in rules])
            return altz
        
    def findMany(self,rules,):
        completeSuccessors = []
        allIndices = self.getAllIndices()
        for i in allIndices:
            alts = self[i].findAlts(rules)
            for j in alts:
                if j!=None: completeSuccessors.append(self.insert(i,j))
        return completeSuccessors
                
    def insert(self,index,newProp):
        '''puts a new proposition in the parse tree at the specified index and connects parent/child relationships appropriately'''
        newParse =  deepcopy(self)
        newParse.note="this is the copy"
        newProp.index = index
        newProp.indexTree
        newParse.action = newProp.action
        
        
        oldProp = self[index]
        if newParse[(index-1)//2] != None: 
            newProp.parent = newParse[(index-1)//2]
            newParse[(index-1)//2].substitute(newProp,oldProp)
            return newParse
        else: return newProp
        
        

            
        
        
        
    def getSymbols(self):
        if self.operator==None:
            return self.symbol
        else:
            output = []
            for i in self.symbol:
                output.append(i.getSymbols())
            return tuple(output)
    def __str__(self):
        return str(self.symbol)
    
class BinaryOperation(Proposition):
    
    
    
    def __init__(self, t, parent = None):
        super(BinaryOperation,self).__init__(t)
        
        if type(t).__name__=="ParseResults": self.args = t[0][0::2]
        else: self.args = t
        if isinstance(self.args[0],str):
            self.a=Proposition(self.args[0],self)
        elif isinstance(self.args[0],Proposition):
            self.a = self.args[0]
            self.a.parent = self

        if isinstance(self.args[1],str):
            self.b=Proposition(self.args[1],self)
        elif isinstance(self.args[1],Proposition):
            self.b = self.args[1]
            self.b.parent = self
            
        self.action = None
        
        
    def indexTree(self, i=None, treeList = None):
        #must be called on the root node
        if treeList == None: treeList = self.treeList
        if i==None:
            self.index=0
            treeList.append(0)
        else:
            self.index=i
            treeList.append(i)
        self.a.indexTree(2*self.index + 1, treeList)
        self.b.indexTree(2*self.index + 2, treeList)
    
    def parseSearch(self,key):
        if key == self.index: return self
        elif key > self.index:
            left = self.a.parseSearch(key)
            if left != None: return left
            return self.b.parseSearch(key)
    
    def substitute(self,newProp,oldProp):
        if self.a==oldProp:
            self.a=newProp
            self.a.parent = self
        if self.b==oldProp:
            self.b=newProp
            self.b.parent = self
    
    def __eq__(self, other):
        if type(self)==type(other) and self.commutative:
            return frozenset([self.a,self.b]) == frozenset([other.a,other.b])
        elif type(self)==type(other) and not self.commutative:
            return self.a == other.a and self.b == other.b
        else: return False
    
    def __ne__(self, other):
        if type(self)!=type(other): return True
        else:
            if self.commutative: return frozenset([self.a,self.b]) != frozenset([other.a,other.b])
            else: return self.a != other.a or self.b != other.b
        
    def __str__(self):
        return '('+str(self.a)+' '+str(self.operator)+' '+str(self.b)+')'
                    
        
        
                
        
          
class Negation(Proposition):
    
    def substitute(self,newProp,oldProp):
        self.arg =newProp
        self.arg.parent = self
    
#    def __deepcopy__(self, memo):
#        return self
#    def __copy__(self, memo):
#        return self
    
    def parseSearch(self,key):
        if key == self.index: return self
        else: return self.arg.parseSearch(key)
    
    def __getitem__(self,key):
        return self.symbol
    
#    def __new__(cls, prop ):
#        '''automatically replaces would-be double negatives with positivies'''
#        if isinstance(prop, Negation):
#            return prop.symbol
#        else:
#            return super(Negation, cls).__new__(cls)
    
    def __init__(self, parse):
        super(Negation,self).__init__(parse)
        if type(parse).__name__=="ParseResults":
            self.arg = parse[0][1]
        else: self.arg = parse
        if isinstance(self.arg,str):
            self.arg=Proposition(self.arg)
        self.arg.parent = self
        self.symbol = self.arg
        self.operator = NegOp()
        self.action=None
        
    def indexTree(self, i=None, treeList = None):
    #must be called on the root node
        if treeList == None: treeList = self.treeList
        if i==None: 
            treeList.append(0)
            self.index=0
        else: 
            treeList.append(i)
            self.index=i
        self.arg.indexTree(2*self.index+1, treeList)
        

    
    def __eq__(self, other):
        if type(self)!=type(other): return False
        else: return self.arg == other.arg
    
    def __ne__(self, other):
        if type(self)!=type(other): return True
        else: return self.arg != other.arg
    
    def __hash__(self):
        return hash((self.arg, 'Negation'))
    
    def getSymbols(self):
        return (NegOp(), self.arg)
    
    def __str__(self):
        return str(self.operator)+str(self.arg)
        
            
        
    
class Conjunction(BinaryOperation):
    
    def __init__(self, t):
        super(Conjunction,self).__init__(t)
        self.symbol = (self.a, AndOp(), self.b)
        self.operator = self.symbol[1]
        self.commutative=True
#        self.action = None
    
 
    def __hash__(self):
        return hash((frozenset([self.a,self.b]), 'Conjunction'))
    
        
    
class Disjunction(BinaryOperation):
    
    def __init__(self, t):
        super(Disjunction,self).__init__(t)
        self.symbol = (self.a, OrOp(), self.b)
        self.operator = OrOp()
        self.commutative=True
        
    def __hash__(self):
        return hash((frozenset([self.a,self.b]), "Disjunction"))
    
    
    
class Implication(BinaryOperation):
    def __init__(self, t, action=None):
        
        super(Implication,self).__init__(t)
        self.symbol = (self.a, ImpOp(), self.b)
        self.operator = self.symbol[1]
        self.action = action
        self.commutative=False
        
    
    def __hash__(self):
        return hash((self.a, self.b, "Implication"))
    


#class Biimplication(Proposition):
#
#class ExclusiveOr(Proposition):
        
