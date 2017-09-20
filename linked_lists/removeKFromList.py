# Linked lists
# codefights
# by Oz 

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
   prev=l
   current=l
   
   while current is not None:
      next=current.next
      
      if current.value==k:
         if current==l:
            l=current.next
            
            #print "lol"
         else:
            prev.next=next
         
      prev=current
      current=current.next
      
   return l
         
      
