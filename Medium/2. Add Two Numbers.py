# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        tmp = res
        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val
            
            if carry > 0:
                sum += carry
            
            carry = sum // 10
            value = sum % 10

            node = ListNode(value)
            tmp.next = node

            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            value = l1.val + carry
            
            carry = value // 10
            value = value % 10
            
            node = ListNode(value)

            tmp.next = node
            tmp = tmp.next
            l1 = l1.next
        
        while l2:
            value = l2.val + carry

            carry = value // 10
            value = value % 10
            
            node = ListNode(value)

            tmp.next = node
            tmp = tmp.next
            l2 = l2.next
        
        if carry:
            node = ListNode(carry)

            tmp.next = node
        
        return res.next
