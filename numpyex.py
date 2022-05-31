import numpy as np
new_arr = np.array([1, 2, 3, 4, 5, 6])
print(new_arr[1:4])
print(new_arr[3:])
print(new_arr[:3])
print(new_arr[-4: -1])

print(new_arr[1:4:2])

# Slice 2-d
new_arr = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]])
print(new_arr[1, 1:4])
