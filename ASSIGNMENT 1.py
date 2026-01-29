"""
ASSIGNMENT 1

Module 2 : Basic Pyhton Concepts

Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""
#1.  Taking Number From user
first_Number = int(input("Enter your First Number: "))
second_Number = int(input("Enter your Second Number: "))

#2. Performs the basic mathematical operations on these two numbers:
# addition 
add = first_Number + second_Number
# subtraction
sub = first_Number - second_Number
# Multiplication 
mul = first_Number * second_Number
# division
div = first_Number / second_Number

#3. Displays the results of each operation on the screen.
print("Addition: ", add,"\nsubtraction: ",sub,"\nMultiplication: ", mul,"\nDivision: ", div)

"""
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""
#1.  Takes a user's first name and last name as input.
first_Name = input("Enter your first name:")
last_Name = input("Enter your last name:")

#2.  Concatenates the first name and last name into a full name.
full_name = first_Name +" "+ last_Name

#3.  Prints a personalized greeting message using the full name.
print("Hello, ",full_name,"! Welcome to the Python program",sep="")
