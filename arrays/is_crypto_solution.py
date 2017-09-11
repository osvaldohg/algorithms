# Arrays
# codefights
# by Oz

def isCryptSolution(crypt, solution):
    res=[]
    keys={}
    
    for pair in solution:
        keys[pair[0]]=pair[1]
    
    for word in crypt:
        num=""
        for letter in word:
            num+=keys[letter]
            
        if num[0]=="0" and len(num)>1:
            return False
        
        res.append(int(num))
        
    print res
    if (res[0]+res[1])==res[2]:
        return True
    else:
        return False
            
