def binary_search(arr, key):
  l = 0
  r = len(arr) -1
  while l <= r:
      mid = (l+r) // 2
      if key == arr[mid]:
          return mid
      elif key < arr[mid]:
          r = mid - 1
      elif key > arr[mid]:
          l = mid + 1
  return -1



arr = [1,5,8,78,200,452]
key = 5

print(binary_search(arr, key))
