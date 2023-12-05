from Autodesk.Revit.DB import *
#import clr
#clr.AddReference('RevitAPI')
#clr.AddReference('RevitAPIUI')

all_elements = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

#Can't do it this way because it has to iterate within the element first to access the methods available within
#for i in all_elements:
#	print(all_elements.Parameters.Definition.BuiltInParameter)

#iterate in all_elements first then nominate which method you wish to iterate further and iterate within that.
for element in all_elements:
	print('1')
	print(15*'-')
	param = element.Parameters
	print(param)
	print('2')
	print(element)
	print(15*'-')
	print('3')
	print(param)
	i=0
	print(type(param))
	for p in param:
		print(15*'-')
		print(i)
		print(15*'**')
		print(type(p.Definition))
		
		name_el = p.Definition.Name
		print(type(name_el))
		name_el_value = p.Definition.Id
		print(type(name_el_value))
		print(15*'-')
		print (name_el)
		print(name_el_value)
		i+=1
		print(30*'&&')