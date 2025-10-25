# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1 = headA
        ptr2 = headB

        while ptr1 != ptr2:
            if ptr1 == None:
                ptr1 = headB
            else:
                ptr1 = ptr1.next
            

            if ptr2 == None:
                ptr2 = headA
            else:
                ptr2 = ptr2.next
        
        return ptr1