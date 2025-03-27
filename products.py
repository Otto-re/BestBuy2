class Product:
    def __init__(self, name, price, quantity=0, promotion=None):
        if not name or price < 0 or (quantity is not None and quantity < 0):
            raise ValueError("Invalid input values")
        self.name = name
        self.price = price
        self.quantity = quantity if quantity is not None else 0
        self.active = self.quantity > 0
        self.promotion = promotion

    def is_active(self):
        return self.active

    def get_quantity(self):
        return self.quantity

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion.name if self.promotion else "None"

    def show(self):
        promo_text = f", Promotion: {self.get_promotion()}" if self.promotion else ""
        return f"{self.name}, Price: {self.price} (Non-Stocked)" if isinstance(self, NonStockedProduct) else f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_text}"

    def buy(self, quantity):
        if self.quantity < quantity:
            raise ValueError("Not enough stock available.")
        self.quantity -= quantity
        self.active = self.quantity > 0
        total_price = self.price * quantity
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price, promotion=None):
        super().__init__(name, price, quantity=0, promotion=promotion)

    def get_quantity(self):
        return 0

    def show(self):
        return f"{self.name}, Price: {self.price} (Non-Stocked)"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum, promotion=None):
        super().__init__(name, price, quantity, promotion)
        self.maximum = maximum

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max allowed: {self.maximum}"

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of this product.")
        return super().buy(quantity)