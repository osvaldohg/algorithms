# common techniques
# from codefights
# by oz

def containsDuplicates(a):
    values={}
    
    for num in a:
        if num in values:
            return True
        else:
            values[num]=1
            
    return False
