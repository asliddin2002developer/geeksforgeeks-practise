'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, pos):
    # Code here
    cur = head
    prev = None

    # if current node is head
    if pos == 1:
        head = cur.next
        cur = None
        return head

    while cur and pos > 1:
        prev = cur
        cur = cur.next
        pos -= 1

    prev.next = cur.next
    cur = None
    return head



