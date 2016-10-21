print "merge_sort_oz"

def merge_sort(arreglo):
    
    if len(arreglo) >1:
        mid=len(arreglo)/2
        
        left=arreglo[:mid]
        right=arreglo[mid:]
        
        merge_sort(left)
        merge_sort(right)
        merge(arreglo,left,right)
        
def merge(arreglo, left, right):
    i,j,k=0,0,0
        
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arreglo[k]=left[i]
            i+=1
        else:
            arreglo[k]=right[j]
            j+=1
        k+=1
        
    while i <len(left):
        arreglo[k]=left[i]
        i+=1
        k+=1
        
    while j <len(right):
        arreglo[k]=right[j]
        j+=1
        k+=1
        
    return arreglo
      
#main

test= [44,23,23,57,7,11,43,25,32]
merge_sort(test)
print test
