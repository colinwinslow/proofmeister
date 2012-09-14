'''
Created on Sep 12, 2012
This is the class heirarchy. Everything inherits from Proposition. Pay close
attention to __eq__ and __hash__ and such as these need to be equivalent in 
many cases.

Values are allow propositions to be assigned truth values, but this isn't 
in use for the time being.

@author: colinwinslow
'''
from LogicalOperators import *

class Proposition(object):
    
    
    def __init__(self,symbol,value=None):
        self.symbol = (symbol)
        self.value = value
        
    def __eq__(self,other):
        return self.symbol==other.symbol
    
    def __ne__(self,other):
        return self.symbol!=other.symbol
    
    def __hash__(self):
        return hash(self.symbol)

    def getLaTeX(self):
        return self.symbol
    
    def getMathML(self):
        return self.symbol
    
    def getPlainText(self):
        return self.getSymbols()
    
    def getValue(self):
        return self.value
    
    def getSymbols(self):
        if type(self.symbol) is str:
            return self.symbol
        else:
            output = []
            for i in self.symbol:
                output.append(i.getSymbols())
            return tuple(output)
                
        
          
class Negation(Proposition):
    
    def __new__(cls,prop):
        '''automatically replaces would-be double negatives with positivies'''
        if isinstance(prop,Negation):
            return prop.symbol[1]
        else:
            return super(Negation, cls).__new__(cls)
    
    def __init__(self,prop):
        if prop.value==None:
            self.value = None
        else: self.value = not prop.value
        self.symbol = (NegOp(), prop)
    
    def __eq__(self,other):
        return self.symbol[1] == other.symbol[1]
    
    def __ne__(self,other):
        return self.symbol[1] != other.symbol[1]
    
    def __hash__(self):
        return hash((self.symbol[1],'Negation'))
        
            
        
    
class Conjunction(Proposition):
    
    def __init__(self,prop1,prop2):
        self.operands = (prop1,prop2)
        if prop1.value==None or prop2.value==None:
            self.value = None
        else: self.value = prop1.value and prop2.value
        self.symbol = (prop1, AndOp(), prop2)
    
    def __eq__(self,other):
        return frozenset(self.operands) == frozenset(other.operands)
    
    def __ne__(self,other):
        return frozenset(self.operands) != frozenset(other.operands)
    
    def __hash__(self):
        return hash((frozenset(self.operands),'Conjunction'))
        
    
class Disjunction(Proposition):
    
    def __init__(self,prop1,prop2):
        self.operands = (prop1,prop2)
        if prop1.value==None or prop2.value==None:
            self.value = None
        else: self.value = prop1.value or prop2.value
        self.symbol = (prop1, OrOp(), prop2)
        
    def __eq__(self,other):
        return frozenset(self.operands) == frozenset(other.operands)
    
    def __ne__(self,other):
        return frozenset(self.operands) != frozenset(other.operands)
    
    def __hash__(self):
        return hash((frozenset(self.operands),"Disjunction"))
    
class Implication(Proposition):
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent
        if antecedent.value==None or consequent.value==None:
            self.value = None
        else: self.value = not antecedent.value or consequent.value
        self.symbol = (antecedent, ImpOp(), consequent)
        
    def __eq__(self,other):
        return self.antecedent == other.antecedent and self.consequent == other.consequent
    
    def __ne__(self,other):
        return self.antecedent != other.antecedent and self.consequent != other.consequent
    
    def __hash__(self):
        return hash((self.antecedent,self.consequent,"Implication"))
    def __str__(self):
        return self.getPlainText()

#class Biimplication(Proposition):
#
#class ExclusiveOr(Proposition):
        
