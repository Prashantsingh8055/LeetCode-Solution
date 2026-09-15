import heapq


class Solution(object):

  def mergeKLists(self, lists):
    """Sorts k linked lists into one linked list using a min-heap.

    :type lists: List[Optional[ListNode]] :rtype: Optional[ListNode]
    """
    heap = []

    # Push the head of each non-empty list into the heap
    # Include an index (i) to prevent comparisons between ListNode objects when values are equal
    for i, node in enumerate(lists):
      if node:
        heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    current = dummy

    while heap:
      val, i, node = heapq.heappop(heap)
      current.next = node
      current = current.next

      if node.next:
        heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next