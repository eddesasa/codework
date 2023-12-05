from Autodesk.Revit.DB import *

all_elements = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()
print(15*'%%%$$$')
print(all_elements)
print(15*'%%%$$$')

for element in all_elements:
	print(15*'-')
	param = element.Parameters
	print (param)
	print(element)
	print(15*'-')
	print(15*'()()()()()()()()')
	room_occupancy_element = element.LookupParameter('Occupancy')
	print(room_occupancy_element.AsString())
	
	#room_occupancy_param = param.LookupParameter('Occupancy')
	#print(room_occupancy_param)
	
	print(15*'()()()()()()()()')
	'''for p in param:
		print(p)
		#room_occupancy_two = p.LookupParameter('Occupancy')
		#print(room_occupancy)
		p_name=p.Definition.Name
		p_id = p.Definition.Id
		#print(p_name)
		print (f"{p_name}:{p_id}")'''