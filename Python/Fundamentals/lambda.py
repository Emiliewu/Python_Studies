def test(a, function):
  for i in range(0, len(a)):
    a[i] = function(a[i],2)
  return a
list = [1,2,3,4,5]
# print(test(list, lambda num: num*num))
# print(test(list, lambda num: num**2))
print(test(list, lambda num1, num2: num1+num2))
