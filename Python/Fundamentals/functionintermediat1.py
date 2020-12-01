import random
import math
def randInt(min=0, max=100):
  if min > max:
    print("max is smaller than minimum")
  if max <= 0:
    num = max - random.random() * (max-min+1)
    return math.ceil(num)
  else:
    num = random.random() * (max-min+1) + min
    return math.floor(num)
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=100, max=50))
print(randInt(min = -40, max=-20))
print(randInt(-2,0))
# print(randInt()) 		    # should print a random integer between 0 to 100
# print(randInt(max=50))    # should print a random integer between 0 to 50
# print(randInt(min=50)) 	    # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

