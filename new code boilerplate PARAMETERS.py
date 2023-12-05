from Autodesk.Revit.DB import BuiltInCategory as Bic
from Autodesk.Revit.DB import FilteredElementCollector as Fec

rooms = Fec(doc).OfCategory(Bic.OST_Rooms).WhereElementIsNotElementType().ToElements()

parameter_list =[]
parameter_dict={}

for room in rooms:
	parameter = room.Parameters
	for param in parameter:
		
		
		parameter_dict[param.Definition.Name]=param.AsValueString()
		#print(param.Definition.Name)
		#print(param.AsValueString())
	parameter_list.append(parameter_dict)
	print(parameter)