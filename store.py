class Store:
    def __init__(self, products):
        self.products = products

    def get_all_products(self):
        return self.products

    def get_total_quantity(self):
        return sum(product.quantity for product in self.products)

    def order(self, shopping_list):
        total_cost = 0
        for product, quantity in shopping_list:
            # Wir rufen die Methode apply_promotion auf
            if product.promotion:
                total_cost += product.promotion.apply_promotion(product, quantity)
            else:
                total_cost += product.price * quantity
        return total_cost