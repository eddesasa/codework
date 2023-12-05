all_walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

count = 0
for wall in all_walls:
	if count == 1:
		print('There are at least 1 wall with the word Exterior')
		break

	wall_type_name= wall.Walltype.get.Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString()
	wall_height = wall.getParameter(BuiltParameter.WALL_USER_HEIGHT_PARAM).AsDouble()
	wall_height_m = wall_height *0.3048
	if wall_height_m > 10:
		continue
	
	if 'Exterior' in wall_type_name:
		count += 1
		print("Total Walls containing the word Exterior: " +str(count))
		