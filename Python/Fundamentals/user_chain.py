class User:
  def __init__(self, user_name, email_address):
    self.name = user_name
    self.email= email_address
    self.account_balance = 0

  #  adding the deposit method
  def make_deposit(self, amount):
    self.account_balance += amount
    return self

  def make_withdraw(self, amount):
    self.account_balance -= amount
    return self
  
  def display_user_balance(self):
    return self.account_balance

  def transfer_money(self, other_user, amount):
    self.account_balance -= amount
    other_user.account_balance += amount
    return self

first_user = User("Chloe Dong","chloedong@gmail.com")
second_user = User("Cindy Zhang","cindyzhang@gmail.com")
third_user = User("Coco Zhao","cocozhao@gmail.com")

# first_user.make_deposit(100)
# first_user.make_deposit(100)
# first_user.make_deposit(100)
# first_user.make_withdraw(150)
# print("The first user account balance is {}". format(first_user.display_user_balance()))
print(first_user.make_deposit(100).make_deposit(100).make_deposit(100).make_withdraw(150).display_user_balance())

# second_user.make_deposit(200)
# second_user.make_deposit(200)
# second_user.make_withdraw(150)
# second_user.make_withdraw(150)
# print("The second user account balance is {}". format(second_user.display_user_balance()))
print(second_user.make_deposit(200).make_deposit(200).make_withdraw(150).make_withdraw(150).display_user_balance())

# third_user.make_deposit(1000)
# third_user.make_withdraw(300)
# third_user.make_withdraw(300)
# third_user.make_withdraw(400)
# print("The third user account balance is {}". format(third_user.display_user_balance()))
print(third_user.make_deposit(1000).make_withdraw(300).make_withdraw(300).make_withdraw(400).display_user_balance())

first_user.transfer_money(third_user, 20)
print("The first user account balance is {}". format(first_user.display_user_balance()))
print("The third user account balance is {}". format(third_user.display_user_balance()))