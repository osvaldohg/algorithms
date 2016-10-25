#test1

print "test 1"


def count(elements):
    d=dict()
    counter=0
    initial=0
    last=0
    pointer=0
    
    if elements[pointer]==1:
        pointer+=1
        counter+=1
        while elements[pointer] ==1:
            counter+=1
            pointer+=1
        initial=counter
        counter=0
    
    
    while pointer < len(elements):
        if elements[pointer] == 1:
            counter+=1
            pointer+=1
        else:
            print "this is counter",counter
            if counter not in d:
                d[counter] = 1
            elif pointer == len(elements) -1:
                last=counter
            else:
                d[counter] = d[counter] + 1

            counter=0
        pointer+=1
    
    total=last+initial
    if total > 0:
        if total not in d:
            d[total] = 1
        else:
            d[total] = d[total] + 1
            
    print d
    
#main 
test=[1,0,1,1,0,0,1,1,1,0,1,1,0]
count(test)   
