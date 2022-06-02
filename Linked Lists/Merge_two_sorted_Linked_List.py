# User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.

	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''


# Function to merge two sorted linked list.
def sortedMerge(head1, head2):
    # code here
    p = head1
    q = head2
    s = None

    if p is None:
        return q
    if q is None:
        return p

    if p and q:
        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next

        new_head = s

    while p and q:
        if p.data <= q.data:
            s.next = p
            s = p
            p = s.next
        else:
            s.next = q
            s = q
            q = s.next

    if p is None:
        s.next = q
    if q is None:
        s.next = p

    head = new_head
    return new_head


