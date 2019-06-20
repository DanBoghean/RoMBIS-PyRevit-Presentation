__title__ = "Pick By Rectangle\nFamily Name"
__doc__ = "This add-in allows the user to select elements using a rectangular selection \
after running and shows the Family Name of the item selected  in a Task Dialog."

#import the .NET common language runtime to allow us to use the necessary .dll files
import clr

#Add the Revit API Reference to allows us to import elements to work with
clr.AddReference('RevitAPI')

#Add the Revit API UI Reference to allow us to work with the Revit UI Elements
clr.AddReference('RevitAPIUI')

#Once the reference is added, we can import the necessary elements from the Revit API
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import ObjectType

 #__revit__ refers to the Revit Command Data that we can access. Just know that you need the __revit__ instance to be able to access the UI Document
uidoc = __revit__.ActiveUIDocument

#The Revit Document can be accessed as a property of the UI Document
#We define a variable and assign the Document object to so that we can work with it without having to type __revit__.ActiveUIDocument.Document every time
doc = uidoc.Document

###
#PICK BY RECTANGLE METHOD
###

#This returns elements instead of References or ElementIds, so you won't need to use the GetElement method.

selection = uidoc.Selection.PickElementsByRectangle()

#To iterate through the list of ids, we create a for loop that goes through the list and assigns it to the id variable until the list is exhausted. 
#This allows us to work with each element in the list indvidually.
for element in selection:
	#Now that we have the element, we can work with it, in this case, we can use the Revit Python Shell to figure out how to access the family name of the element and print it to a Task Dialog
	TaskDialog.Show("BILT NA 2019", element.Symbol.Family.Name)