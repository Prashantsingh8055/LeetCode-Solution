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
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Advance fast pointer so that there's a gap of n between slow and fast
        for _ in range(n + 1):
            fast = fast.next

        # Move fast to the end, maintaining the gap
        while fast:
            fast = fast.next
            slow = slow.next

        # Skip the nth node from the end
        slow.next = slow.next.next

        return dummy.next