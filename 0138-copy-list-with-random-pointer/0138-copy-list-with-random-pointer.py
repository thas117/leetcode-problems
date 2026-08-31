"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # Map original node -> copied node
        old_to_new = {}

        # Step 1: Create all new nodes
        current = head

        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Step 2: Connect next and random pointers
        current = head

        while current:
            old_to_new[current].next = old_to_new.get(current.next)
            old_to_new[current].random = old_to_new.get(current.random)

            current = current.next

        return old_to_new[head]       