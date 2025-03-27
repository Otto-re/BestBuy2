class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input values")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise ValueError("Not enough items available")
        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def show(self) -> str:
        return f"{self.name}, Price: {self.price} (Non-Stocked)"

class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} units")
        return super().buy(quantity)

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max allowed: {self.maximum}"