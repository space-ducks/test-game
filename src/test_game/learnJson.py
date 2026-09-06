#import module for json
import json
#functions of the json module are as follows
#json.dumps(): Converts a Python object to a JSON string
#json.loads(): Parses a JSON string and returns a Python object
#json.dump(): Writes a Python object to a JSON file
#json.load(): Reads a JSON file and returns a Python object

#from calls the module import calls the specific part
from pathlib import Path

#create test integer
testNumber = 1

#with as notation
# open allows to access a file
# w writes, r reads

#path allows file placement in relative locations 
#returns as an absolute file path within the program
#__file__ is the file path currently opened, in this case learnJson.py
#parent is the folder directly prior (parent folder)

#path is a variable type
#saves the file path as filePath
filePath = Path(__file__).parent / 'testFile.json'

#opens filePath and dumps into json file

json.dump(testNumber, open(filePath, 'w'))

#  dump writes to the file
#  load pulls from the file

saveData=json.load(open(filePath, 'r'))

print (saveData)


#character name
#level number
#3 items
#current health

saveFile = {
    "Character Name":"Default",
    "level": 0,
    "items": ["potion", "sword", "shield"],
    "current health": 100,
}

savePath = Path(__file__).parent / 'saveFile.json'
json.dump(saveFile, open(savePath, 'w'))

savePath=json.load(open(savePath, 'r'))
print(savePath)