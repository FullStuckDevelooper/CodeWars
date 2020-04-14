def find_uniq(arr):
    arr.sort()
    n = 0
    if (arr[0] < arr[1]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]

    return n
