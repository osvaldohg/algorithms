print "merge_sort_oz_list"

def merge_sort(arreglo):
    
    if len(arreglo) >1:
        mid=len(arreglo)/2
        
        left=arreglo[:mid]
        right=arreglo[mid:]
        
        merge_sort(left)
        merge_sort(right)
        merge(arreglo,left,right)
        
def merge(arreglo, left, right):
    k=0
        
    while left and right:
        if left[0] < right[0]:
            arreglo[k]=left.pop(0)
            
        else:
            arreglo[k]=right.pop(0)
            
        k+=1
        
    while left:
        arreglo[k]=left.pop(0)
        k+=1
        
    while right:
        arreglo[k]=right.pop(0)
        k+=1
        
    return arreglo
      
#main

test= [54,26,93,17,77,31,44,55,20]
merge_sort(test)
print test
