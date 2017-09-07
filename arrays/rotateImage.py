# Arrays
# codefights
# by oz

def rotateImage(a):
    n=len(a)
    for layer in range(0,n/2):
        first=layer
        last=n-1-layer
        for i in range(first,last):
            offset=i-first
            top=a[first][i]
            
            a[first][i]=a[last-offset][first]
            a[last-offset][first]=a[last][last-offset]
            a[last][last-offset]=a[i][last]
            a[i][last]=top
            
    return a