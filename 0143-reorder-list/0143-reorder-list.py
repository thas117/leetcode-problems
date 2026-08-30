class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        if not head or not head.next:
            return

        # Find the middle of the list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        second = slow.next
        slow.next = None

        # Reverse the second half
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev

        # Merge both halves
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2