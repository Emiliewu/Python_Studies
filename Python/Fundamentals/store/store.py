class Store:
  def __init__(self, name, list = []):
    self.name = name
    self.list = list

  def add_product(self, new_product):
    self.list.append(new_product)
    return self
  
  def sell_product(self, pku):
    for i in range(0, len(self.list)):
      if pku == self.list[i].pku:
        print("The product {} is removed". format(self.list[i].name))
        del self.list[i]
    return self

  def inflation(self, percent_increase):
    for i in range(0, len(self.list)):
      self.list[i].update_price(percent_increase, True)
      print("Updated {} price: {}".format(self.list[i].name, self.list[i].price))
    return self

  def set_clearance(self, category, percent_discount):
    for i in range(0, len(self.list)):
      if category == self.list[i].category:
        self.list[i].update_price(percent_discount, False)
        print("clearance price of {} is ${}".format(self.list[i].name, self.list[i].price))
    return self
      