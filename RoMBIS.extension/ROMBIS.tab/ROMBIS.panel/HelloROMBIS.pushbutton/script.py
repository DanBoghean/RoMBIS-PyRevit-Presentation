__title__ = "Hello ROMBIS!"
__doc__ = "This add-in shows a TaskDialog that exclaims 'Welcome to ROMBIS!'"

#import the .NET common language runtime to allow us to use the necessary .dll files
import clr

#Add the Revit API Reference to allows us to import elements to work with
clr.AddReference('RevitAPIUI')

#Once the reference is added, we can import the necessary elements from the Revit API
from Autodesk.Revit.UI import TaskDialog

#The TaskDialog class allows us to use the Show method to create a Task Dialog in Revit with two required arguments: Title and Main Instruction
TaskDialog.Show("ROMBIS", "Welcome to ROMBIS!")
