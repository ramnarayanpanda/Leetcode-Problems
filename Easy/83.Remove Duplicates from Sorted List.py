# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.


# Check the leetcode page it has diagrams.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]



from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        
        if not temp:
            return head
        
        while temp.next:
            if temp.val == temp.next.val: temp.next = temp.next.next
            else: temp = temp.next 

            if not temp.next: break
            
        return head