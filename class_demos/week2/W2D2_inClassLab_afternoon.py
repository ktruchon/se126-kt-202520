#W2D2 - Text File Handling Review

#PROGRAM PROMPT:


#VARIABLE DICTIONARY:


#--IMPORTS-----------------------------------------------
import csv
#--FUNCTIONS---------------------------------------------
def difference(people, max_cap):
    '''This function is passed 2 values and returns the difference between them'''
    diff = max_cap - people 
    return diff #this value will replace the difference() call in the main code

#--MAIN EXECUTING CODE-----------------------------------

#initialize needed counting vars
total_rec = 0 
rooms_over = 0

#-----connected to file-----------------
print(f"\n\n{'NAME':20}     {'MAX':5}   {'PPL':5}   {'OVER':5}")
print("--------------------------------------------------------")
with open("text_files/classLab2.csv") as csvfile:
    #we must indent one level while connected to the file 
    file = csv.reader(csvfile)
    for rec in file: 
        #below code occurs for every record (row) in the file (text file -> 2D list!)
        #assign each field data value to a friendly var name
        name = rec[0]
        max = int(rec[1])   #all text data read as a string, so cast as a num!
        ppl = int(rec[2])
        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display the rooms that are over capacity (remaining is negative)
        if remaining < 0 :
            rooms_over += 1
            print(f"{name:20}   {max:5}   {ppl:5}   {remaining * -1:5}")
        
        #count ALL rooms! 
        total_rec += 1
#-----disconnected from file-------------
#display final data (counting vars)
print(f"\nRooms currently OVER capacity: {rooms_over}")
print(f"Total rooms in the file: {total_rec}")