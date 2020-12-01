arr =  [1,3,3,4,5,9,7,8,11,10]
def bubble_sort(arr):
  count = 0
  for j in range(0,len(arr)):
    for i in range(0, len(arr)-j-1):
      count += 1
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
  print(count)
  print(arr)

bubble_sort(arr)

