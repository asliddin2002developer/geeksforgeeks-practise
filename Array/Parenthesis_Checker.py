
#User function Template for python3

class Solution:

    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        res = ['()', '{}', '[]']
        stack = []
        for i in range(len(x)):
            if x[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                cur_char = stack.pop()
                if cur_char == '(':
                    if x[i] != ")":
                        return False
                if cur_char == '{':
                    if x[i] != "}":
                        return False
                if cur_char == '[':
                    if x[i] != "]":
                        return False
        if stack:
            return False
        return True



        return True            
        
