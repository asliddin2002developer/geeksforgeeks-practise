'''
	Your task is to return the data stored in
	the nth node from end of linked list.

	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''


# Function to find the data of nth node from the end of a linked list
def getNthFromLast(head, n):
    # code here

    cur = head
    count = 0

    while cur:
        count += 1
        cur = cur.next

    cur = head
    if n > count:
        return -1

    for i in range((count - n)):
        cur = cur.next
    return cur.data


