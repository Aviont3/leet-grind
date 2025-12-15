# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# "Save next, flip pointer, move prev, move curr."
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None
        
            
        while curr:
            
            next_temp = curr.next # temporary holds the next node

            curr.next = prev # sets the next as prev as the next start the process of flipping the direction
            prev = curr # prev becomes the curr
            curr = next_temp # curr becomes the next 
            
            
            
        return prev
