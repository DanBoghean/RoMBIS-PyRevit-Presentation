__title__ = "Gather all Walls"
__doc__ = "This add-in uses the FilteredElementCollector with the OfClass() method to gather all the walls in the project"

#import the .NET common language runtime to allow us to use the necessary .dll files
import clr

#Add the Revit API Reference to allows us to import elements to work with
clr.AddReference('RevitAPI')

#Add the Revit API UI Reference to allow us to work with the Revit UI Elements
clr.AddReference('RevitAPIUI')

#Once the reference is added, we can import the necessary elements from the Revit API
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

 #__revit__ refers to the Revit Command Data that we can access. Just know that you need the __revit__ instance to be able to access the UI Document
uidoc = __revit__.ActiveUIDocument

#The Revit Document can be accessed as a property of the UI Document
#We define a variable and assign the Document object to so that we can work with it without having to type __revit__.ActiveUIDocument.Document every time
doc = uidoc.Document

#The FilteredElementCollector allows us to get a list of elements based on specific parameters. First we create an instance of the FilteredElementCollector by inputting the Document as an argument
fec = FilteredElementCollector(doc)

#Then we can apply different modifiers to get what we want. In this class, we can find all the walls in the project by using the OfClass() method and providing the Wall argument
elements = fec.OfClass(Wall)

#You can also use the OfCategory() method and provide a BuiltInCategory enumeration
#elements = fec.OfCategory(BuiltInCategory.OST_Walls)

for element in elements:
	print(element.Name)
	
