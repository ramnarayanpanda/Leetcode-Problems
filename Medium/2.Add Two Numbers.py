# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]




class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        from itertools import zip_longest

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

        lst1 = int(''.join([str(i) for i in print_linklist(l1)[::-1]]))
        lst2 = int(''.join([str(i) for i in print_linklist(l2)[::-1]]))

        #print(str(lst1+lst2)[::-1])
        return create_linklist_from_list([int(i) for i in str(lst1+lst2)[::-1]])