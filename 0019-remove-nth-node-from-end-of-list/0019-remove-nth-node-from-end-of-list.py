# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        
        # Create dummy node
        dummy = ListNode(0)
        dummy.next = head

        # Two pointers
        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for i in range(n):
            fast = fast.next

        # Move both pointers
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the node
        slow.next = slow.next.next

        # Return the new head
        return dummy.next