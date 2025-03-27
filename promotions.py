from abc import ABC, abstractmethod

# Abstrakte Klasse für Promotionen
class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name  # Der Name der Promotion, z.B. "30% off", "Buy 2, get 1 free"

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        # Diese Methode muss in jeder spezifischen Promotion-Klasse implementiert werden
        pass

# Prozentualer Rabatt
class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent  # Der Prozentsatz des Rabatts

    def apply_promotion(self, product, quantity: int) -> float:
        # Berechne den Gesamtpreis vor Rabatt
        total_price = product.price * quantity
        # Berechne den Rabatt
        discount = total_price * (self.percent / 100)
        return total_price - discount  # Gesamtpreis nach Rabatt

# Zweiter Artikel zum halben Preis
class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        # Berechne den Gesamtpreis unter Berücksichtigung der Promotion
        if quantity < 2:
            return product.price * quantity

        discounted_price = (quantity // 2) * product.price * 1.5 + (quantity % 2) * product.price
        return discounted_price

# Kauf 2, erhalte 1 gratis
class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        # Berechne den Preis für jedes Set von 3 Artikeln
        discounted_price = (quantity // 3) * 2 * product.price + (quantity % 3) * product.price
        return discounted_price