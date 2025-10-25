# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        tmp = head
        length = 1

        while tmp.next:
            tmp = tmp.next
            length += 1

        tmp.next = head
        k = length-k%length

        while k > 0:
            tmp = tmp.next
            k -= 1
        
        head = tmp.next
        tmp.next = None

        return head

        