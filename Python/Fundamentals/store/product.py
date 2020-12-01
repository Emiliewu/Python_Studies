class Product:
  def __init__(self, name, price, category, pku):
    self.name = name
    self.price = price
    self.category = category
    self.pku = pku

  def update_price(self, percent_change, is_increased):
    if is_increased == True:
      self.price += self.price*percent_change
    elif is_increased == False:
      self.price -= self.price*percent_change
    return self

  def print_info(self):
    print("Name: {} - Category: {} - Price: ${} ".format(self.name, self.category, self.price))
    return self
  
