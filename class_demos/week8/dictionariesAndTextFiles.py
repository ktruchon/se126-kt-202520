#W8D2 - Dictionaries and Text File Data
#this demo utilizes: dictionary_file.csv [W8 Canvas Module]

#--IMPORTS------------------------------------------------------------
import csv 
#--MAIN EXECUTING CODE------------------------------------------------

#mini review on dictionaries
library = {
    #indexes are STRINGS set by the developer
    #'key' : value
    "1230" : "Red Rising", 
    "1231" : "The Little Prince"
}

library_nums = []

with open("text_files/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #add each record's data as a new key + value pair from the text file
        #key --> rec[0]  ; value --> rec[1]
        library.update({rec[0] : rec[1]})
        #when using .update() --> pass {'key' : value}

        library_nums.append(rec[0])

#disconnect from file 
print(f"\n{'KEY':6}\t{'TITLE'}")
print("-" * 50)
for key in library:
    #for every key (and value) pair found within the 'library' dictionary
    print(f"{key:6}\t{library[key]}")
print("-" * 50)

#SEQUENTIAL SEARCH FOR A TITLE
search = input("\nEnter the TITLE you are looking for: ")
found = 0

for key in library:
    if search.lower() == library[key].lower():
        #store the found title's location in the dictionary --> 
        found = key

if found != 0:
    print(f"\nKEY:{found:6}\tTITLE:{library[found]}")
else:
    print(f"\nYour search for {search} came up empty :[")


#type() returns the class type of the data passed to it
if type(library) is list:
    print("'library' is a LIST")




#BINARY SEARCH for LIBRARY NUMBER (dictionary keys)
#in order to binary search a set of keys you must FIRST ... 
#       1. Store the dictionary into a 2D list
#       2. Sort the 2D list by keys
#       3. Binary search through the 2D list :]

#       1. Store the dictionary into a 2D list
dictList = []

for key in library:
    dictList.append([key,library[key]])
    #in this 2D list: dictList[x][y]
    #                   x --> key value

for i in range(len(dictList)):
    print(dictList[i]) #just printing to prove it has been stored correctly

for x in range(len(dictList)):
    for y in range(len(dictList[x])):
        print(f"{dictList[x][y]}")#just printing to visualize [x][y] from line 70 

