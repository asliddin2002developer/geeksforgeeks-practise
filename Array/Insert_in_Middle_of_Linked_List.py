'''
    Your task is to insert a new node in
	the middle of the linked list with
	the given value.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Function Arguments: head (head of linked list), node
	(node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''


# Function to insert a node in the middle of the linked list.
def insertInMid(head, node):
    # code here
    slow = head
    fast = head.next

    # incrementing slow pointer once and fast pointer twice, so when fast reaches the end of the linkedlist and the loop gets terminated slow will be in the middle of the linkedlist.

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # inserting the node after slow and returning the head.

    node.next = slow.next
    slow.next = node
    return head


