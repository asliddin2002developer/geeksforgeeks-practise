def transitionPoint(arr, n):
    #Code here
    low = 0
    high = n-1

    if n >= 1 and arr[0] != 0:
        return 0

    for i in range((n//2):

        mid = (low+high) // 2

    if arr[mid] == 0 and arr[mid+1] == 1:
        return arr.index(arr[mid+1])
    elif arr[mid] != 0:
    high = mid
elif arr[mid] == 0:
low = mid

return -1



