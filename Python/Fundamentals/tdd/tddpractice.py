import unittest

def reverseList(arr):
  for i in range(0, (len(arr)//2)):
    arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
  print(arr)
  return arr
# reverseList([1,3,5])

def isPalindrome(str):
  if str == str[::-1]:
    print("this word is palindrome")
    return True
  else:
    print("this word is not palindrome")
    return False
# isPalindrome("racecar")

def coins(num):
  change = []
  quarter = num//25
  change.append(quarter)
  dime = (num - quarter*25)//10
  change.append(dime)
  nickel = (num - quarter*25 - dime*10)//5
  change.append(nickel)
  penny = num - quarter*25 - dime*10 - nickel*5
  change.append(penny)
  # print(change)
  return change
# coins(87)

def factorial(num):
  factorial = 1
  for i in range(2, num+1):
    factorial *= i
  print(factorial)
  return factorial
# factorial(5)

def fibonacci(num):
  fib0 = 0
  fib1 = 1
  if num < 2:
    print(num)
    return num
  else:
    while num >= 2:
      [fib0], [fib1] = [fib1], [fib0+fib1]
      num = num - 1
    print(fib1)
    return fib1
# print(fibonacci(5))

class fibonacciTest(unittest.TestCase):
  def testfibonacci(self):
    self.assertEqual(fibonacci(5), 5)
    self.assertEqual(fibonacci(4), 3)
    self.assertEqual(fibonacci(0), 0)
    self.assertEqual(fibonacci(1), 1)
    self.assertEqual(fibonacci(2), 1)

class factorialTest(unittest.TestCase):
  def testfactorial(self):
    self.assertEqual(factorial(5), 120)
    self.assertEqual(factorial(4), 24)
    self.assertEqual(factorial(3), 6)
    self.assertEqual(factorial(2), 2)


class coinsTest(unittest.TestCase):
  def testcoins(self):
    self.assertEqual(coins(87), [3,1,0,2])
    self.assertEqual(coins(99), [3,2,0,4])
    self.assertEqual(coins(9), [0,0,1,4])
    self.assertEqual(coins(10), [0,1,0,0])
    self.assertEqual(coins(150), [6,0,0,0])

class isPalindromeTest(unittest.TestCase):
  def testisPalindrome(self):
    self.assertTrue(isPalindrome("racecar"))
    self.assertFalse(isPalindrome("rabcr"))
    self.assertFalse(isPalindrome("emilie"))
    self.assertEqual(isPalindrome("racecar"), True)
    self.assertEqual(isPalindrome("emilie"), False)
    self.assertTrue(isPalindrome(""))
    self.assertTrue(isPalindrome("1o1"))
    self.assertTrue(isPalindrome("1@1"))

class reverseListTest(unittest.TestCase):
  def testReverseList(self):
    self.assertEqual(reverseList([1,3,5]), [5,3,1])
    self.assertEqual(reverseList([1,3,5,7]), [7,5,3,1])
    self.assertEqual(reverseList([1]), [1])
    self.assertEqual(reverseList([]), [])
    
if __name__ == "__main__":
  unittest.main()