#SE126 - Intro to Python Review Practices
#Found in SE126 Canvas > Course Resources > PRACTICE - Control Flow


#---PRACTICE 1: WHILE LOOPS-----------------------------------------------------------------
#1A. Write a program in Python that: asks a user to enter their name.  Once their name has been entered, enter a while loop that prints hello ___(their name)!.  Ask the user if they'd like to see the message again.  Based on their response, allow the loop to repeat itself.  When they no longer respond to see the message again, print them a personalized goodbye message.
print("--PRACTICE 1A----------")

name = input("Enter your name: ")
   
answer = "y" #loop control

while answer == "y":
    print(f"\t Hello {name}!")
    
    #build a way out of the loop - reset the loop control
    answer = input("\t Would you like to see that again? [y/n]: ").lower()

print(f"Goodbye {name}!")



#1. B. Rewrite the above program so that you are printing hello in a while loop, but have it print 5 times (and do not ask the user if they would like to continue again each time)
print("--PRACTICE 1B----------")

name = input("Enter your name: ")
   
count = 0 #loop control

while count < 5:
    print(f"\t Hello {name}!")
    
    #build a way out of the loop - reset the loop control
    count += 1

print(f"Goodbye {name}!")



#1. C. Rewrite the above program again, but before entering the loop ask the user how many times they would like to see the printed message. Based on their response, run the loop the appropriate number of times.  
print("--PRACTICE 1C----------")

name = input("Enter your name: ")
times = int(input("How many times would you like to see your name: "))
   
count = 0 #loop control

while count < times:
    print(f"\t Hello {name}!")
    
    #build a way out of the loop - reset the loop control
    count += 1

print(f"Goodbye {name}!")
 

#---PRACTICE 2: IF/ELSE-----------------------------------------------------------------
#2. Write a program in Python that: asks a user to enter the value of an integer.  Using if and elif statements, print the following based on specific conditions: [NOTE: only ONE of these messages should print for the number entered]

    #If the number is less than 0
    #"This number is negative!"
    #If the number is greater than 100
    #"Woah, this number is greater than 100!"
    #If the number is equal to 7
    #"This is KT's favorite number!"
    #If none of the above, just print the number back to the user
print("--PRACTICE 2A----------")

number = int(input("Enter an integer: "))
 
if number < 0:
    print(f"The number {number} is NEGATIVE!")  
elif number == 7:
    print(f"The number {number} is KT's FAVORITE NUMBER!")
elif number > 100:
    print(f"The number {number} is WOAH THIS NUMBER IS GREATER THAN 100!")
else:
    print(f"The number you entered is {number}!")

 

#3. Rewrite Practice #2 but ask for the number inside of a while loop, and ask the user if they would like to enter a new number before exiting the loop. Once the loop has exited, print the sum total of all of the numbers entered by the user, and then a goodbye message.
print("--PRACTICE 2B----------")

sum_numbers = 0
answer = "y" #loop control

while answer == "y":
    number = int(input("Enter an integer: "))
    
    sum_numbers += number
    
    if number < 0:
        print(f"The number {number} is NEGATIVE!")  
    elif number == 7:
        print(f"The number {number} is KT's FAVORITE NUMBER!")
    elif number > 100:
        print(f"The number {number} is WOAH THIS NUMBER IS GREATER THAN 100!")
    else:
        print(f"The number you entered is {number}!")
        
    answer = input("Would you like to enter another number? [y/n]: ").lower()
    
print(f"The sum of all numbers you entered is: {sum_numbers}\nGoodbye!")