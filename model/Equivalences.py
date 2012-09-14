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
            print prop.symbol.getPlainText()
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
        
class DeMorgansJoin():
    def __init__(self):
        self.appliesTo = ('Conjunction','Disjunction')
    def getSuccessors(self,prop):
        if isinstance(prop,Conjunction):
            output = Negation(Disjunction(Negation(prop.operands[0]),Negation(prop.operands[1])))
        elif isinstance(prop,Disjunction):
            output = Negation(Conjunction(Negation(prop.operands[0]),Negation(prop.operands[1])))
        else: output = []
        return output 
    
class ImplicationLaw(): 
    def __init__(self):
        self.appliesTo = ('Implication','Disjunction')
        
    def getSuccessors(self,prop):
        if isinstance(prop,Disjunction):
            return Implication(Negation(prop.operands[0]),prop.operands[1])
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