from promotions import Promotion, PercentDiscount, SecondHalfPrice, ThirdOneFree

class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input values")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = False if quantity == 0 else True
        self.promotion = None

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

    def set_promotion(self, promotion):
        self.promotion = promotion  # Setzt eine Promotion für das Produkt

    def get_promotion(self):
        return self.promotion  # Gibt die aktuelle Promotion des Produkts zurück

    def show(self) -> str:
        promo_text = f" | Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise ValueError("Not enough items available")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def show(self) -> str:
        return f"{self.name}, Price: {self.price} (Non-Stocked)"

    def buy(self, quantity) -> float:
        # Nicht gelagerte Produkte können nicht gekauft werden
        raise ValueError(f"{self.name} is not available for purchase.")

class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} units per order")
        if quantity > self.quantity:
            raise ValueError(f"Not enough items available. Only {self.quantity} left.")
        return super().buy(quantity)

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max allowed: {self.maximum}"