'''
Created on Sep 13, 2012

@author: colinwinslow
'''

class EquivalenceRule():
    def __init__(self,cases):
        self.cases = cases
        



class Idempotence(EquivalenceRule):
    
    super.__init__(('And','Or'))
    
    def simplify(self,prop):
        if prop.conjunctees[0]==prop.conjunctees[1]:
            return (prop.conjunctees[0],'Idempotent Law')
            
        
        
    def expand(self,prop):
    