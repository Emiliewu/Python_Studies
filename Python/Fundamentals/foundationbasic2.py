# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
def countDown(num):
  arrlist = []
  while num >= 0:
    arrlist.append(num)
    num -= 1
  return arrlist
print(countDown(10))
# ------------------------------------
# Print and Return - Create a function that will receive a list with two numbers.
#  Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def pandR(arrlist):
  print(arrlist[0])
  return(arrlist[1])
result = pandR([5,6])
print(result)
# -------------------------------------
# First Plus Length - Create a function that accepts a list 
# and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(arrlist):
  sum = arrlist[0]+len(arrlist)
  return sum
result = first_plus_length([1,2,3,4,5])
print(result)
# -----------------
# Values Greater than Second 
# - Write a function that accepts a list 
# and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
def values_greater_than_second(arrlist):
  arrNew = []
  arrlen = len(arrlist)
  count = 0
  if arrlen < 2:
    return False
  else:
    for x in range (0, arrlen):
      if arrlist[x] > arrlist[1]:
        arrNew.append(arrlist[x])
        count += 1
    print(count)
    return arrlist
test1 = values_greater_than_second([5,2,3,2,1,4])
test2 = values_greater_than_second([3])
print(test1)
print(test2)
# -----------------
# This Length, That Value - Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def this_length_this_value(size,value):
  newlist = []
  for x in range(0,size):
    newlist.append(value)
  return newlist
print(this_length_this_value(4,7))
print(this_length_this_value(6,2))

