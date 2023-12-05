from Autodesk.Revit.DB import BuiltInCategory as Bic
from Autodesk.Revit.DB import FilteredElementCollector as Fec
from Autodesk.Revit import *

#rooms = Fec(doc).OfCategory(Bic.OST_Rooms).WhereElementIsNotElementType().ToElements()

#parameter_list =[]
#parameter_dict={}

#for room in rooms:
	
room_id = ElementId(1201474)
room =  doc.GetElement(room_id)
room_parameters = room.Parameters
room_area = room.get_Parameter(BuiltInParameter.ROOM_AREA)

room_occupancy = room.LookupParameter('Occupancy').AsString()
print(room_occupancy)


__title__= "Nothing"
t = Transaction(doc, __title__ )
t.Start()
room_occupancy.Set('666').AsString()
print(room_occupancy)
t.Commit()

























'''for item in room_parameters:
	print(item.Definition)
	print(room_parameters)
	print(item.Definition.Name)
	print(room_area)
	'''
#print(room.LookupParameter('Volume').AsDouble())
#print(room.LookupParameter('Type Name').AsString())
#print(room)
#print(room_parameters)
#print(room_area)



#print(room_parameters.Definition.Name)
#print(room_area)
#print(room_parameters)
#print(room)
#print(list(room.Parameters))

 	#room_id =  room.Id
	#room_element = doc.GetElement(room_id)
	#room_parameters = room.Parameters
	#room_location = room.Location
	#room_name = room.Name
	#useless = room.get_Parameter(BuiltInParameter.ROOM_ACTUAL_LIGHTING_LOAD_PARAM).AsDouble()
	#room_area = room.Area
	#room_perimeter = room.Perimeter
	#room_parameters_Map = room.get_Parameter(BuiltInParameter.ROOM_AREA).AsDouble()
	#room_number = room.Number
	#room_location = room.Location.Point
	#room_ordered_parameters = room.GetOrderedParameters()
	#room_area_param = DB.BuiltInParameter.ROOM_AREA
	#room_area_param_element = room.get_Parameter(room_area_param).AsDouble()
	#room_location_DB = DB.Location
	#parameter = room.LookupParameter('ROOM_AREA')
	#element = doc.GetElement(room.Id)
	#new_parameter = element.get_Parameter(room_area_param).AsDouble()
	#value=20
	#new_parameter.Set()
	
	#print(30*'-')
	#print(new_parameter)
	#print(30*'-')
	
	#print(20*'-')
	#print(room_id)
	#print(room_element)
	#print(room_parameters)
	#print(room_location)
	#print(room_name)
	#print(useless)
	#print(room_area)
	#print(room_perimeter)
	#print(room_parameters_Map)
	#print(room_number)
	#print(room_location)
	#print(room_ordered_parameters)
	#print(room_area_param)
	#print(room_area_param_element)
	#print(room_location_DB)
	#print(parameter)
	
	#print(20*'-')
	#'''
	
	
		