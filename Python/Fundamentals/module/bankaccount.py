class BankAccount:
  def __init__(self, int_rate, name, balance=0,):
    self.int_rate = int_rate
    self.balance = balance
    self.name = name
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