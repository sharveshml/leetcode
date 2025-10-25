# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
        
        slow = self.reversed(slow)
        fast = head

        while fast and slow:
            if fast.val != slow.val:
                return False
            else:
                fast = fast.next
                slow = slow.next
        
        return True

    def reversed(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        next = head.next

        while cur != None:
            cur.next = prev
            prev = cur
            cur = next

            if next != None:
                next = next.next

        return prev