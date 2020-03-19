# Building a basic calculator application
operation = input(""" Enter the Math operation you want to calculate :
'+' for addition
'-' for subtraction
'*' for multiplication
'/' for division
""")

num1 = int(input("Enter your first number :"))
num2 = int(input("Enter your second number :"))

if operation == '+':
    num = num1 + num2
    print("{} + {} = {} ".format(num1,num2,num))

elif operation == '-':
    num = num1 - num2
    print("{} - {} = {} ".format(num1,num2,num))

elif operation == '*':
    num = num1 * num2
    print("{} x {} = {} ".format(num1,num2,num))

elif operation == '/':
    num = num1 / num2
    print("{} / {} = {} ".format(num1,num2,num))

else:
    print("Entered operator is not valid, Please enter the valid operator")


# Demonstrating one line if by writing a program for greatest of 3 numbers

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a>b>c:
    print("a is greater")
elif a<b>c:
    print("b is greater")
else:
    print("c is greater")


# Re-write program for calculator application applying switch case functionality in Python

