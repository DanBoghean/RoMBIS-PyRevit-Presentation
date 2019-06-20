__title__ = "Read/Set Filled\nRegion Parametesr"
__doc__ = "This will read the Area parameter of all Filled Regions \
and then Set the value to the Comments parameter."

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

#We can gather all of the filled regions in the project by using a FilteredElementCollector and the OfClass() method
fec = FilteredElementCollector(doc).OfClass(FilledRegion)

	
#Since we will be editing the elemnts in Revit we need to first create a Transaction within Revit. A Transaction must always be created before you make any changes within Revit. It requires the Document and Transaction Name as arguments. The Transaction Name is what will show up in the Undo/Redo dropdown
transaction = Transaction(doc, "Set Comments Parameter")

#Once the Transaction is created, we have to Start it by using the Start() method
transaction.Start()

#To iterate through the list of filled regions, we create a for loop that goes through the list until the list is exhausted. 
#This allows us to work with each element in the list indvidually.
for element in fec:
	
	#One way to get a parameter from an element is to use the LookupParamter() method. This requires a string argument which is the name of the paramter. This should only be used if you can guarantee that there is only one parameter of that name for the element. 
	areaParameter = element.LookupParameter("Area")
	
	print(areaParameter)
	
	#Once the parameter is found, we can access the value of the parameter using different methods depending on the parameter storage type. 
	
	print(areaParameter.StorageType)
	
	#In this case, the Area parameter is stored as a Double so we can access it using the AsDouble() method.
	area = areaParameter.AsDouble()
	
	print(area)

	#The better way to access parameters is using the BuiltInParameter enumeration. This allows you to access any built-in parameters and know what you will not get any conflicting parameters if they exist with the same name. You can also use the GUID of a parameter to access it.
	commentsParameter = element.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
	
	print(commentsParameter)
	
	#Now that we are in the transaction, we can take the commentsParameter variable we assigned previously and assign it using the Set() Method with the area value we extracted. We need to encapsulate the area in a str() method to explicitly tell the Set method that we are writing a string.
	commentsParameter.Set(str(area))
	
#When the edit is completed, you can finish the transaction by using the Commit() method. This will make sure all of the changes are made to the element
transaction.Commit()
