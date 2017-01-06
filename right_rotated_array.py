
def right_rotated_array(arr, num_rotations):
    size = len(arr)
    rotated_arr = [0]*size
    for i in range(size):
        rotated_arr[(i + num_rotations)%size] = arr[i]
    return rotated_arr

arr = [1, 2, 3]

print right_rotated_array(arr, 0)    # [1, 2, 3]
print right_rotated_array(arr, 1)    # [3, 1, 2]
print right_rotated_array(arr, 2)    # [2, 3, 1]
print right_rotated_array(arr, 3)    # [1, 2, 3]