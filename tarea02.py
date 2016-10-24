print "merge_sort_oz"
inv=0
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
    global inv    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arreglo[k]=left[i]
            i+=1
        else:
            arreglo[k]=right[j]
            j+=1
            inv+=len(left)-i
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

#test= [44,23,23,57,7,11,43,25,32]
test=[1,5,3,2,4,6]
test2=[1,3,5,2,4,6]
#merge_sort(test2)
#print test
#print "this is",inv

fh=open("sample.txt","r")
superlista=list()
for line in fh:
    #print line.strip()
    superlista.append(int(line))

#print superlista
merge_sort(superlista)
print superlista
print "this is inv",inv
