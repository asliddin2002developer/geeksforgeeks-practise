class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        anti_cloc_str1 = (str1[-2]+str1[-1]) + str1[:len(str1)-2]
        clock_str1 = str1[2: len(str1)] + (str1[0] + str1[1])
        if anti_cloc_str1 == str2:
            return True
        elif clock_str1 == str2:
            return True
        else:
            return False

