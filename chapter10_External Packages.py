# How to combine many series to form a dataframe?
import pandas as pd
ser1 = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
ser2 = pd.Series([6,7,8,9,10], index=['a','b','c','d','e'])
print(ser1,ser2)
data = pd.DataFrame({'a':ser1,'b':ser2, 'idx_col': ser1.index})
print(data)

# Writing program to demonstrate deep and shallow copy
import copy
old_list = [[1,2,3],[4,5,6],[7,8,9]]
new_list = copy.copy(old_list)
new_list[0] = ['a','b','c']

print("Old_List",old_list)
print("New_List",new_list)

new_list1 = copy.copy(old_list)
new_list1[0][2] = 'c'
print("Old_List",old_list)
print("New_List1",new_list1)

new_list2 = copy.deepcopy(old_list)
new_list2[0][2] = 'c'
print("Old_List",old_list)
print("New_List2",new_list2)

# Replace items that satisfy a condition with another value in numpy array
import numpy as np

a = np.random.randint(0,5, size=(5,4))
print(a)
b = a<3
print(b)
c = (a<3).astype(int)
print(c)