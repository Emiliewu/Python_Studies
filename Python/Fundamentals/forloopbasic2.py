# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(test):
  for x in range(0,len(test)):
    if test[x] > 0:
      test[x] = "big"
  return test
test1 = biggie_size([1,-2,-3,4,5,0])
test2 = biggie_size([-1, 3, 5, -5])
print(test1)
print(test2)
# # # -------

# Count Positives - Given a list of numbers, 
# create a function to replace the last value with the number of positive values.
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(test):
  count = 0
  for x in range(0, len(test)):
    if test[x] > 0:
      count +=1
  test[-1] = count
  return test
test1 = count_positives([-1,1,1,1])
test2 = count_positives([1,6,-4,-2,-7,-2])
print(test1)
print(test2)

# ------------------------

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(test):
  sum = 0
  for x in range(0, len(test)):
    sum += test[x]
  return sum
test1 = sum_total([1,2,3,4])
test2 = sum_total([6,3,-2])
print(test1)
print(test2)

# -----------------------------------

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def average(test):
  sum = 0 
  for x in range(0, len(test)):
    sum += test[x]
  return sum/len(test)
test1 = average([1,2,3,4])
print(test1)

# --------------------------

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(arrlist):
  return len(arrlist)
test1 = length([37,2,1,-9])
test2 = length([])
print(test1)
print(test2)
# -----------------------

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(arrlist):
  if len(arrlist) == 0:
    return False
  min = arrlist[0]
  for x in range(0, len(arrlist)):
    if min > arrlist[x]:
      min = arrlist[x]
  return min
test1 = minimum([37,2,1,-9])
test2 = minimum([])
print(test1)
print(test2)
# -----------------------

# Maximum - Create a function that takes a list and returns the maximum value in the list.
#  If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(test):
  if len(test) == 0:
    return False
  max = test[0]
  for x in range(0, len(test)):
    if max < test[x]:
      max = test[x]
  return max
test1 = maximum([37,2,1,-9])
test2 = maximum([])
print(test1)
print(test2)

# -------------------------------

# Ultimate Analysis - Create a function that takes a list and returns a dictionary 
# that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(test):
  sumTotal = 0
  average = 0
  minimum = test[0]
  maximum = test[0]
  length = len(test)
  for x in range(0, len(test)):
    sumTotal += test[x]
    if minimum > test [x]:
      minimum = test[x]
    if maximum > test[x]:
      maximum = test[x]
    average = sumTotal / len(test)
  dictionary = {'sumTotal': sumTotal, 'average': average, 'minimum': minimum, 'maximum': maximum, 'length': length}
  return dictionary
test1 = ultimate_analysis([37,2,1,-9]) 
print(test1)

# -----------------------

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(test):
  length = len(test)
  if length < 2:
    return test
  for x in range(0, length//2):
    temp = test[x]
    test[x] = test[length-1-x]
    test[length-1-x] = temp
  return test
test1 = reverse_list([37,2,1,-9])
print(test1)