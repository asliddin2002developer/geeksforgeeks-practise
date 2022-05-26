'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''


class Solution:
    # Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self, head, x):
        # code here
        new_node = Node(x)
        if head:
            new_node.next = head
        head = new_node
        return head

    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        # code here
        new_node = Node(x)
        if head == None:
            head = new_node
            return head

        last_node = head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return head




