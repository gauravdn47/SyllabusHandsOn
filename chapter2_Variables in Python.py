# Differentiating between a valid and Invalid Identifiers
# Assigning a value to a variable
'''
for = 5 # invalid since 'for' is a keyword
'''
foo = 5 # valid since foo is not a keyword


# Name some types of Values, what function to check the type of a variable

# Integer
foo = 5
type_of_foo = type(foo)
print(type_of_foo)

# String
foo = '5'
type_of_foo = type(foo)
print(type_of_foo)

# Boolean
foo = True
type_of_foo = type(foo)
print(type_of_foo)

# Float
foo = 5.00
type_of_foo = type(foo)
print(type_of_foo)

# Complex number
foo = 5+6j
type_of_foo = type(foo)
print(type_of_foo)