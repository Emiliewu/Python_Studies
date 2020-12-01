class BankAcount:
  def __init__(self, int_rate, balance=0):
    self.int_rate = int_rate
    self.balance = balance
  
  def deposit(self, amount):
    self.balance += amount
    return self
  
  def withdraw(self, amount):
    if self.balance < amount:
      self.balance -= 5
      print("insufficient funds: Charging a $5 fee")
    else:
      self.balance -= amount
    return self
  
  def display_account_info(self):
    print("Balance: ${}".format(self.balance))
    return self
  
  def yield_interest(self):
    if self.balance > 0:
      self.balance += self.int_rate*self.balance
    return self

first_account = BankAcount(0.01, 1000)
second_account = BankAcount(0.01)

print(first_account.deposit(100).deposit(100).deposit(100).withdraw(300).yield_interest().display_account_info())

print(second_account.deposit(500).deposit(500).withdraw(200).withdraw(200).withdraw(300).withdraw(301).yield_interest().display_account_info())