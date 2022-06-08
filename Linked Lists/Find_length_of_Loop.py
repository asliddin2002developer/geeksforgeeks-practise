'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''

#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    #Your code here
    
    fast, slow = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if fast is None or fast.next is None:
        return 0
        
    fast = head
    while fast!=slow:
        fast = fast.next
        slow = slow.next
    
    count = 1
    while fast.next != slow:
        fast = fast.next
        count +=1
    return count    
        
    
    
