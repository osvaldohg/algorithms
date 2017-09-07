# Arrays
# from codefights
# by oz

def firstDuplicate(a):
    numbers={}
    
    for i in range(0,len(a)):
        if a[i] in numbers:
            return a[i]
        else:
            numbers[a[i]]=1
    
    return -1
    