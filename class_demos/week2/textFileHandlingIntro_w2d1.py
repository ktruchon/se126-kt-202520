from os import system, name 

def clear():
    if name == 'nt':#for windows
        __ = system('cls')
    else:#for linux and mac
        __ = system('clear')


clear()

#When reading a text or csv file directly, it is treated as a 2D list: a list (textFile) where every value is another list ([name, number, color])
textFile = [
    #lists are represented with [] and , separated values
    ["Abby", "10", "red"], #this is the first record or textFile[0]
    ["Bobby", "11", "orange"],
    ["Carol", "12", "yellow"],
    ["David", "13", "green"],
    ["Elise", "14", "blue"],
    ["Frank", "15", "indigo"],
    ["George", "16", "violet"]
]

print(textFile)         #entire 2D textfile; notice the multiple []s 
print(textFile[0])      #first record in 2D textFile 
print(textFile[0][0])   #first value of first record in 2D textFile

#this print() just gives headers before we enter the loop
print(f"{'NAME'}\t{'NUM'}\t{'COLOR'}")
print("-----------------------------------")

#below the for loop will run for as many records (1D lists) as found within textFile (a 2D list)
#'record' is simply the name we are giving to each item within the greater iterable 
for record in textFile:
    
    #we can view the enrire record as a list:
    print(record)
    
    #but we need to be able to access individual values in the list, so
    #we could simply view the values directly:
    print(f"{record[0]}\t{record[1]}\t{record[2]}")
    
    #or we could store to variables if more comfortable
    name = record[0]
    number = record[1]
    color = record[2]
    
    print(f"{name}\t{number}\t{color}")
    
    
print("And that's how a for loop accesses text file data!")

input("Press enter for next part of demo...")

clear()

#import the csv library for access to csv.reader()
import csv 

#point to the appropriate file and store the path as a friendly name 'csvfile'
with open("text_files/simple.csv") as csvfile:
    
    #have the processor read and store the data found at the 'csvfile' path to the 2D list called 'file' 
    file = csv.reader(csvfile) 
    
    #for every 'record' (row) in the 'file':
    for record in file:
        
        #we can view the enrire record as a list:
        print(record)
        
        #but we need to be able to access individual values in the list, so
        #we could simply view the values directly:
        print(f"{record[0]}\t{record[1]}\t{record[2]}")
        
        #or we could store to variables if more comfortable
        name = record[0]
        number = record[1]
        color = record[2]
        
        print(f"{name}\t{number}\t{color}")