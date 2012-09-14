'''
Created on Sep 13, 2012
These are objects that all have a getSuccessors method that checks a given propisition
to see if a particular law or equivalence applies, and returns the result of that
application if it can be. These will be the successors in the graph search. 
@author: colinwinslow
'''

from Propositions import *


class Idempotence():
    
    def __init__(self):
        self.appliesTo = ('Conjunction','Disjunction')
        
    def getSuccessors(self,prop):
        if isinstance(prop,Conjunction) or isinstance(prop,Disjunction):
            return self.simplify(prop)
        
    def simplify(self,prop):
        if prop.a==prop.b:
            return (prop.a,'Idempotent Law')
        
class DoubleNegativity():
    
    def __init__(self):
        self.appliesTo = ('Negation')
    
    def getSuccessors(self,prop):
        if isinstance(prop,Negation):
            if isinstance(prop.symbol,Negation):
                return prop.symbol.symbol
        
class DeMorgansSplit():
    def __init__(self):
        self.appliesTo = ('Negation')
    
    def getSuccessors(self,prop):
        if isinstance(prop.symbol, Conjunction):
            nota = Negation(prop.symbol.a)
            notb = Negation(prop.symbol.b)
            return Disjunction(nota,notb)
        elif isinstance(prop.symbol, Disjunction):
            nota = Negation(prop.symbol.a)
            notb = Negation(prop.symbol.b)
            return Conjunction(nota,notb)
        
class DeMorgansJoin():
    def __init__(self):
        self.appliesTo = ('Conjunction','Disjunction')
    def getSuccessors(self,prop):
        if isinstance(prop,Conjunction):
            output = Negation(Disjunction(Negation(prop.a),Negation(prop.b)))
        elif isinstance(prop,Disjunction):
            output = Negation(Conjunction(Negation(prop.a),Negation(prop.b)))
        else: output = []
        return output 
    
class ImplicationLaw(): 
    def __init__(self):
        self.appliesTo = ('Implication','Disjunction')
        
    def getSuccessors(self,prop):
        if isinstance(prop,Disjunction):
            return Implication(Negation(prop.a),prop.b)
        if isinstance(prop,Implication):
            return Disjunction(Negation(prop.antecedent),prop.consequent)
        
class Contraposition():
    def __init__(self):
        self.appliesTo = ('Implication')
        
    def getSuccessors(self,prop):
        if isinstance(prop,Implication):
            return Implication(Negation(prop.antecedent),Negation(prop.consequent))
        
    
        
        


#class Associativity():
#    
#    def __init__(self):
#        self.appliesTo = ('Conjunction','Disjunction')
#        
#    def getSuccessors(self,prop):
#        if isinstance(prop.a,Conjunction) or isinstance(prop.b,Conjunction):
#            conj = self.conjunctionAssociate(prop)
#        if isinstance(prop.a,Disjunction) or isinstance(prop.b,Disjunction):
#            disj = self.disjunctionAssociate(prop)
#        return conj+disj
#            
#        
#    def conjunctionAssociate(self,prop):
#        output = []
#        for p in prop.operands:
#            if 
#            return (prop.a,'Associative Law')