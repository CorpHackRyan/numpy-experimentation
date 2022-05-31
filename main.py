# Experimentation with
import numpy as np

arr = np.array([1,2,3,4,5,6])
print(type(arr), arr)

# Arrays are homogeneous data structures
# All data elements in an array, get converted to the same type
# String takes priority


# To determine the type inside of the array, NumPy provides:
# Attributes of ndarray object
# 1. ndim
# 2. shape
# 3. size
# 4. dtype

emp = [100, 'sakeeb', 10000.5]
dept = [[100, 'sakeeb', 100000.5],
        [101, 'abc', 20000.6],
        [102, 'xyz', 30000.5]]

# Slicing
# arr[startRowPos : endRowPos +1, startColPos : endColPos + 1]

li = [[1,2,3,10],
      [4,5,6,20],
      [7,8,9,30],
      [1,2,3,40]]

arr = np.array(li)

print(arr[1:3, 1:3])
print(arr[[0,3],:])
print(arr[:, [0,3]])
print(arr[[0,3], 1:3])

