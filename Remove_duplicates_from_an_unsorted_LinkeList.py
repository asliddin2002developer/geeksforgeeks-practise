# User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None

'''


class Solution:
    # Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        hashmap = {}
        cur = head
        prev = None

        while cur:
            if cur.data in hashmap:
                prev.next = cur.next

            else:
                hashmap[cur.data] = cur.data
                prev = cur
            cur = cur.next

        return head


