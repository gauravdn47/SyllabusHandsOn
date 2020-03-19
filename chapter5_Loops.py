# Calculation and printing Fibonacci Series till nth term
n = int(input("Enter a Number :"))
a = 0
b = 1
if n>0:
    if n == 1:
        print(a)

    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)


# Identifying Armstrong numbers within a given range
x = int(input("Enter a range of number"))
for i in range(x):
    num = i
    result = 0
    n = len(str(i))
    while(i != 0):
        digit = i % 10
        result = result + digit ** n
        i = i//10
    if num==result:
        print(num)

# Checking if a given number is an Armstrong number
x = int(input("Enter a number"))
num = x
result = 0
n = len(str(x))
while (x != 0):
    digit = x % 10
    result = result + digit ** n
    x = x // 10
if num == result:
    print("The given number is an Armstrong Number")
else:
    print("The given number is not an Armstrong number")



