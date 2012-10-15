'''
Created on Sep 13, 2012
These are objects that all have a getSuccessorNodes method that checks a given proposition
to see if a particular law or equivalence applies, and returns the result of that
application if it can be. These will be the successors in the graph search. 
@author: colinwinslow
'''

from Propositions import *
from copy import deepcopy

def negate(prop):
    print "negatefunction"
    '''negates without causing double negatives'''
    if isinstance(prop,Negation):
        out = deepcopy(prop.arg)
        out.parent = prop.parent
        out.index = (out.index-1)//2
        out.indexTree()
    else: 
        pp = prop.parent
        out = Negation(prop)
        out.index = out.arg.index
        out.parent = pp
        out.indexTree(out.arg.index)
    return out

class Idempotence():
    
    def __init__(self):
        self.appliesTo = ('Conjunction', 'Disjunction')
        
    def getSuccessorNodes(self, prop):
        if isinstance(prop, Conjunction) or isinstance(prop, Disjunction):
            out = self.simplify(prop)
            try: out.action = "Idempotence"
            except: pass
            return out
        
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
            nota = negate(prop.symbol.a)
            notb = negate(prop.symbol.b)
            out = Disjunction((nota, notb))
            out.action = "De Morgan's Law"
            return out
        elif isinstance(prop.symbol, Disjunction):
            nota = negate(prop.symbol.a)
            notb = negate(prop.symbol.b)
            out = Conjunction((nota, notb))
            out.action = "De Morgan's Law"
            return out
        
class DeMorgansJoin():
    def __init__(self):
        self.appliesTo = ('Conjunction', 'Disjunction')
    def getSuccessorNodes(self, prop):
        if isinstance(prop, Conjunction):
            out = negate(Disjunction([negate(prop.a), negate(prop.b)]))
            out.action = "De Morgan's Law"
            return out
        elif isinstance(prop, Disjunction):
            out = negate(Conjunction([negate(prop.a), negate(prop.b)]))
            out.action = "De Morgan's Law"
            return out
    
class ImplicationLaw(): 
    def __init__(self):
        self.appliesTo = ('Implication', 'Disjunction')
        
    def getSuccessorNodes(self, prop):
        if isinstance(prop, Disjunction):
            out = Implication((Negation(prop.a), prop.b))
            out.action = "Implication Law"
            return out
        if isinstance(prop, Implication):
            out = Disjunction((Negation(prop.a), prop.b))
            out.action= "Implication Law"
            return out
        
class Contraposition():
    def __init__(self):
        self.appliesTo = ('Implication')
        
    def getSuccessorNodes(self, prop):
        if isinstance(prop, Implication):
            out = Implication((Negation(prop.b), Negation(prop.a)))
            out.action = "Contraposition"
            return out
        
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
                    out = Disjunction((overlap.pop(), Conjunction((unique.pop(), unique.pop()))))
                    out.action="Distributive Law"
                    return out
            elif isinstance(prop.a, Disjunction):
                out = Disjunction((Conjunction((prop.b, prop.a.a)), Conjunction((prop.b, prop.a.b))))
                out.action="Distributive Law"
                return out
            elif isinstance(prop.b, Disjunction):
                out = Disjunction((Conjunction((prop.a, prop.b.a)), Conjunction((prop.a, prop.b.b))))
                out.action="Distributive Law"
                return out
            
        if isinstance(prop, Disjunction):
            if isinstance(prop.a, Conjunction) and isinstance(prop.b, Conjunction):
            # this checks to see if we can "undistribute"
                aMembers = set((prop.a.a, prop.a.b))
                bMembers = set((prop.b.a, prop.b.b))
                overlap = aMembers.intersection(bMembers)
                unique = aMembers.symmetric_difference(bMembers)
                if len(overlap) == 1:
                    out = Conjunction((overlap.pop(), Disjunction((unique.pop(), unique.pop()))))
                    out.action="Distributive Law"
                    return out
            elif isinstance(prop.a, Conjunction):
                out = Conjunction((Disjunction((prop.b, prop.a.a)), Disjunction((prop.b, prop.a.b))))
                out.action="Distributive Law"
                return out
            elif isinstance(prop.b, Conjunction):
                out = Conjunction((Disjunction((prop.a, prop.b.a)), Disjunction((prop.a, prop.b.b))))
                out.action = "Distributive Law"
                return out
            
    
        
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
                out = Conjunction([prop.a.a, Conjunction([prop.a.b, prop.b])])
                out.action="Associative Law"
                return out
            elif isinstance(prop.b, Conjunction):
                out = Conjunction([Conjunction([prop.a, prop.b.a]), prop.b.b])
                out.action="Associative Law"
                return out 
        if isinstance(prop, Disjunction):
            if isinstance(prop.a, Disjunction):
                out = Disjunction([prop.a.a, Disjunction([prop.a.b, prop.b])])
                out.action="Associative Law"
                return out 
            elif isinstance(prop.b, Disjunction):
                out = Disjunction([Disjunction([prop.a, prop.b.a]), prop.b.b])
                out.action="Associative Law"
                return out
       
