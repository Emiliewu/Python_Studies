from product import Product
from store import Store
# create an store instance
store1 = Store("Hudson Bay")
    # create some product instances
product1 = Product("bag", 100, "women", "123456701")
store1.add_product(product1)
product2 = Product("boots", 200, "women", "123456702")
store1.add_product(product2)
product3 = Product("boots", 200, "men", "123456703")
store1.add_product(product3)
product4 = Product("necklace", 400, "jewlery", "123456704")
store1.add_product(product4)
product5 = Product("watch", 400, "jewlery", "123456705")
store1.add_product(product5)
# sell the product
print(store1.sell_product("123456705"))

# display product information
print(store1.list[1].print_info())
print(store1.list[0].print_info())

# inflation
store1.inflation(0.05)


# cleareance
store1.set_clearance("jewlery", 0.20)
