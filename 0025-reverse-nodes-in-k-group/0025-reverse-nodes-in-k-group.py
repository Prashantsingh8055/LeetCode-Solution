# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 1:
            return head

        # Dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        
        prev_group = dummy

        while True:
            # 1. Check if there are at least k nodes left
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            next_group = kth.next
            
            # 2. Reverse k nodes
            prev = next_group
            curr = prev_group.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 3. Connect with the rest of the list
            group_head = prev_group.next
            prev_group.next = kth
            prev_group = group_head