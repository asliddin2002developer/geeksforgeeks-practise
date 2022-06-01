# User function Template for python3


class Solution:

    def MissingNumber(self, array, n):
        # code here
        actual_num = [i for i in range(1, n + 1)]

        diff = set(actual_num).difference(set(array))
        return list(diff)[0]

        ############ second solution ############

        # diff = sum(actual_num) - sum(array)
        # return diff


