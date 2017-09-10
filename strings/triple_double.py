# from codefights, wizeline assessment
# by oz

def tripleDouble(a, b):
    print 
    print check(b,2)
    
    val_a=set(check(a,3))
    val_b=set(check(b,2))
    
    res=val_a.intersection(val_b)
    if len(res)>0:
        return True
    else:
        return False

def check(n,limit):
    count=1
    res=[]
    
    if len(n)<limit:
        return res
       
    
    for i in range(1,len(n)):
        if n[i-1]==n[i]:
            count+=1
            if count==limit:
                res.append(n[i])
        else:
            count=1
            
    return res    
            
    