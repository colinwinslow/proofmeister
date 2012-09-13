'''
Created on Sep 13, 2012

@author: colinwinslow
'''

class AndOp():
    
    def getLaTeX(self):
        return '\\wedge'
                
    def getSymbols(self):
        return 'and '       
    
    def getMathML(self):
        return 'mathml AND'
    
    def getPlainText(self):
        return self.getSymbols()
    
    def __str__(self):
        return "&"
    
class OrOp():
    
    def getLaTeX(self):
        return '\\vee'
                
    def getSymbols(self):
        return 'or '       
    
    def getMathML(self):
        return 'mathml OR'
    
    def getPlainText(self):
        return self.getSymbols()
    
    def __str__(self):
        return "v "
    
class ImpOp():
    
    def getLaTeX(self):
        return '\\rightarrow'
                
    def getSymbols(self):
        return 'implies '       
    
    def getMathML(self):
        return 'mathml IMPLIES'
    
    def getPlainText(self):
        return self.getSymbols()
    
    def __str__(self):
        return "->"