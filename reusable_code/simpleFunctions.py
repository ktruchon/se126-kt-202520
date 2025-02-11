#a file with some simple functions i utilize often in class code


#--CLEAR SCREEN FUNCTION-----------------------------------------
from os import system, name #required!

def clear():
    if name == 'nt':#for windows
        __ = system('cls')
    else:#for linux and mac
        __ = system('clear')
        
#--INPUT CHECKS-------------------------------------------------
#simple version with an error trap loop
ans = input("Would you like to enter the search program? [y/n]").lower()

#validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the search program? [y/n]").lower()
#--------------------------------------
#using lists to our advantage
print("\tSEARCHING MENU")
print("1. Search by TYPE") #shows all of either elf or dragon
print("2. Search by NAME") #binary search review
print("3. Search by MEANING") #find part of a whole
print("4. EXIT")

search_type = input("\nHow would you like to search today? [1-4]: ")

#using 'not in' for user validity checks
if search_type not in ["1", "2", "3", "4"]:
        print("***INVALID ENTRY!***\nPlease try again")
else:
    print("..do some code in here based on the menu option....")


#--SWAPPING for BUBBLE SORT--------------------------------------
def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp


#--DISPLYING from LISTS-------------------------------------------
#to test the function below, use the 'party.csv' file to populate the lists

def display(x, foundList, records):
    '''
        PARAMETERS:
        -x       signifier for if we are printing a single record or multiple
                when x != "x" it is an index and we have one value, otherwise we have multiple

        -records the length of a list we are going to process through (# of loops/prints)

        -foundlist is a list passed to the function when using sequential searchfor multiple returns - when it is populated, it contains a list of index positions
    '''
    print(f"{'CLASS':8}  {'NAME':10}  {'MEANING':25}  {'CULTURE'}")
    print("----------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{class_type[x]:8}  {name[x]:10}  {meaning[x]:25}  {culture[x]}")

    elif foundList:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{class_type[foundList[i]]:8}  {name[foundList[i]]:10}  {meaning[foundList[i]]:25}  {culture[foundList[i]]}") 
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{class_type[i]:8}  {name[i]:10}  {meaning[i]:25}  {culture[i]}")

    print("----------------------------------------------------------------\n")

