    
import csv

totalRecs = 0 #the total number of records (rows) in the file
overCount = 0

#STEP 2:
#connecting to the file's path - switch \ to /
#-----connected to file--------------------------------------------

with open("text_files/classLab2.csv") as csvfile:
    print(f"\n{'NAME':15} \t {'MAX':3} \t {'CURRENT':3} \t OVER")
    print("----------------------------------------------------")

    file = csv.reader(csvfile)

    for rec in file:

        totalRecs += 1

        name = rec[0]
        max = rec[1]
        current = rec[2]


        if max < current:

            overCount += 1
            max = int(max)
            current = int(current)
            diff = (max - current) * -1
           
            print(f"{rec[0]:15} \t {rec[1]:3} \t {rec[2]:3} \t {diff}")

print(f"\nTOTAL OVER: {overCount}")
print(f"TOTAL RECORDS: {totalRecs}")