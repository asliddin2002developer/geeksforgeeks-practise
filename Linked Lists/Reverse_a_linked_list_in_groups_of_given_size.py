"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""


class Solution:
    def reverse(self, head, k):
        # Code here
        cur = head
        prev = None
        nxt = None
        count = 0

        while cur and count < k:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count += 1
        if nxt != None:
            head.next = self.reverse(nxt, k)
        return prev