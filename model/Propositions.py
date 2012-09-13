'''
Created on Sep 12, 2012

@author: colinwinslow
'''
from LogicalOperators import *

class Proposition():
    
    def __init__(self,symbol,value=None):
        self.symbol = (symbol)
        self.value = value

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
    
    def __init__(self,parent):
        if parent.value==None:
            self.value = None
        else: self.value = not parent.value
        self.symbol = ('~', parent.symbol)
            
        
    
class Conjunction(Proposition):
    
    def __init__(self,prop1,prop2):
        self.conjunctees = set([prop1,prop2])
        if prop1.value==None or prop2.value==None:
            self.value = None
        else: self.value = prop1.value and prop2.value
        self.symbol = (prop1, AndOp(), prop2)
    
    #this one will need an equivalence method so A&B == B&A
    
class Disjunction(Proposition):
    
    def __init__(self,prop1,prop2):
        self.conjunctees = set([prop1,prop2])
        if prop1.value==None or prop2.value==None:
            self.value = None
        else: self.value = prop1.value or prop2.value
        self.symbol = (prop1, OrOp(), prop2)
        
    #this one will need an equivalence method so AvB == BvA
    
class Implication(Proposition):
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent
        if antecedent.value==None or consequent.value==None:
            self.value = None
        else: self.value = not antecedent.value or consequent.value
        self.symbol = (antecedent, ImpOp(), consequent)

#class Biimplication(Proposition):
#
#class ExclusiveOr(Proposition):
        
