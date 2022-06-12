class Solution:
    #Function to find triplets with zero sum.
    def findTriplets(self, arr, n):
        #code here

        ## first approach

        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if sum([arr[i], arr[j], arr[k]]) == 0:
        #                 return True
        # return False



        # n log n | second approach
        arr.sort()


        for i in range(n//2):
            l = i+1
            r = n-1

            while l < r:
                cur_sum = arr[i]+arr[l]+arr[r]
                if cur_sum == 0:
                    return True
                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1
        return False

