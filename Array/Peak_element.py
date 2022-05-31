# your task is to complete this function
# function should return index to the any valid peak element
class Solution:

    def peakElement(self, arr, n):
        # Code here
        ########### 1 ###############
        # max_n = max(A)
        # index = A.index(max_n)
        # return index

        # Code here
        ##################  2  #################
        if n is 1:
            return 0
        for i in range(n):

            # if element at first index is greater than next
            if i == 0 and arr[1] < arr[0]:
                return 0

            # if element is at last index and it is greater than
            # its prev one
            elif i == n - 1 and arr[n - 2] < arr[n - 1]:
                return n - 1

            # case, when element is at any other index
            # then you need to check both of its neighbour
            elif arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                return i

