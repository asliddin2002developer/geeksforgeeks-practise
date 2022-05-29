# User function template for Python

class Solution:
    def binarysearch(self, arr, n, k):
        # code here
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if k == arr[mid]:
                return arr.index(arr[mid])
            elif arr[mid] < k:
                low = mid + 1
            elif arr[mid] > k:
                high = mid - 1
        return -1

        ####  recursive approach #comment all of the code above  #####

    return self.bin_search(arr, 0, n - 1, k)


def bin_search(self, arr, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2

    if arr[mid] == k:
        return mid
    if arr[mid] > k:
        return self.bin_search(arr, 0, mid - 1, target)
    elif arr[mid] < k:
        return self.bin_search(arr, mid + 1, right, target)



