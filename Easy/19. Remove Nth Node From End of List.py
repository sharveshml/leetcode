# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count, tmp = 0, head

        while tmp:
           count += 1

           tmp = tmp.next

        if count == 1 or count == n:
            return head.next

        tmp = head
        cur = 1
        while  cur != count - n:
            cur += 1
            tmp = tmp.next
        
        tmp.next = tmp.next.next

        return head