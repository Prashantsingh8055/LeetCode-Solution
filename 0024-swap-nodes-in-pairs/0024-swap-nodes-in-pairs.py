# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify edge cases (like swapping the head)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # We need at least two nodes ahead to perform a swap
        while prev.next and prev.next.next:
            # 1. Identify the nodes to swap
            first = prev.next
            second = prev.next.next
            
            # 2. Reassign pointers to swap them
            prev.next = second         # The node before the pair now points to the second node
            first.next = second.next   # The first node points to whatever comes after the pair
            second.next = first        # The second node points back to the first node
            
            # 3. Move the prev pointer forward for the next iteration
            prev = first
            
        # Return the new head, which is right after our dummy node
        return dummy.next