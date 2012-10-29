'''
Created on Oct 29, 2012

@author: colinwinslow
'''
from copy import copy

class Derivation():

    def __init__(self,start,goal,tracebackResults,rules):
        self.startStatement = start
        self.goalStatement = goal
        self.steps = tracebackResults
        self.rules = rules
        self.ruleSet = frozenset([r.name for r in rules])
    
    def __getitem__(self,key):
        return self.steps[key]
    
    def __len__(self):
        return len(self.steps)
    
    def __hash__(self):
        return hash((self.startStatement.simHash(),self.goalStatement.simHash(),self.ruleSet))
    
    def reMap(self,newPropMap):
        '''returns a copy with re-mapped props'''
        copy = copy(self)
        copy.startStatement.propMap = newPropMap
        copy.goalStatement.propMap = newPropMap
        for s in copy.steps:
            s.state.propMap = newPropMap
        return copy
        
    