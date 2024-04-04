# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        prev, forward = head, head.next

        while forward:
            if prev.val == forward.val:
                temp = forward.next
                forward.next = None
                forward = temp
                prev.next = forward
            else:
                prev = forward
                forward = forward.next

        return head
