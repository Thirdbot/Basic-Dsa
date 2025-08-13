

def bitonicmerge(array,low,cnt,dir):
    if cnt > 1:
        k = cnt // 2
        
        for i in range(low,low+k):
            compAndSwap(array,i,i+k,dir)
            
        bitonicmerge(array,low,k,dir)
        bitonicmerge(array,low+k,k,dir)
        
        
def bitonicsort(array,low,cnt,dir):
    
    if cnt > 1:
        k = cnt // 2
        
        bitonicsort(array,low,k,1)
        bitonicsort(array,low+k,k,0)
        
        bitonicmerge(array,low,cnt,dir)

def compAndSwap(array,i,j,dir):

    if dir == (array[i] > array[j]):
        array[i],array[j] = array[j],array[i]
    



a = [3, 7, 4, 8, 6, 2, 1, 5]

n = len(a)

bitonicsort(a,0,n,1)

print(a)