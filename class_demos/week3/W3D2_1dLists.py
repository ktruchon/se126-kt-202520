#W3D1 - Introduction to Lists

#PROGRAM PROMPT: *This is continuation of Lab #2* Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.


#This file utilizes: filehandling.csv


#--IMPORTS---------------------------------------------------------------
import csv


#--FUNCTIONS-------------------------------------------------------------


#--MAIN EXECUTING CODE---------------------------------------------------

#CREATE AN EMPTY LIST for every *potential* field in the file
#always base your number of lists on the longest record ie the one with the most field data
compType = []       #computer type -> D or L
manu = []           # manufacturer -> DL, GW, or HP
proc= []            #processor type
ram = []            #total RAM
hd_1 = []           #hard drive #1 

num_hd = []         #number of hard disk drives -> 1 or 2

hd_2 = []           #hard drive #2 * even though not all records have this, still creating an empty list
os = []             #operarting system
yr = []             #machine year



#create a var to count the total number of records in the file
#total_rec = 0

#connecting to the file
with open("text_files/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        #this loop will occur for every record in the file
        
        #FIELD 1 - rec[0] - computer type
        #from Lab #2:
        if rec[0] == "D":
            compType.append("Desktop")
        else:
            compType.append("Laptop")
        
        #FIELD 2 - rec[1] - manufacturer type
        if rec[1] == "DL":
            manu.append("Dell")
        elif rec[1] == "GW":
            manu.append("Gateway")
        elif rec[1] == "HP":
            manu.append("HP")
        else: #optional if the file is too long to review first
            manu.append("*ERROR*")
            
        #FIELD 3 - rec[2] - processor
        proc.append(rec[2])        
        #FIELD 4 - rec[3] - ram size
        ram.append(rec[3])
        
        #FIELD 5 - rec[4] - first hard drive size
        hd_1.append(rec[4])
        
        #FIELD 6 - rec[5] - number of hard drives
        num_hd.append(int(rec[5]))
        
        #FIELD 7, 8, 9 are based on int(rec[5])
        if int(rec[5]) == 1:
            hd_2.append("---")     #no second disk here since rec[5] is a 1!
            os.append(rec[6])      #next field is the OS
            yr.append(rec[7])          #final field is the year
        else:
            hd_2.append(rec[6])    #rec[5] != 1, so there is a second drive/extra record
            os.append(rec[7])      #next field is the OS
            yr.append(rec[8])           #final field is the year
            
            
        #one print for all of the records, regardless of size
        #print(f"{comp:10}{manufacturer:10}{processor:5}{ram_size:5}{hardDrive_1:10}{str(no_of_hardDrives):10}{hardDrive_2:10}{operating:5}{year:5}")
        
        #total_rec += 1
            
#disconnected from file



#process data from lists using a FOR loop *after* you are no longer connected to the file

#just printing
#field headers print for final display of all parallel list data
print(f"{'COMPTYPE':10}{'BRAND':10}{'PROC':5}{'RAM':5}{'HD#1':10}{'No.HDD':10}{'HD#2':10}{'OS':5}{'YEAR':5}")
print("---------------------------------------------------------------------------")
for i in range(0, len(compType)):
    print(f"{compType[i]:10}{manu[i]:10}{proc[i]:5}{ram[i]:5}{hd_1[i]:10}{str(num_hd[i]):10}{hd_2[i]:10}{os[i]:5}{yr[i]:5}")
print("---------------------------------------------------------------------------")
#counting for desktops and laptops that are old
old_desk = 0        #from 2016 or earlier
old_lap = 0
for i in range(0, len(yr)):
    if int(yr[i]) <= 16: #too old
        print(f"old machine found on index {i}")
        if compType[i] == "Desktop":
            old_desk += 1

#final counts display
print(f"\nTotal no. of desktops that need to be replaced: {old_desk} Cost: ${old_desk * 2000:.2f}")

print(f"\nTOTAL RECORDS IN FILE: {len(compType)}\n\nThank you, Goodbye.")