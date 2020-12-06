# Build an algorithm for insertion sort. 
# Please watch the video here to understand how insertion sort works and implement the code. 
# Basically, this sort works by starting at index 1, 
# shifting that value to the left until it is sorted relative to all values to the left, 
# and then moving on to the next index position 
# and performing the same shifts until the end of the list is reached.
#psuedocode: 1. from the second index, compare the value of the index to the previous index's value,
#  if it is larger, insert the value in to the index. 2. from a loop i from index 1, to the end of the array 
# which is the len-1
arr = [9,3,1,4,5,9,7,8,11,10]
def insertion_sort(arr):
  count = 0
  for i in range(1, len(arr)):
    while i > 0 and arr[i-1] > arr[i]:
      arr[i-1], arr[i] = arr[i], arr[i-1]
      count += 1
      i -= 1
  return count, arr

print(insertion_sort(arr))

# ===========================================
# another way to do it
def insertion_sort2(arr):
  count = 0
  for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
      continue
    e = arr[i]
    while i > 0 and arr[i-1] > e:
      arr[i] = arr[i-1]
      count += 1
      i -= 1
    arr[i] = e
  return count, arr

list = [9,3,1,4,5,9,7,8,11,10]
print(insertion_sort2(list))
