from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Berechnet den Rabatt oder die Promotion für ein Produkt"""
        pass

class PercentDiscount(Promotion):
    def __init__(self, name, discount_percent):
        super().__init__(name)
        self.discount_percent = discount_percent

    def apply_promotion(self, product, quantity):
        total_price = product.price * quantity
        discount = total_price * (self.discount_percent / 100)
        return total_price - discount

class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity >= 2:
            total_price = product.price * quantity - product.price / 2  # Preis des zweiten Produkts halbiert
        else:
            total_price = product.price * quantity
        return total_price

class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity >= 3:
            total_price = product.price * (quantity - (quantity // 3))  # Ein Produkt kostenlos für jedes dritte
        else:
            total_price = product.price * quantity
        return total_price