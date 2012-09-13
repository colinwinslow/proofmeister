'''
Created on Sep 13, 2012

@author: colinwinslow
'''

from Propositions import *


class Idempotence():
    
    def __init__(self):
        self.appliesTo = ('Conjunction','Disjunction')
        
    def getSucessors(self,prop):
        return self.simplify(prop)
        
    def simplify(self,prop):
        if prop.operands[0]==prop.operands[1]:
            return (prop.operands[0],'Idempotent Law')
        
class DoubleNegativity():
    
    def __init__(self):
        self.appliesTo = ('Negation')
    
    def getSucessors(self,prop):
        if isinstance(prop.symbol[1],Negation):
            return prop.symbol[1].symbol[1]
        


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
        
    