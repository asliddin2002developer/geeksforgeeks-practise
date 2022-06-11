class Solution:
    def majorityElement(self, arr, n):
        #Your code here
        hashmap = dict()
        if n == 1:
            return arr[0]

        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for k, v in hashmap.items():
            if v > n/2:
                return k

        return -1

