__title__ = "Create Elements"
__doc__ = "Create a new plumbing fixture instance using the Revit API"

#import the .NET common language runtime to allow us to use the necessary .dll files
import clr

#We import sys so that we can use the exit() method if a part of our script breaks
import sys

#Add the Revit API Reference to allows us to import elements to work with
clr.AddReference('RevitAPI')

#Add the Revit API UI Reference to allow us to work with the Revit UI Elements
clr.AddReference('RevitAPIUI')

#Once the reference is added, we can import the necessary elements from the Revit API
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#We need to make sure we import the SturcturalType enumeration from the Structure Class in order to use the NewFamilyInstance Class later on
from Autodesk.Revit.DB.Structure import StructuralType

 #__revit__ refers to the Revit Command Data that we can access. Just know that you need the __revit__ instance to be able to access the UI Document
uidoc = __revit__.ActiveUIDocument

#The Revit Document can be accessed as a property of the UI Document
#We define a variable and assign the Document object to so that we can work with it without having to type __revit__.ActiveUIDocument.Document every time
doc = uidoc.Document

#We can get the Active View by using the ActiveView property of the Document
activeView = doc.ActiveView

#We need to find the Type (FamilySymbol) we want to create in Revit. In order to do that, we can use a FilteredElementCollector and cycle through to find one that matches the name we are interested in.

fec = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PlumbingFixtures).WhereElementIsElementType()

for type in fec:
	#Usually, we'd be able to use something like type.Name but in this case, because of some weird casting for FamilySymbol in the Revit API and python, we have to get create and use Element.Name.GetValue(type). This gives us the name of the type to check against to find the one we want
	typeName = Element.Name.GetValue(type)
	typeTest = '42" x 21"'
	
	#We create an if statement to find the type we want by testing to see if the name equals the one we are looking for
	if typeName == typeTest:
		
		#If the type name we want is found, then we can assign it to a variable to be used later in our script
		familySymbol = type
		
#Any time that we change anything within Revit, we must use a Transaction to encompass that change. This will also correspond to the Undo/Redo actions for everything contained in the Transaction
transaction = Transaction(doc, "Create Element")

#After the Transaction object is created, we have to call the Start() method in order to initate the transcation to make any changes
transaction.Start()

#Try/Except blocks allow us to catch exceptions that might occur. In this case, we are creating a new instance with the familySymbol we had defined previously be iterating through our FilteredElementCollector. However, since we are not instituting a check to see if the type we are looking for is found, there is a chance that our familySymbol parameter never gets created.
#This is where the Try/Except block comes in. If an error occurs within this block of code, it skips to the except block and executes whatever is there and continue to read the rest of the code. In this case, we are calling the exit() methon from sys in order to exit the script after a Task Dialog is shown because we don't want to keep the code running.
try:
	#We're using the Create property of the Document to call the NewFamilyInsatance() method. This has 3 argumentst: the XYZ location, the FamilySymbol (Revit Type), and the View to place it in. 
	doc.Create.NewFamilyInstance(XYZ(0,0,0), familySymbol, StructuralType.NonStructural)
	
except Exception as e:
	#If an exception occurs, a Task Dialog gives some information and the script exits.
	TaskDialog.Show("Error", str(e))
	
	#We can call the RollBack() method on the transaction to undo all of the changes since the script didn't make any changes due to the exception.
	transaction.RollBack()
	sys.exit(0)
		
#Once the changes are made, we need to use the Commit() method to end the transaction. This will save all the changes back to Revit
transaction.Commit()