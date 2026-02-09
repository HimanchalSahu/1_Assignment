"""
ASSIGNMENT 2: 

Module 3: Control Structures in Python 

Task 1: Check if a Number is Even or Odd 
Problem Statement:  Write a Python program that: 
1.  Takes an integer input from the user.
2.  Checks whether the number is even or odd using an if-else
statement. 
3.  Displays the result accordingly.
 
"""

#Taking input from user
int = int(input("Enter a number: "))

#Cheaking for odd or even number
if int % 2 == 0:
    print(f"{int} is a even number.")
else:
    print(f"{int} is an odd number.")


"""

Task 2: Sum of Integers from 1 to 50 Using a Loop 
Problem Statement: Write a Python program that: 
1.   Uses a for loop to iterate over numbers from 1 to 50. 
2.   Calculates the sum of all integers in this range. 
3.   Displays the final sum.
"""
# Initialize sum variable
sum = 0
# calculating sum
for i in range(1, 51):
    sum += i
    
#displays the final sum
print("The sum of integers from 1 to 50 is:", sum)
