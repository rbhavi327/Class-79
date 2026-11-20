import numpy as np
data_type = [('name','S15'),('class',int),('height',float)]
student_details = [('James',5,48.5),('Kate',7,70.8),('Mark',10,70.6),('Emily',11,75.4)]

students = np.array(student_details,dtype=data_type)
print("Original array:")
print(students)
print("\n")
print("Sort by height:")
print(np.sort(students,order='height'))