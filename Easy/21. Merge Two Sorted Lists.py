# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2
        res = ListNode(0)
        tmp = res

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                tmp.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                tmp.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            
            tmp = tmp.next
        
        if ptr1:
            tmp.next = ptr1
        elif ptr2:
            tmp.next = ptr2

        return res.next