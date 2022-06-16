class Solution:

    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1) != len(str2):
            return False

        map1, map2 ={}, {}

        for i in range(len(str1)):
            c1, c2 = str1[i], str2[i]

            if ((c1 in map1 and map1[c1] != c2) or (c2 in map2 and map2[c2] != c1)):
                return False
            map1[c1] = c2
            map2[c2] = c1
        return True   
        
        
      