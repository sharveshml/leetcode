# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        prev = None
        cur = head
        next = cur.next

        while cur != None:
            cur.next = prev
            prev = cur
            cur = next

            if next != None:
                next = next.next
        
        return prev
