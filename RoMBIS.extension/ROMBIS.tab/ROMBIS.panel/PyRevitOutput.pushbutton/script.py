__title__ = "PyRevit Ouput Print"
__doc__ = "This will print to the PyRevit output as an example of how to show data to the user."

#import the .NET common language runtime to allow us to use the necessary .dll files
import clr

#Add the Revit API Reference to allows us to import elements to work with
clr.AddReference('RevitAPI')

#Add the Revit API UI Reference to allow us to work with the Revit UI Elements
clr.AddReference('RevitAPIUI')

#Once the reference is added, we can import the necessary elements from the Revit API
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#The Revit Document can be accessed as a property of the UI Document
#We define a variable and assign the Document object to so that we can work with it without having to type __revit__.ActiveUIDocument.Document every time
doc = uidoc.Document

#We've defined a list with three elements that we would like to print to a PyRevit output using a default Python list
list = ["1. First Thing", "2. Second Thing", "3. Third Thing"]

#Using a for loop, we can cycle through the items in the list and perform an action on each one individually. In this case, all we need to do to have PyRevit output it to a window is to use the Python print() statement.
#This can be used to output lots of information directly to the user in a easy to use format.
for item in list:
	print(item)