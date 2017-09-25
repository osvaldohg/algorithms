# common techniques
# from codefights
# by oz

def sumOfTwo(a, b, v):
    x=[]
    y={}

    if len(a)<len(b):
        x=a
        for n in b:
            y[n]=1
    else:
        x=b
        for n in a:
            y[n]=1
        
    for num in x:
        val=v-num
        try:
            if y[val]==1:
                return True
        except:
            pass
    return False
    
