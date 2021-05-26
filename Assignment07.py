# ---------------------------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickling and structured error handling
# ChangeLog (Who,When,What):
# SaraONeal,5.25.2021,Created script
# SaraONeal,5.25.2021,Added code from Assignment 5 to demonstrate error handling in assignment 7
# SaraONeal,5.25.2021,Added code to demonstrate pickling in assignment 7
# ---------------------------------------------------------------------------------------------- #


# -- Module05 Data -- #
# declare variables and constants
File = "ToDoList.txt"   # An object that represents a file -- purposely left off "str" to cause NameError
objFile = None  # file handle
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Module05 Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

#  Error Handling - Example 1 (NameError)
try:
    print("Load data from ToDoList text file into python list of dictionary rows: \n")
    objFile = open(strFile, "r")
    for row in objFile:
        lstRow = row.split(",")  # split() returns a list object
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        lstTable.append(dicRow)
        print(lstTable)  # List with dictionary objects
    objFile.close()

except NameError as e:
    print("Please define a local or global variable")
    print("Built-in Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-in Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

print()

#  Error Handling - Example 2 (IndexError)
try:
    print("Load data from ToDoList text file into python list of dictionary rows: \n")
    objFile = open(File, "r")
    for row in objFile:
        lstRow = row.split(",")  # split() returns a list object
        dicRow = {"Task": lstRow[0], "Priority": lstRow[14].strip()}
        lstTable.append(dicRow)
        print(lstTable)  # List with dictionary objects
    objFile.close()

except IndexError as e:
    print("Index value must be within range")
    print("Built-in Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-in Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

print()

#  Error Handling - Example 3 (Raise Customer Error when negative value is entered by user)
try:
    print("Type in a 'negative value' for your household item")
    strValue = float(input('Enter an estimated value: '))
    if strValue < 0:
        raise Exception('Do not enter a negative value for the estimated value of the household item')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-in Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

print()

#  Pickling - Example 1

#  Import pickle module
import pickle

#  Add dictionary items to Python object
dicObj = {'ID': 1, 'Name': 'Sue', 'Grade': 'A'}
print(dicObj)

#  Store data with pickle.dump method
fileObj = open('PicklingExample1.dat', "ab")
pickle.dump(dicObj, fileObj)
fileObj.close()

#  Script pauses for user to review PicklingExample.dat file
input('Review data stored in the PicklingExample1.dat file now. Press enter to load data back with pickle.load method.')

#  Read the data back with pickle.load method
fileObj = open("PicklingExample1.dat", "rb")
fileObjData = pickle.load(fileObj)  # Load() only loads one row of data
fileObj.close()

print(fileObjData)