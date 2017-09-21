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
   prev=None
   current=l
      
   while l is not None and l.value==k:
      l=l.next
   
   while current is not None:
      
      if current.value==k:
         if prev is not None:
            prev.next=current.next
         
         current=current.next
         continue
      prev=current
      current=current.next
      
   return l
         
      
