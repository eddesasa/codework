#boilerplate text
import clr

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

#Preparing input from dynamo to revit
famDocs = IN[0]
famNames = [f.Title for f in famDocs]

#Get all the data we need to support this workflow

famTypesList, famTypeNamesList, famParamsList, famParamNamesList = [],[],[],[]

for f in famDocs:
    famMan = f.FamilyManager
    #get type data
    famTypes = list(famMan.Types)
    typeNames = [f.Name for f in famTypes]
    famTypesList.append(famTypes)
    famTypeNamesList.append(typeNames)
    #get parameter data
    params = famMan.GetParameters()
    paramNames = [p.Definition.Name for p in params]
    famParamsList.append(params)
    famParamNamesList.append(paramNames)
    
def famDoc_setParameter(famDoc, p, t, v):
    try: 
        famMan = famDoc.FamilyManager
        famMan.CurrentType = t
        famMan.Set(p,v)
        return True
    except:
        return False

#Get excel data
outcomesList = []
paramNames = IN[1]
excelData = IN[2]


for row in excelData:
    #Result for the row
    outcomes = []
    #Get the family
    famInd = famNames.index(row[0])
    famDoc = famDocs[famInd]
    #Get the type
    typeInd = famTypeNamesList[famInd].index(row[1])
    famType = famTypesList[famInd][typeInd]
    #Limit to just parameters
    values = row[2:]
    #Start a transaction
    t = Transaction(famDoc, row[0]+" - "row[1])
    t.Start()
    #Do some things
    for p,v in zip(paramNames, values):
        # Get the parameter
        parInd = famParamNamesList[famInd].index(p)
        famPar = famParamsList[famInd][parInd]
        #Set the Parameter
        setParam = famDoc_setParameter(famDoc, famPar, famType, v)
        outcomes.append(setParam)
    #commiting the transaction
    t.Commit()
    #Append the outcomes list
    outcomesList.append(outcomes)
    
#Declare output
OUT = outcomesList