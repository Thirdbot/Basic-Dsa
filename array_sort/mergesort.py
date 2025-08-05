def mergesort(array):
    
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    
    return merge(left,right)


def merge(left,right):
    array = []
    i,j = 0,0
    
    while (i < len(left) and j < len(right)):
        
        if left[i] < right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1
            
    array.extend(left[i:])
    array.extend(right[j:])
    
    return array

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergesort(unsortedArr)
print("Sorted array:", sortedArr)