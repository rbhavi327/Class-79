import numpy as np
array =[0,1,2,3,4,5,6,7,8,9]
data_type=[('number',int)]
array_orig = np.array(array,dtype=data_type)
print("Original array:")
print(array)
array2 = array
for i in range(1,9,2):
    array2[i] = -1

print("\n Modified array:")
print(array2)

print("\n Shape change:")
print(array_orig.reshape(2,5))