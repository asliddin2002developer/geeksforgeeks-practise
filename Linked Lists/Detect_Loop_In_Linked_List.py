'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None

'''


class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # code here
        ## first approach
        cur = head
        set_ll = set()

        while cur:
            if cur in set_ll:
                return True
            elif cur.next is None:
                return False
            set_ll.add(cur)
            cur = cur.next

        ## second approach
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


