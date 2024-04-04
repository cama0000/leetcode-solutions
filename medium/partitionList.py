# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less, greater = ListNode(), ListNode()
        lessTail, greaterTail = less, greater

        while head:
            if head.val < x:
                lessTail.next = head
                lessTail = lessTail.next
            else:
                greaterTail.next = head
                greaterTail = greaterTail.next
            head = head.next
        
        lessTail.next = greater.next
        greaterTail.next = None
        
        return less.next