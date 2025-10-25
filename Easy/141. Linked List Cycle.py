# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return head
    
        slow, fast = head, head.next

        while fast != None:
            slow = slow.next

            if fast.next != None:
                fast = fast.next.next
            else:
                break

            if fast == slow:
                return True


        return False