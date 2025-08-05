my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n):
    sorted_index = i
    for j in range(sorted_index+1,n):
        if my_array[j] < my_array[sorted_index]:
            sorted_index = j
        my_array[i],my_array[sorted_index] = my_array[sorted_index],my_array[i]
print(my_array)