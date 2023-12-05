# Import necessary Dynamo libraries
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction

#import Revit Nodes
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Access the current Revit document
doc = DocumentManager.Instance.CurrentDBDocument

# Start a transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# Get rooms using Dynamo's FilteredElementCollector
rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()

element = IN[0]


# Define a function to set parameter by name
def SetParameterByName(element, parameterName, value):
    parameter_dict = []
    parameter = element.LookupParameter(parameterName)
    if parameter:
        parameter.Set(value)
        parameter_dict.append({parameterName, value})
    return parameter_dict  
   
   
resultElements =[]
# Loop through rooms and set parameters
for room in rooms:
   
    occup_load = round(IN[2]/ 100)
    
    resultElements.append(SetParameterByName(room, IN[1], occup_load))

# Commit the transaction
TransactionManager.Instance.TransactionTaskDone()

OUT = resultElements