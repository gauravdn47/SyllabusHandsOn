# Demonstrate slicing of tuple
Name = ("Arjun","Akshay","Krishna","Karan")
Age = (24,43,34,54)
print(Name[0])
print(Name[0:2])
print(Name[-1])
print(Name[0:])
print(Name[:len(Name)])
print(Name[-0:-1])
print(Age[0])
print(Age[0:2])
print(Age[-1])
print(Age[0:])
print(Age[:len(Age)])
print(Age[-0:-1])

# Demonstrate d[1]='w', demonstrate built-in fun on Strings
d = "a","b","c","d","e","f"
print(d[1])
print(d[4])
print(d[0:3])
print(d[0:len(d)])
print(d[:len(d)])
print(d[0:])
print(d[0:-1])
print(d[:-len(d)])

# Slice a List and convert it to a set
lst = ["apple","banana","orange","cherry","mango"]
print(lst)
sat = set(lst[0:3])
print(sat)
print(type(sat))

# What are some properties of Frozen sets? Demonstrate
lst = ["apple","banana","orange","cherry","mango"]
sat = frozenset(lst)
print(sat)
print(type(sat))

# it freezes the elements and make them unchangeable
# you can't add, remove and do data slicing with frozen sets

# Name 5 built-in function on list and tuples both
# 5 built-in function on tuple
lst =  ["apple","banana","orange","cherry","mango"]
tple = (1,2,9,8,6,7,5,4,3)
print(sorted(tple))
print(type(tple))
print(len(tple))
print(max(tple))
print(min(tple))

# 5 built-in function on list
print(sorted(lst))
print(type(lst))
print(len(lst))
print(max(lst))
print(min(lst))
lst.append("kiwi")
print(lst)
lst.remove("kiwi")
print(lst)
lst.insert(3,"berry")
print(lst)
del lst[3]
print(lst)

# Store 3 tuples in another tuple and print it in reverse
tpl1 = (1,2,3)
tpl2 = ("shekhar","raj")
tpl3 = (2.0,3.2,5.3)

tple = tpl1 + tpl2 + tpl3
print(tple[::-1])

# Can a set can hold duplicate Values? Demonstrate
sat = {11,2,10,11,10,3,4,5,6,6,5,5,5}
print(sat)
print(type(sat))

# Therefore sets cannot store duplicate values

# Demonstrate get(), items() , values() and keys()
students = {"Ram":26,"Shyam":24,"Satyam":30,"Sundaram":28}
print(students)
print(type(students))
print(students.items())
print(students.values())
print(students.keys())
print(students.get("Satyam"))

# Convert Immutable dict to a dict
# Demonstrate unpacking of a tuple

a = ("MNNIT Allahabad", 5000, "Engineering")
(college, student, type_of_college) = a

print(college)
print(student)
print(type_of_college)
