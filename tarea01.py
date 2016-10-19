
def karatsuba(num1, num2):
    print "iterating"
    if int(num1) < 100 or int(num2) <100:
        return int(num1)*int(num2)
        
    m=len(num1)
    m2=m/2
    
    a=num1[:m2]
    b=num1[m2:]
    c=num2[:m2]
    d=num2[m2:]
    
    z0=karatsuba(a,c)
    z11=karatsuba(a,d)
    z12=karatsuba(b,c)
    z13=z11+z12
    z2=karatsuba(b,d)
    
    return z0*((10**m)) + (z13*(10**m2)) + z2
    
#MAIN    
print karatsuba("1234","5678")
print karatsuba("3141592653589793238462643383279502884197169399375105820974944592","2718281828459045235360287471352662497757247093699959574966967627")
