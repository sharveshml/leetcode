# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        slow = fast = head
        hasCycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                hasCycle = True
                break

        if not hasCycle:
            return None
            
        tmp = slow.next

        length = 1
        while tmp != slow:
            tmp = tmp.next
            length += 1

        slow = head
        fast = head
        
        for i in range(length):
            slow = slow.next
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
