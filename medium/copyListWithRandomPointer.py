"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        mapping = {None : None}

        # perform deep copy and map old and new list nodes together
        while cur:
            copy = Node(cur.val)
            mapping[cur] = copy
            cur = cur.next
        
        cur = head

        # set the next and random pointers for all the copies
        while cur:
            copy = mapping[cur]
            copy.next = mapping[cur.next]
            copy.random = mapping[cur.random]
            cur = cur.next

        return mapping[head]