def binary_search(arr, key, l, r):
    if l > r:
        return -1
    else:
        m = (l + r) // 2
        if key == arr[m]:
            return m
        elif key < arr[m]:
            return binary_search(arr, key, l, m-1)
        elif key > arr[m]:
            return binary_search(arr, key, m+1, r)

arr = [1,5,8,65,214,1452,8888]
key = 65

print(binary_search(arr, key, 0 , len(arr)))
