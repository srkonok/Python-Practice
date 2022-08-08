# #Way 1
# class Product:
#     def __init__(self,price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self,value):
#         if value<0:
#             raise ValueError("Invalid Price!")
#         self.__price=value

# product=Product(-50)
# n=product.get_price()
# print(n)

# Way 2 (pythonic way)
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Invalid Price!")
        self.__price = value

product = Product(50)
print(product.price)
