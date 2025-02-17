#BINARY SEARCH: 
#               * requires a collection of UNIQUE values to search through
#               * requires the collection to be SORTED (ORDERED)
#                       ascending or descending ; alpha or numeric

name = ["Austin", "Cory", "Noah", "Justyn", "Andrew", "Matt", "Rob", "Ray"]
fave_color = ["blue", "red", "green", "red", "blue", "green", "grey", "black"]


for i in range(0, len(name) - 1):#outter loop

    for index in range(0, len(name) - 1):#inner loop
        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing
        if(name[index] > name[index + 1]):

            #if above is true, swap places!

            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp

            #swap all other values - you could also handle swapping with a function!
            temp = fave_color[index]
            fave_color[index] = fave_color[index + 1]
            fave_color[index + 1] = temp


#BINARY SEARCH - the searching loop will only work if we first ORDER the name list!
search = input("Enter the NAME you are looking for: ")

min = 0 
max = len(name) - 1
mid = int((min + max) / 2)

while min < max and search != name[mid]:
    if search < name[mid]:
        max = mid - 1
    else:
        #search > name[mid]
        min = mid + 1
    
    mid = int((min + max) / 2)  

if search == name[mid]:
    print(f"Your search for {search} is complete, see details below:") 

    print(f"\t{'NAME':10}  {'FAVE COLOR'}")
    print(f"-----------------------------------------------")
    print(f"\t{name[mid]:10}  {fave_color[mid]}")
    print(f"-----------------------------------------------")
else:
    print(f"Your search for {search} came up empty :[")