print "heap"

heap_min=['x']
heap_max=['x']

def removeroot(heap,min):
    val=heap[1]
    #heap[1]=heap.pop()
    #print heap
    if len(heap) >2:
        heap[1]=heap.pop()
        if min:
            bubbledown(heap)
        else:
            bubbledown_max(heap)
    else:
        heap.pop()
    return val

def getroot(heap):
    return heap[1]
    
def bubbledown(heap):
    print "bubble"
    for i in range(2,len(heap)):
        #print heap[i/2],heap[i]
        if heap[i/2] > heap[i]:
            #left, right = right, left
            heap[i/2],heap[i]=heap[i],heap[i/2]

def bubbledown_max(heap):
    for i in range(2,len(heap)):
        if heap[i/2] < heap[i]:
            #left, right = right, left
            heap[i/2],heap[i]=heap[i],heap[i/2]
            
def bubbleup(heap):
    for i in range(len(heap)-1,1,-1):
        if heap[i] < heap[i/2]:
            #left, right = right, left
            heap[i/2],heap[i]=heap[i],heap[i/2]

def bubbleup_max(heap):
    for i in range(len(heap)-1,1,-1):
        if heap[i] > heap[i/2]:
            #left, right = right, left
            heap[i/2],heap[i]=heap[i],heap[i/2]
            
def insert(val,heap,min):
    heap.append(val)
    if min:
        bubbleup(heap)
    else:
        bubbleup_max(heap)
#main
#print heap_min
#print heap_max

#true main
fh=open("mediana2.txt","r")
for line in fh:
    number=int(line.strip())
    print number
    
    if len(heap_max) == 1 and len(heap_min) ==1:
        insert(number,heap_max,False)
    
    elif number <= getroot(heap_max):
        if len(heap_max)-len(heap_min)<=0:
            insert(number,heap_max,False)
        else:
            tmp=removeroot(heap_max,False)
            insert(number,heap_max,False)
            insert(tmp,heap_min,True)
    else:
        if len(heap_max)-len(heap_min)>=0:
            insert(number,heap_min,True)
        else:
            tmp=removeroot(heap_min,True)
            insert(number,heap_min,True)
            insert(tmp,heap_max,False)

    print "max",heap_max
    print "min",heap_min




