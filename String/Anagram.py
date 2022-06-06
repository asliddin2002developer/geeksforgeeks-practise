class Solution:

    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        # simple approach
        # a = sorted(a)
        # b = sorted(b)
        # return a == b

        # 2 approach with hash

        d = {}

        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in b:
            if i in d:
                d[i] -= 1
            else:
                d[i] = 1

        for i in d:
            if d[i] != 0:
                return False
        return True        
                
                
                