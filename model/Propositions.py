'''
Created on Sep 12, 2012
This is the class heirarchy. Everything inherits from Proposition. Pay close
attention to __eq__ and __hash__ and such as these need to be equivalent in 
many cases.


@author: colinwinslow
'''
from LogicalOperators import *


def removeNones(inlist):
    output = []
    for i in inlist:
        if i!=None: output.append(i)
    return output

    

class Proposition(object):
    
    def __getitem__(self,key):
        if isinstance(self.symbol,str):
            return self
        else:
            return self.symbol[key]
       
    
    def __init__(self, symbol,action=None):
        self.action=action
        self.operands = (None)
        self.symbol = (symbol)

        self.operator = None
        self.successors = set()
        self.parent = None
        
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
            return self
        else:
            altz = removeNones([r.getSuccessorNodes(self) for r in rules])
            return altz
        
    def findMany(self,rules,):
        if type(self).__name__=="Proposition":
            return self

        
        
        
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
                
        
          
class Negation(Proposition):
    
    def __getitem__(self,key):
        return self.symbol
    
    def __new__(cls, prop, action = None):
        '''automatically replaces would-be double negatives with positivies'''
        if isinstance(prop, Negation):
            return prop.symbol
        else:
            return super(Negation, cls).__new__(cls)
    
    def __init__(self, parse):
        if type(parse).__name__=="ParseResults":
            self.arg = parse[0][1]
        else: self.arg = parse
        self.operands = (self.arg)
        self.symbol = self.arg
        self.operator = NegOp()
        self.action=None

    
    def __eq__(self, other):
        if type(self)!=type(other): return False
        else: return self.symbol == other.symbol
    
    def __ne__(self, other):
        if type(self)!=type(other): return True
        else: return self.symbol != other.symbol
    
    def __hash__(self):
        return hash((self.symbol, 'Negation'))
    
    def getSymbols(self):
        return (NegOp(), self.symbol)
    
    def __str__(self):
        return str(self.operator)+str(self.symbol)
        
            
        
    
class Conjunction(Proposition):
    
    def __init__(self, t):
        if type(t).__name__=="ParseResults":
            self.args = t[0][0::2]
        else: self.args = t
        if isinstance(self.args[0],str):
            self.a=Proposition(self.args[0])
        elif isinstance(self.args[0],Proposition):
            self.a = self.args[0]
        if isinstance(self.args[1],str): 
            self.b=Proposition(self.args[1])
        elif isinstance(self.args[1],Proposition): 
            self.b = self.args[1]
        self.b.parent = self
        self.a.parent = self
        self.operands = (self.a, self.b)
        self.symbol = (self.a, AndOp(), self.b)
        self.operator = self.symbol[1]
        self.action = None
    
    def __eq__(self, other):
        if type(self)==type(other):
            return frozenset(self.operands) == frozenset(other.operands)
        else: return False
    
    def __ne__(self, other):
        if type(self)!=type(other): return True
        else: return frozenset(self.operands) != frozenset(other.operands)
    
    def __hash__(self):
        return hash((frozenset(self.operands), 'Conjunction'))
    
    def __str__(self):
        return '('+str(self.a)+' '+str(self.operator)+' '+str(self.b)+')'
        
    
class Disjunction(Proposition):
    
    def __init__(self, t):
        if type(t).__name__=="ParseResults":
            self.args = t[0][0::2]
        else: self.args = t
        if isinstance(self.args[0],str): self.a=Proposition(self.args[0])
        elif isinstance(self.args[0],Proposition): self.a = self.args[0]
        if isinstance(self.args[1],str): self.b=Proposition(self.args[1])
        elif isinstance(self.args[1],Proposition): self.b = self.args[1]
        self.b.parent = self
        self.a.parent = self
        self.operands = (self.a, self.b)
        self.symbol = (self.a, OrOp(), self.b)
        self.operator = OrOp()
        
    def __eq__(self, other):
        if type(self)==type(other):
            return frozenset(self.operands) == frozenset(other.operands)
        else: return False
    
    def __ne__(self, other):
        if type(self)!=type(other): return True
        else: return frozenset(self.operands) != frozenset(other.operands)
    
    def __hash__(self):
        return hash((frozenset(self.operands), "Disjunction"))
    
    def __str__(self):
        return '('+str(self.a)+' '+str(self.operator)+' '+str(self.b)+')'
    
class Implication(Proposition):
    def __init__(self, parse, action=None):
        if type(parse).__name__=="ParseResults":
            self.args = parse[0][0::2]
        else: self.args = parse
        if isinstance(self.args[0],str): self.a=Proposition(self.args[0])
        elif isinstance(self.args[0],Proposition): self.a = self.args[0]
        if isinstance(self.args[1],str): self.b=Proposition(self.args[1])
        elif isinstance(self.args[1],Proposition): self.b = self.args[1]
        self.b.parent = self
        self.a.parent = self
        self.operands = (self.a, self.b)
        self.symbol = (self.a, ImpOp(), self.b)
        self.operator = self.symbol[1]
        self.action = action
        
    def __eq__(self, other):
        if type(self)==type(other):
            return self.a == other.a and self.b == other.b
        else: return False
    
    def __ne__(self, other):
        if type(self)!=type(other): return True
        else: return self.a != other.a and self.b != other.b
    
    def __hash__(self):
        return hash((self.a, self.b, "Implication"))
    
    def __str__(self):
        return '('+str(self.a)+' '+str(self.operator)+' '+str(self.b)+')'

#class Biimplication(Proposition):
#
#class ExclusiveOr(Proposition):
        
