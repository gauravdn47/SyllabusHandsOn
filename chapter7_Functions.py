# Rewriting Calculator program using method based approach
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def Multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("""Enter the valid operation from the following :
1 : Addition
2 : Subtraction
3 : Multiplication
4 : Division """)

select = input("Please select the operation :")
number1 = int(input("Enter the first number :"))
number2 = int(input("Enter the second number :"))

if select == "1":
    print(number1,"+",number2, "=",add(number1,number2))
elif select == "2":
    print(number1,"-",number2, "=",subtract(number1,number2))
elif select == "3":
    print(number1,"x",number2, "=",Multiply(number1,number2))
elif select == "4":
    print(number1,"/",number2, "=",divide(number1,number2))
else:
    print("Invalid Input")

# Writing a boolean method and executing in loop to identify Armstrong numbers in an array
from array import *
arr = array('i',[10,4,11,5,153,216,])
print(arr)
print(type(arr))

for i in arr:
        num = i
        result = 0
        n = len(str(i))
        while (i != 0):
            digit = i % 10
            result = result + digit ** n
            i = i // 10
        if num == result:
            print(True)
        else:
            print(False)

# Rewriting Fibonacci Series using method based approach

def fibo(n):
    a = 0
    b = 1
    if n > 0:
        if n == 1:
            print(a)

        else:
            print(a)
            print(b)
            for i in range(2, n):
                c = a + b
                a = b
                b = c
                print(c)
fibo(5)

# Changing default search path for modules
sys.path.append('/path/to/search')
