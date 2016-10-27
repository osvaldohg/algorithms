#test1

def count(elements):
    d=dict()
    counter=0
    initial=0
    last=0
    pointer=0
    
    if elements[pointer]==1:
        pointer+=1
        counter+=1
        while pointer < len(elements):
            if elements[pointer]==1:        
                counter+=1
                initial=counter
            else:
                break
            pointer+=1
            
    counter=0
    pointer+=1
    while pointer < len(elements):
        if elements[pointer] == 1:
            counter+=1
            if pointer == (len(elements)-1):
                last=counter
            
        else:
            if counter > 0:
                if counter not in d:
                    d[counter] = 1
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
#test=[1,0,1,1,0,0,1,1,1,0,1,1,0]
#test=[1,0,1,1,0,0,1,1,1,0,1,1,0,1,1]
test=[1,1,1,0,1,1,0,1]
#test=[1,0,1,1,0]
count(test)   
