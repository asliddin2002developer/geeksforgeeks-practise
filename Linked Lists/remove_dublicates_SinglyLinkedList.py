# Remove duplicate element from sorted Linked List
# Easy Accuracy: 46.37% Submissions: 100k+ Points: 2
# Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).
# Note: Try not to use extra space. Expected time complexity is O(N). The nodes are arranged in a sorted way.
#
# Example 1:
#
# Input:
# LinkedList: 2->2->4->5
# Output: 2 4 5
# Explanation: In the given linked list
# 2 ->2 -> 4-> 5, only 2 occurs more
# than 1 time.

# User function Template for python3
'''
	Your task is to remove duplicates from given
	sorted linked list.

	Function Arguments: head (head of the given linked list)
	Return Type: none, just remove the duplicates from the list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''


# Function to remove duplicates from sorted linked list.
#my-solution
def removeDuplicates(head):
    # code here
    cur = head
    prev = None
    hashmap = {}
    while cur:
        if cur.data not in hashmap:
            hashmap[cur.data] = cur.data
            prev = cur
            cur = cur.next
        else:
            prev.next = cur.next
            cur = cur.next
    return head