def strstr(s,x):
    #code here

    len_str = len(x)
    for i in range(len(s)):
        if s[i:len_str] == x:
            return i
        len_str += 1
    return -1

