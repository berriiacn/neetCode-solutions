# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            # tmp variable to update pointers
            nxt = curr.next
            # reverse the next pointer to prev node
            curr.next = prev
            # update pointers
            prev = curr
            curr = nxt
        
        return prev
    
from typing import Optional