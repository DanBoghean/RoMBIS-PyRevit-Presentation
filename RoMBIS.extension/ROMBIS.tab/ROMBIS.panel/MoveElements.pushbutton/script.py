__title__ = "Move Elements"
__doc__ = "Move selected elements 3' in the Y direction using the Revit API"

#import the .NET common language runtime to allow us to use the necessary .dll files
import clr

#Add the Revit API Reference to allows us to import elements to work with
clr.AddReference('RevitAPI')

#Add the Revit API UI Reference to allow us to work with the Revit UI Elements
clr.AddReference('RevitAPIUI')

#Once the reference is added, we can import the necessary elements from the Revit API
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from System.Collections.Generic import List

 #__revit__ refers to the Revit Command Data that we can access. Just know that you need the __revit__ instance to be able to access the UI Document
uidoc = __revit__.ActiveUIDocument

#The Revit Document can be accessed as a property of the UI Document
#We define a variable and assign the Document object to so that we can work with it without having to type __revit__.ActiveUIDocument.Document every time
doc = uidoc.Document

###
#ACTIVE SELECTION METHOD
####

#We can access the current selection in Revit by using the Selection property of the UI Document. 
#From there, we can use the GetElementIds() method to create a list of all of the selected element ids and assign it to the selectionIds variable which will become a list 
selectionIds = uidoc.Selection.GetElementIds()

#The MoveElements() method we will be using requires a list of element ids to work on, so we use the List[]() we imported from System.Collections.Generic to create this list
elementList = List[ElementId]()

#To iterate through the list of ids, we create a for loop that goes through the list and assigns it to the id variable until the list is exhausted. 
#This allows us to work with each element in the list indvidually.
for id in selectionIds:
	
	#The List element uses an Add() method to add elements to the list, so we use that here to add the ids of the elements we selected
	elementList.Add(id)
	
#Once the list of element ids is created for all the elements we want to move, we first need to create a Transaction in Revit.
#Any time that we change anything within Revit, we must use a Transaction to encompass that change. This will also correspond to the Undo/Redo actions for everything contained in the Transaction
transaction = Transaction(doc, "Move Element")

#After the Transaction object is created, we have to call the Start() method in order to initate the transcation to make any changes
transaction.Start()

#Revit gives us access to a class called ElementTransformUtils. This has methods such as MoveElements, RotateElements, and CopyElements. 
ElementTransformUtils.MoveElements(doc, elementList, XYZ(0, 3, 0))

#Once the changes are made, we need to use the Commit() method to end the transaction. This will save all the changes back to Revit
transaction.Commit()