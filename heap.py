print "heap"

heap_min=['x']
heap_max=['x']


def removeroot(heap,min):
    val=heap[1]
    heap[1]=heap.pop()
    print heap
    if min:
        bubbledown(heap)
    else:
        bubbledown_max(heap)
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





