#quicksort_oz

print "quiksort"

def quicksort(arreglo, n):
    if n==1:
        return arreglo
    
    pivot=partition(arreglo[0],n)
    quicksort(arreglo, start,pivot-1)
    quicksort(arreglo, pivot+1,end)
    
    
def partition(arreglo,l,r):
    p=arreglo(l)
    i=l+1
    j=l+1
    
    for x in range (j,r):
        if arreglo[x] < p:
            #implement swap
            swap arreglo[j,i]
            i=i+1
            
        
    swap arreglo[l] and arreglo[i-1]
    
