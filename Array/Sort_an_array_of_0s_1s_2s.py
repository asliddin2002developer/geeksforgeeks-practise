#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        low = 0
        mid = 0
        high = n-1
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid +=1
            elif arr[mid] == 2:
                arr[high], arr[mid] = arr[mid], arr[high]
                high -= 1
            else:
                mid+=1






