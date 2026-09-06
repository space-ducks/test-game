#list with stored values 
firstList = [1,2,3,4,5,6,7,8,9,10]

print(firstList[0:9:2])
#prints the first 10 elements of the list, starting at index 0 (INCLUSIVE) and taking every 2nd element
#Inclusive for the first number and not inclusive for the second number
#list can include different data types, including strings, integers, and booleans

#List allows duplicate numbers, it is ordered and changeable
#ordered means that the items have a defined order, and that order will not change
#changeable means that we can change, add, and remove items in a list after it has been created


#dictionary test
#ordered, changeable, and does not allow duplicates

dict1 = {
    "noah": 1, "orange", 33,
    "randy": 2, "blue", 22,
}

#key includes values on the left
#calling noah or randy will return the value on the right
#can be helpful for storing information for to be called later
