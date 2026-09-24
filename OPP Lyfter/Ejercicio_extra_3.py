class Product:

    def __init__(self, name, price, amount):
            self.name = name
            self.price = price
            self.amount = amount

    def calculate_subtotal(self):
        return self.price * self.amount

class Inventory:

    def __init__(self, ):
        self.products =[]

    def add_product(self,product):
        self.products.append(product)

    def show_products(self):
        if not self.products:
            print('The inventory is empty')

        for prod in self.products:
            print(f'Product {prod.name} | Price {prod.price} | Amount {prod.amount}')   

    def calculate_total_value_of_inventory(self):
        total = 0
        for prod in self.products:
            total += prod.calculate_subtotal()
        return total


product_1 = Product("Mouse", 5000, 3)
product_2 = Product("Teclado", 8000, 2)
my_inventory = Inventory()
my_inventory.add_product(product_1)
my_inventory.add_product(product_2)


print(f'{my_inventory.calculate_total_value_of_inventory()}')