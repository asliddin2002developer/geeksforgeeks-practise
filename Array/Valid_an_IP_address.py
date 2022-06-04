def str_to_int(val):
    output = None
    try:
        output = int(val)
    except:
        output = None
    return output


def isValid(s):
    #code here
    is_True = True
    s = s.split(".")
    if len(s) != 4:
        return False

    for i in s:
        if len(i) > 1:
            if i[0] == '0':
                return False
        #try to convert i into int
        num = str_to_int(i)
        if num is None:
            return False
        if num >= 0 and num <= 255:
            continue
        else:
            is_True = False
    return is_True


