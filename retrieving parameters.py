import Autodesk.Revit.DB as DB

# Assume that 'doc' is defined elsewhere in your code
# Specify the category you are interested in (e.g., Doors)
category_name = "Doors"

# Get the category object
category = DB.Category.GetCategory(doc, DB.BuiltInCategory.OST_Doors)

if category:
    # Get all parameters of the category
    parameters = category.Parameters

    # Create a list to store parameter names
    parameter_names = []

    # Loop through parameters and add names to the list
    for param in parameters:
        parameter_names.append(param.Definition.Name)

    # Print the list of parameter names
    print(parameter_names)
else:
    print("Category not found.")