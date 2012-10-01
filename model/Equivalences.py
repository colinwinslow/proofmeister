'''
Created on Sep 13, 2012
These are objects that all have a getSuccessorNodes method that checks a given proposition
to see if a particular law or equivalence applies, and returns the result of that
application if it can be. These will be the successors in the graph search. 
@author: colinwinslow
'''

from Propositions import *



class Idempotence():
    
    def __init__(self):
        self.appliesTo = ('Conjunction', 'Disjunction')
        
    def getSuccessorNodes(self, prop):
        if isinstance(prop, Conjunction) or isinstance(prop, Disjunction):
            return self.simplify(prop)
        
    def simplify(self, prop):
        if prop.a==prop.b:
            return prop.a
        
class DoubleNegativity():
    
    def __init__(self):
        self.appliesTo = ('Negation')
    
    def getSuccessorNodes(self, prop):
        if isinstance(prop, Negation):
            if isinstance(prop.symbol, Negation):
                return prop.symbol.symbol
        
class DeMorgansSplit():
    def __init__(self):
        self.appliesTo = ('Negation')
    
    def getSuccessorNodes(self, prop):
        if isinstance(prop.symbol, Conjunction):
            nota = Negation(prop.symbol.a)
            notb = Negation(prop.symbol.b)
            return Disjunction(nota, notb, type(self))
        elif isinstance(prop.symbol, Disjunction):
            nota = Negation(prop.symbol.a)
            notb = Negation(prop.symbol.b)
            return Conjunction(nota, notb, type(self))
        
class DeMorgansJoin():
    def __init__(self):
        self.appliesTo = ('Conjunction', 'Disjunction')
    def getSuccessorNodes(self, prop):
        if isinstance(prop, Conjunction):
            return Negation(Disjunction(Negation(prop.a), Negation(prop.b)), type(self))
        elif isinstance(prop, Disjunction):
            return Negation(Conjunction(Negation(prop.a), Negation(prop.b)), type(self))
    
class ImplicationLaw(): 
    def __init__(self):
        self.appliesTo = ('Implication', 'Disjunction')
        
    def getSuccessorNodes(self, prop):
        if isinstance(prop, Disjunction):
            return Implication(Negation(prop.a), prop.b, type(self))
        if isinstance(prop, Implication):
            return Disjunction(Negation(prop.a), prop.b, type(self))
        
class Contraposition():
    def __init__(self):
        self.appliesTo = ('Implication')
        
    def getSuccessorNodes(self, prop):
        if isinstance(prop, Implication):
            return Implication(Negation(prop.a), Negation(prop.b), type(self))
        
class Distributivity():
    def __init__(self):
        self.appliesTo = ('Conjunction', 'Disjunction')
    
    def getSuccessorNodes(self, prop):
        if isinstance(prop, Conjunction):
            if isinstance(prop.a, Disjunction) and isinstance(prop.b, Disjunction):
            # this checks to see if we can "undistribute"
                aMembers = set((prop.a.a, prop.a.b))
                bMembers = set((prop.b.a, prop.b.b))
                overlap = aMembers.intersection(bMembers)
                unique = aMembers.symmetric_difference(bMembers)
                if len(overlap) == 1:
                    return Disjunction(overlap.pop(), Conjunction(unique.pop(), unique.pop()), type(self))
            elif isinstance(prop.a, Disjunction):
                return Disjunction(Conjunction(prop.b, prop.a.a), Conjunction(prop.b, prop.a.b), type(self))
            elif isinstance(prop.b, Disjunction):
                return Disjunction(Conjunction(prop.a, prop.b.a), Conjunction(prop.a, prop.b.b), type(self))
            
        if isinstance(prop, Disjunction):
            if isinstance(prop.a, Conjunction) and isinstance(prop.b, Conjunction):
            # this checks to see if we can "undistribute"
                aMembers = set((prop.a.a, prop.a.b))
                bMembers = set((prop.b.a, prop.b.b))
                overlap = aMembers.intersection(bMembers)
                unique = aMembers.symmetric_difference(bMembers)
                if len(overlap) == 1:
                    return Conjunction(overlap.pop(), Disjunction(unique.pop(), unique.pop()), type(self))
            elif isinstance(prop.a, Conjunction):
                return Conjunction(Disjunction(prop.b, prop.a.a), Disjunction(prop.b, prop.a.b), type(self))
            elif isinstance(prop.b, Conjunction):
                return Conjunction(Disjunction(prop.a, prop.b.a), Disjunction(prop.a, prop.b.b), type(self))
            
    
        
class Absorption():
    def __init__(self):
        self.appliesTo = ('Conjunction', 'Disjunction')
        
    def getSuccessorNodes(self, prop):
        return None

class Associativity():
    def __init__(self):
        self.appliesTo = ('Conjunction', 'Disjunction')
        
    def getSuccessorNodes(self, prop):
        if isinstance(prop, Conjunction):
            if isinstance(prop.a, Conjunction):
                return Conjunction(prop.a.a, Conjunction(prop.a.b, prop.b), type(self))
            elif isinstance(prop.b, Conjunction):
                return Conjunction(Conjunction(prop.a, prop.b.a), prop.b.b, type(self))
        if isinstance(prop, Disjunction):
            if isinstance(prop.a, Disjunction):
                return Disjunction(prop.a.a, Disjunction(prop.a.b, prop.b), type(self))
            elif isinstance(prop.b, Disjunction):
                return Disjunction(Disjunction(prop.a, prop.b.a), prop.b.b, type(self))
       
