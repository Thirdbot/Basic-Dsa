my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(1,n):
    sorted_index = i
    current_value = my_array[i]
    for j in range(i-1,-1,-1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            sorted_index = j
            
        else:
            break
    
    my_array[sorted_index] = current_value


print(my_array)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

for i in range(1,n):
    inserted_index = i
    current_value = my_array.pop(inserted_index)
    for j in range(i-1,-1,-1):
        if my_array[j] > current_value:
            inserted_index = j
    my_array.insert(inserted_index,current_value)
    
print(my_array)
