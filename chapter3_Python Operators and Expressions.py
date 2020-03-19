# Expressions vs Statements

# Expression
4 + 5
4 * 9
True
False

# Statements
# If Condition

# Converting int to str and vice-versa
x = 5
type_of_x = type(x)
print(type_of_x)
y = str(x)
type_of_y = type(y)
print(type_of_y)

a = '5'
type_of_a = type(a)
print(type_of_a)
b = int(a)
type_of_b = type(b)
print(type_of_b)

# Comparing output of '/' and '//'
x = 5
y = 2
Division = x/y
print("The division output is:",Division)

x = 5
y = 2
Division = x//y
print("The division output is:",Division)

# Demonstrating Manual approach of bitwise operation
print(~12) # Bitwise Ones' Compliment operator

a = 12
b = 13
c = a & b # Bitwise AND Operator
print(c)

a = 12
b = 13
c = a | b # Bitwise OR Operator
print(c)

a = 10
b = 7
c = a ^ b # Bitwise XOR Operator
print(c)

a = 10
b = 2
c = a << b # Bitwise Left Shift Operator
print(c)

a = 10
b = 1
c = a >> b # Bitwise Right shift Operator
print(c)


