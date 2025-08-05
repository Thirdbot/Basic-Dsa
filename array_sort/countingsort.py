def countingsort(array):
    
    max_val = max(array)
    
    space = [0] * (max_val+1)
    
    while len(array) > 0:
        num = array.pop(0)
        space[num] += 1
        
    for i in range(len(space)):
        while space[i] > 0:
            array.append(i)
            space[i] -= 1
    
    return array

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = countingsort(unsortedArr)
print("Sorted array:", sortedArr)