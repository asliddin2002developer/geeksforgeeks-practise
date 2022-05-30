'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''


class Solution:

    # Function to count nodes of a linked list.
    def getCount(self, head_node):
        # code here
        cur = head_node
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

