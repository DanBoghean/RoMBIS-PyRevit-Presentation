__title__ = "Pick Object\nFamily Name"
__doc__ = "This add-in allows the user to select elements after running and \
shows the Family Name of the item selected  in a Task Dialog. \
This only allows for the user to select one item."

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
#PICK OBJECT METHOD
###

#If we want to allow the user to pick elements after the add-in is launched, we can use the PickObject() or PickObjects() methods. This will prompt the user to select elements and put the selected items into a list.

#The PickObject() method requires one argument which is an enumeration of ObjectType. See the apidocs.co website for the possible options. It returns a Reference instead of an ElementId

selectionReference = uidoc.Selection.PickObject(ObjectType.Element)

#We can use the GetElement() method of the document to access the element the Reference is pointing to
selectionElement = doc.GetElement(selectionReference)

TaskDialog.Show("BILT NA 2019", selectionElement.Symbol.Family.Name)