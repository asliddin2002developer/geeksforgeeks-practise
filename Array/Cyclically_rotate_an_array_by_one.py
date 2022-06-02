def rotate(arr, n):
    elem = arr[-1]
    arr.insert(0, elem)
    arr.pop()

    ######### actual solution ##########
    x = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];

    arr[0] = x;



