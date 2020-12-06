# Selection sort works by iterating through the list, 
# finding the minimum value, and moving it to the beginning of the list. 
# Then, ignoring the first position, which is now sorted, 
# iterate through the list again to find the next minimum value and move it to index 1. 
# This continues until all values are sorted.
arr = [9,3,1,4,5,9,7,8,11,10]
def selection_sort(arr):
  count = 0
  for i in range(0, len(arr)-1):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
        count += 1
    if min_index != i:
      arr[i], arr[min_index] = arr[min_index], arr[i]
  return count, arr

print(selection_sort(arr))

