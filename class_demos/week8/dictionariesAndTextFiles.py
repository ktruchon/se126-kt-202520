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

min = 0 
max = len(library_nums) - 1
mid = int((min + max) / 2)

while min < max and search != library_nums[mid]:
    if search < library_nums[mid]:
        max = mid - 1
    else:
        min = mid + 1
    mid = int((min + max) / 2)

if search == library_nums[mid]:
    print(f"We found your search for {search}, see details below: ")
    print(f"\nKEY:{library_nums[mid]:6}\tTITLE:{library[library_nums[mid]]}")
else:
    print(f"We could not complete your search for {search} :[")
    