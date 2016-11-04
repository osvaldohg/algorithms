#quicksort_oz
#quicksort using first element as pivot

counter=0
print "quicksort"

def quicksort(arreglo,l,r):
    print "quicksort oz"
    
    if l < r:
        p=partition(arreglo,l,r)
        quicksort(arreglo,l,p-1 )
        quicksort(arreglo,p+1,r)
    
def partition(arreglo,l,r):
    p=arreglo[l]
    
    i=l+1
    j=l+1
    global counter

    for x in range (j,r+1):
        
        counter+=1
        if arreglo[x] < p:
            #swap arreglo[j,i]
            tmp=arreglo[i]
            arreglo[i]=arreglo[x]
            arreglo[x]=tmp
            i+=1

    pivot=arreglo[l]
    arreglo[l]=arreglo[i-1]
    arreglo[i-1]=pivot
    return i-1

def readValues(path):
    fh=open(path,"r")
    lista=list()
    for line in fh:
        lista.append(int(line))

    return lista

#main
print "hola"
#a=[3,8,2,5,1,4,7,6]
#a=[3,9,8,4,6,10,2,5,7,1]
#print a
#b=[8,7,6]
#partition(b,0,2)
#print b
a=readValues("tareaOZ.txt")
quicksort(a,0,len(a)-1)
print a
print counter
