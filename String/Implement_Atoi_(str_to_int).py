class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        # Code here

        string = string.replace(" ", "")
        if string[0] == '-':
            is_negative = True
            str_idx = 1
        else:
            is_negative = False
            str_idx = 0
        res = 0
        for i in range(str_idx, len(string)):
            if not string[i].isdigit():
                return -1
            place_val = 10 ** (len(string) - (i+1))
            int_chr = ord(string[i]) - ord('0')
            res += int_chr * place_val

        if is_negative:
            return -1 * res
        else:
            return res

