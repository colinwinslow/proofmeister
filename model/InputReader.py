from pyparsing import *
import Propositions


    
def logicParse(instring):
    variable = oneOf(list(alphas))
    expr = operatorPrecedence( variable,
        [
        (oneOf("~ not !"), 1, opAssoc.RIGHT, Propositions.Negation),
        (oneOf("| or"),  2, opAssoc.LEFT,  Propositions.Disjunction),
        (oneOf("and &"), 2, opAssoc.LEFT,  Propositions.Conjunction),
        (oneOf("-> implies"), 2, opAssoc.LEFT,  Propositions.Implication)
        ])
    out = expr.parseString(instring)[0]
    out.indexTree()
    return out






    