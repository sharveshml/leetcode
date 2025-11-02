# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left: int, right: int):
        node = ListNode(0)
        tmp = node

        while left and right:
            if left.val <= right.val:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next
            tmp = tmp.next
            
        if left:
            tmp.next = left
        elif right:
            tmp.next = right
        
        return node.next
    def mergesort(self, start: int, end: int, lists: List[Optional[ListNode]]):
        if start > end:
            return None

        if start == end:
            return lists[start]

        mid = (start + end) // 2

        left = self.mergesort(start, mid, lists)
        right = self.mergesort(mid+1, end, lists)

        return self.merge(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        return self.mergesort(0, len(lists)-1, lists)