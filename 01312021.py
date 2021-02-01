
#this is for PRACTICE only.
#ONLY meaningful to the owner.

import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

a_mul_b = a * b
a_plus_b = a + b
a_minus_b = a - b
a_div_b = a / b
a_pow_b = a ** b

import numpy as np
a = np.array([1,2,3],dtype='int32')
print(a)

b = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='int16')

ndim
dtype
itemsize
nbytes

c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
c

#get a specific element[r, c]
c[1,2]

#specific row
c[0,:]

#getting a little more fancy [startindex:endindex:stepsize]
c[0, 1:6:2]

#Get specific element (work outside in)
#first one - #th set
# middle one - #th array of set
#thrid one - #th item of array of set

b[1,0,:]


#all 1s matrix
np.ones((4,2,2), dtype='int32')

#any other number
np.full((3,3), 77, dtype='float32')
