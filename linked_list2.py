#created 7/6/17
#by oz

class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def reverse(self):
        prev=None
        current=self.head
        
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        
        self.head=prev
        
#  P   C    N 
# **-> 1 -> 3 -> 5 -> None
# None<- 1 <- 3 <- 5 <- **

    