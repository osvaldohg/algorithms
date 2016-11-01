print "test_set"

def test_set(A,B):
    aSet=set(A)
    bSet=set(B)

    if aSet == bSet:
        return "equal"    
        
    #if aSet.issubset(bSet):
    #    return "sublist"
    
    if aSet <= bSet:
        return "sublist"
    
    #if aSet.issuperset(bSet):
    #    return "superlist"
    
    if aSet >= bSet:
        return "superlist"    
    
    return "neither"
    
        
#main

A=[1,2,3]
B=[1,2,3,4,5]
#sublist

C=[1,2,3]
D=[1,2,3]
#"equal"

E=[1,2,3,4,5]
F=[2,3,4]
#superlist

G=[1,2,4]
H=[1,2,3,4,5]
#neither

I=[3,4,5]
J=[6,7,8]
#neither

K=[2,3,4]
L=[1,2,3,4]
#sublist

M=[1,2,3]
N=[1,2,0,1,2,3]
#sublist

print test_set(A,B)
print test_set(C,D)
print test_set(E,F)
print test_set(G,H)
print test_set(I,J)
print test_set(K,L)
print test_set(M,N)
