from pyparsing import *
import Propositions
from statement import Statement

    
def logicParse(instring):
    variable = oneOf(list(alphas))
    expr = operatorPrecedence( variable,
        [
        (oneOf("~ not !"), 1, opAssoc.RIGHT, Propositions.Negation),
        (oneOf("| or"),  2, opAssoc.LEFT,  Propositions.Disjunction),
        (oneOf("and &"), 2, opAssoc.LEFT,  Propositions.Conjunction),
        (oneOf("-> implies"), 2, opAssoc.LEFT,  Propositions.Implication)
        ])
    parsetree = expr.parseString(instring)[0]
    parsetree.indexTree()
    
    propdict = dict()
    for i in parsetree.getAllIndices():
        propdict[i]=parsetree[i]
    s = Statement(propdict)
    return s






    