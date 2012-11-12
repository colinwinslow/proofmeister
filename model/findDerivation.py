from InputReader import logicParse
from pickle import Pickler,Unpickler
from dbtesting import *
from model.Search import search


def findDerivation(startStr,goalStr,rules):
    
    #parse start and goal
    startParse = logicParse(startStr)
    goalParse = logicParse(goalStr,startParse.propMap)
    
    #calculate hash
    thisSearchHash = hash((startParse,goalParse))
    
    #check db to see if we have done this proof before
    queryResult = fetch(thisSearchHash)
    
    
    
    #if so, pull the derivation from the database
    if queryResult:
        print "It was cached"
        cachedProof = pickle.loads(queryResult[0][2])
        return cachedProof.reMap(startParse.propMap)
    
    
    #otherwise, run the search. 
    else:
        print "Running the search"
        queryResult = search(startParse,goalParse,rules)
    
    #and add it to the db
        addItem(thisSearchHash,queryResult)
        return queryResult