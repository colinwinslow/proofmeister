'''
Created on Sep 13, 2012
These are objects that all have a getSucessors method that checks a given propisition
to see if a particular law or equivalence applies, and returns the result of that
application if it can be. These will be the successors in the graph search. 
@author: colinwinslow
'''

from Propositions import *


class Idempotence():
    
    def __init__(self):
        self.appliesTo = ('Conjunction','Disjunction')
        
    def getSucessors(self,prop):
        if isinstance(prop,Conjunction) or isinstance(prop,Disjunction):
            return self.simplify(prop)
        
    def simplify(self,prop):
        if prop.operands[0]==prop.operands[1]:
            return (prop.operands[0],'Idempotent Law')
        
class DoubleNegativity():
    
    def __init__(self):
        self.appliesTo = ('Negation')
    
    def getSucessors(self,prop):
        if isinstance(prop,Negation):
            if isinstance(prop.symbol[1],Negation):
                return prop.symbol[1].symbol[1]
        
class DeMorgansSplit():
    def __init__(self):
        self.appliesTo = ('Negation')
    
    def getSucessors(self,prop):
        if isinstance(prop.symbol[1], Conjunction):
            nota = Negation(prop.symbol[1].operands[0])
            notb = Negation(prop.symbol[1].operands[1])
            return Disjunction(nota,notb)
        elif isinstance(prop.symbol[1], Disjunction):
            nota = Negation(prop.symbol[1].operands[0])
            notb = Negation(prop.symbol[1].operands[1])
            return Conjunction(nota,notb)
        
        


#class Associativity():
#    
#    def __init__(self):
#        self.appliesTo = ('Conjunction','Disjunction')
#        
#    def getSucessors(self,prop):
#        if isinstance(prop.operands[0],Conjunction) or isinstance(prop.operands[1],Conjunction):
#            conj = self.conjunctionAssociate(prop)
#        if isinstance(prop.operands[0],Disjunction) or isinstance(prop.operands[1],Disjunction):
#            disj = self.disjunctionAssociate(prop)
#        return conj+disj
#            
#        
#    def conjunctionAssociate(self,prop):
#        output = []
#        print prop.getPlainText()
#        for p in prop.operands:
#            if 
#            return (prop.operands[0],'Associative Law')