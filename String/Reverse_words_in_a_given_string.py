class Solution:

    #Function to reverse words in a given string.
    def reverseWords(self,S):
        str = ''
        sl  = S.split(".")
        count = 0
        for i in sl[::-1]:
            if count == len(sl)-1:
                str += i
                break
            count +=1
            str += i+'.'
        return str


