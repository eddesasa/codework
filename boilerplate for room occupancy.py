# Import necessary Dynamo libraries
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction

# Access the current Revit document
doc = DocumentManager.Instance.CurrentDBDocument

# Start a transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# Get rooms using Dynamo's FilteredElementCollector
rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()

element = IN[0]


# Define a function to set parameter by name
def SetParameterByName(element, parameterName, value):
    parameter = element.LookupParameter(parameterName)
    if parameter:
        parameter.Set(value)
    OUT = element
   

# Loop through rooms and set parameters
for room in rooms:
    area = room.Area
    occup_load = round(IN[2] / 100)
    
    SetParameterByName(room, IN[1], occup_load)

# Commit the transaction
TransactionManager.Instance.TransactionTaskDone()

