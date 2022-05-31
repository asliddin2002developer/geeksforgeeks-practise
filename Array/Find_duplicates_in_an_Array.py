class Solution:

    def duplicates(self, arr, n):
        # code here
        # 	hashmap = {}
        # 	dup = []

        # 	for i in range(len(arr)):
        # 	    if arr[i] in hashmap:
        # 	        dup.append(arr[i])

        # 	    else:
        # 	        hashmap[arr[i]] = i

        # 	if dup:
        # 	    return sorted(list(set(dup)))
        # 	else:
        # 	    return [-1]

        ############## second solution #############

        # First check all the values that are
        # present in an array then go to that
        # values as indexes and increment by
        # the size of array
        for i in range(0, n):
            index = arr[i] % n
            arr[index] += n

        # Now check which value
        # exists more
        # than once by dividing
        # with the size
        # of array
        flag = False
        res = []
        for i in range(0, n):
            if (arr[i] // n) > 1:
                res.append(i)
                flag = True

        if flag == False:
            res.append(-1)
        return res


