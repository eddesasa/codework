from Autodesk.Revit.DB import BuiltInCategory as Bic
from Autodesk.Revit.DB import FilteredElementCollector as Fec
from Autodesk.Revit.DB import *

rooms = Fec(doc).OfCategory(Bic.OST_Rooms).WhereElementIsNotElementType().ToElements()
#print(rooms)


__title__ = 'Transaction 1'	
t = Transaction(doc, __title__)
t.Start()


for room in rooms:
	
	room_parameter = room.Parameters
	room_parameter_map = room.ParametersMap
	room_area = room.Area
	room_occupancy = room.LookupParameter('Occupancy')
	new_occupancy = str(room_area/100)
	room_occupancy.Set(new_occupancy)
	print(room_occupancy.AsString())
	
t.Commit()




	