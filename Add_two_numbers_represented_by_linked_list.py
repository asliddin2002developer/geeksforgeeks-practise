''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    # Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        str1 = ''
        str2 = ''
        lis1 = []
        lis2 = []
        lis3 = []
        first_ll = first
        second_ll = second

        while first_ll:
            lis1.append(first_ll.data)
            first_ll = first_ll.next

        while second_ll:
            lis2.append(second_ll.data)
            second_ll = second_ll.next

        str1 = ''.join(map(str, lis1))

        str2 = ''.join(map(str, lis2))

        sum_num = int(str1) + int(str2)

        for i in str(sum_num):
            lis3.append(i)

        new_ll = LinkedList()
        for i in lis3:
            new_ll.insert(i)
        return new_ll.head