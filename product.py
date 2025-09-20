class Product:
    inventory = []
    product_counter = 0

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        cls.product_counter += 1
        new_product = Product(cls.product_counter, name, category, quantity, price, supplier)
        cls.inventory.append(new_product)
        return "Product added successfully"

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for pr in cls.inventory:
            if pr.product_id == product_id:
                if quantity is not None:
                    pr.quantity = quantity
                if price is not None:
                    pr.price = price
                if supplier is not None:
                    pr.supplier = supplier
                return "Product updated successfully"
        return "Product not found"

    @classmethod
    def delete_product(cls, product_id):
        for pr in cls.inventory:
            if pr.product_id == product_id:
                cls.inventory.remove(pr)
                return "Product deleted successfully"
        return "Product not found"


class Order:

    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.produce_id = product_id
        self.quantity = quantity

    def place_order(self):

        return f"Order placed Successfully. Order ID: {self.order_id}"
    
p1 = Product.add_product("PC", "Electronics", 50, 1000, "Supplier A")
print(p1)
p2 = Product.add_product("Short", "Clothing", 100, 25, "Supplier B")
print(p2)
p3 = Product.update_product(1, quantity = 45, price = 950)
print(p3)
p4 = Product.delete_product(2)
print(p4)
order1 = Order(order_id = 1, product_id = 1, quantity = 2)
print(order1.place_order())
