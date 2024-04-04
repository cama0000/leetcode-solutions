# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None:
        #     return None

        # prev, forward = head, head.next
        # dummy = ListNode(0, head)
        # s = set()
        # s.add(prev.val)

        # while forward:
        #     if forward.val in s:
        #         if prev.next.val != forward.val:
        #             prev = prev.next
                
        #         if prev.val == forward.val:
        #             curr = prev
        #         else:
        #             curr = prev.next

        #         while curr and curr.val == forward.val:
        #             temp = curr.next
        #             curr.next = None
        #             curr = temp

        #         if prev.val == forward.val:
        #             dummy.next = curr
        #             prev = dummy
        #             forward = curr
        #         else:
        #             forward = curr
        #             prev.next = forward

        #     else:
        #         s.add(forward.val)
        #         forward = forward.next

        # return dummy.next

        dummy = ListNode()
        dummy.next = head    
        cur = dummy

        while cur:
            if cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                temp = cur.next.next

                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                cur.next = temp.next
            else:
                cur = cur.next
        
        return dummy.next