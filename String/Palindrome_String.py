class Solution:
    def isPalindrome(self, S):
        i = 0
        j = len(S)-1
        S = S.lower()
        while i < j:
            while not S[i].isalnum() and i < j:
                i += 1
            while not S[j].isalnum() and i < j:
                j -= 1
            if S[i] != S[j]:
                return 0
            i+=1
            j -=1
        return 1


