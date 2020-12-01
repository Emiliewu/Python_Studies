class BankAcount:
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

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account = []

  def user_deposite(self, amount, account_name):
    for i in range(0, len(self.account)):
      if self.account[i] == account_name:
        self.account[i].deposit(amount)
        print("Deposite {} to {} and the new balance is {}". format(amount, self.account[i].name, self.account[i].balance))
    return self

  def user_withdraw(self, amount, account_name):
    for i in range(0, len(self.account)):
      if self.account[i] == account_name:
        self.account[i].withdraw(amount)
        print("withdraw {} from {} and the new balance is {} ". format(amount,self.account[i].name, self.account[i].balance))
    return self

  def display_user_balance(self, account_name):
    for i in range(0, len(self.account)):
      if self.account[i] == account_name:
        print("Current balance of {} is {} ". format(self.account[i].name, self.account[i].balance))
    return self


first_user = User("Harry Potter", "harrypotter@gmail.com")
account1 = BankAcount(0.02, "account1", balance = 0)
account2 = BankAcount(0.02, "account2", balance = 0)
first_user.account.append(account1)
first_user.account.append(account2)
first_user.user_deposite(100, account1)
print(first_user.display_user_balance(account1))
first_user.user_withdraw(100, account2)
print(first_user.display_user_balance(account2))
print(first_user.user_deposite(200, account1).user_deposite(200, account2).user_withdraw(10, account1).user_withdraw(10,account1).user_withdraw(50, account2).display_user_balance(account1).display_user_balance(account2))