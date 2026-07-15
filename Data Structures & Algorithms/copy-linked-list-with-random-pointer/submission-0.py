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
        original = {None:None}

        curr =  head
        while curr:
            original[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = original[curr]
            copy.next = original[curr.next]
            copy.random = original[curr.random]
            curr = curr.next
        return original[head]