def mergeSortedArrays(arr1, arr2):
  i=0
  j=0
  arr3 = []
  if len(arr1) == 0:
      return arr2
  if len(arr2) == 0:
      return arr1

  while i < len(arr1) and j < len(arr2) :
      if(arr1[i] <= arr2[j]):
          arr3.append(arr1[i])
          i+=1
      else:
          arr3.append(arr2[j])
          j+=1
  if i < len(arr1):
      arr3.extend(arr1[i:])
  if j < len(arr2):
      arr3.extend(arr2[j:])
  return arr3

print(mergeSortedArrays([0,3,4,31,44,545], [3,4,6,30,33,232]))
