new_array = [12,34,54,2,3]



def shellsort_itr(array):
    
    n = len(array)
    mid_range = n // 2
    
    while (mid_range > 0):
        
        for i in range(mid_range,n):
            temp = array[i]
            j = i
            
            while j >= mid_range and array[j-mid_range] > temp:
                array[j] = array[j-mid_range]
                j -= mid_range
            array[j] = temp
        
        mid_range = mid_range // 2
    return array


print(shellsort_itr(new_array))