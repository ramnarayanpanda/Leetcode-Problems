# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]







# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def print_linklist(obj: Optional[ListNode]):
            if obj == None:
                return []
            else:
                lst = [obj.val]
                while obj.next:
                    obj = obj.next
                    lst.append(obj.val)
                return lst

        def create_linklist_from_list(lst):
            if len(lst) == 0: return None
            i = 0
            obj1 = ListNode(lst[i])
            obj2 = obj1
            for i in range(1, len(lst)):
                obj2.next = ListNode(lst[i])
                obj2 = obj2.next
            return obj1

        fin_lst = []
        lst1 = print_linklist(list1)
        lst2 = print_linklist(list2)
        l1, l2 = len(lst1), len(lst2)
        ll1, ll2 = 0, 0

        while (ll1 < l1) and (ll2 < l2):
            if lst1[ll1] <= lst2[ll2]:
                fin_lst.append(lst1[ll1])
                ll1+=1
            else: 
                fin_lst.append(lst2[ll2])
                ll2+=1
            
        while (ll1 < l1):
            fin_lst.append(lst1[ll1])
            ll1 += 1

        while (ll2 < l2):
            fin_lst.append(lst2[ll2])
            ll2 += 1
            
        print(fin_lst)
        return create_linklist_from_list(fin_lst)