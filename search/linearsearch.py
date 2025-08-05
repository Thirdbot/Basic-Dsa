def linearsearch(arr,target):
    
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1

arr = [3, 7, 2, 9, 5]
targetVal = 9

result = linearsearch(arr, targetVal)

if result != -1:
    print("Value",targetVal,"found at index",result)
else:
    print("Value",targetVal,"not found")