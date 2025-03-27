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
        if self.promotion:
            return self.promotion.name
        return "None"

    def show(self):
        promo_text = f", Promotion: {self.get_promotion()}" if self.promotion else ""
        if isinstance(self, NonStockedProduct):
            return f"{self.name}, Price: ${self.price}, Promotion: {self.get_promotion()} (Non-Stocked)"
        elif isinstance(self, LimitedProduct):
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Max allowed: {self.maximum}, Promotion: {self.get_promotion()}"
        else:
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promo_text}"

    def buy(self, quantity):
        if self.quantity < quantity:
            raise ValueError("Not enough stock available")
        self.quantity -= quantity
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price, promotion=None):
        super().__init__(name, price, quantity=0, promotion=promotion)

    def get_quantity(self):
        return 0

    def show(self):
        return f"{self.name}, Price: ${self.price}, Promotion: {self.get_promotion()} (Non-Stocked)"

    def buy(self, quantity):
        raise ValueError("Cannot buy non-stocked product")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum, promotion=None):
        super().__init__(name, price, quantity, promotion)
        self.maximum = maximum

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Max allowed: {self.maximum}, Promotion: {self.get_promotion()}"

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of this product")

        if self.quantity < quantity:
            raise ValueError("Not enough stock available")

        self.quantity -= quantity

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)  # Korrekt angewendet

        return self.price * quantity