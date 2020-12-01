class Underscore:
    def map(self, iterable, callback):
        #  your code here
        for i in range(0, len(iterable)):
          iterable[i] = callback(iterable[i])
        return iterable
    def find(self, iterable, callback):
        # your code here
        for i in range(1, len(iterable)-1):
          temp = callback(iterable[i])
          if temp == True:
            return iterable[i]
    def filter(self, iterable, callback):
        result = []
        # your code
        for i in range(0, len(iterable)):
          temp = callback(iterable[i])
          if temp == True:
            result.append(iterable[i])
        return result
    def reject(self, iterable, callback):
        # your code
        result = []
        for i in range(0, len(iterable)):
          temp = callback(iterable[i])
          if temp == False:
            result.append(iterable[i])
        return result
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)
# should return [2, 4, 6] after you finish implementing the code above
map_value = _.map([1,2,3], lambda x: x*2) # should return [2,4,6]
print(map_value)
find_value = _.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
print(find_value)
# _.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
reject_value = _.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]
print(reject_value)