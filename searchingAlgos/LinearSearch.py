def linear_search(arr, key):
  n = len(arr)
  for i in range(n):
      if arr[i] == key:
          return i
  return -1

arr = [1, 8 ,74, 63, 125, 55, 7]
key = 5
print(linear_search(arr, key))
