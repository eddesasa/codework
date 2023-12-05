from Autodesk.Revit.DB import *
import re


all_columns = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Columns).WhereElementIsNotElementType().ToElements()
all_walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
all_beams = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()
all_foundations = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFoundation).WhereElementIsNotElementType().ToElements()
all_floors = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType().ToElements()
all_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()
all_levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()
'''
print(all_columns)
print(all_walls)
print(all_beams)
print(all_foundations)
print(all_floors)

for column in all_columns:
	print(column)

for wall in all_walls:
	print(wall)
	
for beam in all_beams:
	print(beam)
	
for foundation in all_foundations:
	print(foundation)
	
for floor in all_floors:
	print(floor)

for room in all_rooms:
	print(room.Level.Name)
	
	
	
for level in all_levels:
	print(level)
'''

#for level in all_levels:
#	print(level.Level)

'''for level in all_levels:
	param = level.Parameters
	room_name = room.LookupParameter('Name')
	print(room_name)

'''

'''
t = Transaction(doc, 'Setup')
t.Start()

i=1
j=1
k=1

for room in all_rooms:
	#print(room.Name)
	#param = room.Parameters
	#print(room)
	room_name = room.LookupParameter('Name')
	room_level = room.Level.Name
	#print(room_name)
	print(room.Name)
	
	
	level_pattern_one = r'^01'
	level_pattern_two = r'^02'
	level_pattern_three = r'^03'
			
	if (re.search(level_pattern_one, room_level)):
		room_name.Set(str(i)+'-Ground Floor')
		i+=1
	elif(re.search(level_pattern_two, room_level)):
		room_name.Set(str(j)+'-First Floor')
		j+=1
	elif(re.search(level_pattern_three, room_level)):
		room_name.Set(str(k)+'-Cobertura')
		k+=1
	else:
		print ('No Match')
			
t.Commit()	
'''

t = Transaction(doc, 'Setup')
t.Start()

i=100
j=200
k=300
for room in all_rooms:
	print(room.Number)
	room_number = room.Number
	room_level = room.Level.Name
	
	level_pattern_one = r'^01'
	level_pattern_two = r'^02'
	level_pattern_three = r'^03'
			
	if (re.search(level_pattern_one, room_level)):
		#room_number.Set(str(j))
		#room_number= str(i)
		room.Number = str(i)
		i+=1
	elif(re.search(level_pattern_two, room_level)):
		#room_number.Set(str(j))
		#room_number = str(j)
		room.Number = str(j)
		j+=1
	elif(re.search(level_pattern_three, room_level)):
		#room_number = str(k)
		#room_number.Set(str(k))
		room.Number = str(k)
		k+=1
	else:
		print ('No Match')
	
t.Commit()		
		
'''
for room in all_rooms:
	print(type(room.Level))
'''

