seats = [
    ["A", "B", "C", "D"],
    ["A", "B", "C", "D"],
    ["A", "B", "C", "D"],
    ["A", "B", "C", "D"],
    ["A", "B", "C", "D"],
    ["A", "B", "C", "D"],
    ["A", "B", "C", "D"]
]

valid_rows = [1, 2, 3, 4, 5, 6, 7]
valid_seats = ["A", "B", "C", "D"]

def display():

    print("ROW\tA\tB\t\tC\tD")
    print("------------------------------------------------------")
    for i in range(len(seats)):
        print(f"{i + 1}\t", end="")
        for x in range(len(seats[i])):
            print(f"{seats[i][x]}\t", end="")
            if x == 1:
                print("\t", end="")
        print()
    print("-----------------------------------------------------")

display()

row = input("Enter the row you wish to sit in [1-7]: ")
if row.isdigit() and int(row) in valid_rows:
    print("yippee")


dummy = "A"
