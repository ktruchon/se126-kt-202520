#W8D2 - Dictionary Review + Gaining Data from Text Files
#this demo utilizes: dictionary_file.csv

#---IMPORTS-------------------------------------------------------------
import csv 
#---MAIN EXECUTING CODE-------------------------------------------------
library = {
    #'key' : value
    "1230" : "Red Rising",
    "1231" : "The Little Prince"
}

with open("text_files/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        #for every record in the file, do the following
        #file --> 2D list; rec --> 1 record's data, also a list!
        library.update({rec[0] : rec[1]})
        #libary_num --> rec[0], a string
        #title --> rec[1], also a string

#disconnected from file------------------------------

print(f"{'KEY':4} : {'TITLE'}")
print("-" * 50)
for key in library:
    #for every key found in the library dictionary
    print(f"{key.upper():4} : {library[key]}")
print("-" * 50)

#--SEQUENTIAL SEARCH with DICTIONARIES-----------
search = input("\nEnter the LIBRARY NUM you are looking for: ")

found = 0

for key in library:
    if search.lower() == key.lower():
        found = key
    
if found != 0:
    print(f"We found your search for {search}, here is the info: ")
    print("-" * 50)
    '''
    for i in range(0, len(found)):
        print(f"{found[i].upper():4} : {library[found[i]]}")
    '''
    print(f"{found.upper():4} : {library[found]}")
    print("-" * 50)
else:
    print(f"We could not find your search for {search} :[ ")