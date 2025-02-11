
name = ["Austin", "Cory", "Noah", "Justyn", "Andrew", "Matt", "Rob", "Ray"]
fave_color = ["blue", "red", "green", "red", "blue", "green", "grey", "black"]


print("ORIGINAL PARALLEL LIST DATA: ")

print(f"\t{'[NAME]'}'s favorite color is {'[COLOR]'}!")
for i in range(0, len(name)):
    print(f"\t{name[i]:10}'s favorite color is {fave_color[i]}!")
#BUBBLE SORT----------------------------------------


for i in range(0, len(name) - 1):#outter loop
    print("OUTER LOOP! i = ", i)

    for index in range(0, len(name) - 1):#inner loop
        print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing

        if(name[index] > name[index + 1]):
            print("\t\t SWAP! ", name[index], "<-->", name[index + 1])
            #if above is true, swap places!

            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp

            #swap all other values
            temp = fave_color[index]
            fave_color[index] = fave_color[index + 1]
            fave_color[index + 1] = temp



#display the sorted list and check that the favorite color still matches the student
print("PARALLEL LIST DATA SORTED BY NAME: ")

print(f"\t{'[NAME]'}'s favorite color is {'[COLOR]'}!")
for i in range(0, len(name)):
    print(f"\t{name[i]:10}'s favorite color is {fave_color[i]}!")