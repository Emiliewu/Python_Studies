x = [ [5,2,3], [10,8,9] ] 
students = [
  {'first_name':  'Michael', 'last_name' : 'Jordan'},
  {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
  'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
  'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0][2] = "Bryant"
print(students)
# # In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
# # Change the value 20 in z to 30
z[0]["y"] = 30
print(z)

# -----------------------------------------


students = [
  {'first_name':  'Michael', 'last_name' : 'Jordan'},
  {'first_name' : 'John', 'last_name' : 'Rosales'},
  {'first_name' : 'Mark', 'last_name' : 'Guillen'},
  {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# # Create a function iterateDictionary(some_list) that, 
# # given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
def iterateDictionary(some_list):
  for item in some_list:
    list = []
    for key, value in item.items():
      list.append('{} - {}'.format(key, value))
    print(', '.join(list))
iterateDictionary(students)
    
# # Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# # the function prints the value stored in that key for each dictionary.
def iterateDictionary2(key_name, some_list):
  for item in some_list:
    print(item[key_name])
iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

# ----------------------------------

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 
dojo = {
  'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
  'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
  for key, value in some_dict.items():
    print("{} {}".format(len(value), key.upper()))
    for item in value:
      print(item)
    print()

printInfo(dojo)
