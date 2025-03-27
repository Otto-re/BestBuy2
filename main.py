from store import Store
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100, promotion=SecondHalfPrice(name="Second Half Price")),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500, promotion=ThirdOneFree(name="Buy 2 get 1 free")),
    Product("Google Pixel 7", price=500, quantity=250),
    NonStockedProduct("Windows License", price=125, promotion=PercentDiscount("30% off", discount_percent=30)),
    LimitedProduct("Shipping", price=10, quantity=250, maximum=1, promotion=None)
]

best_buy = Store(product_list)

def start(store):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        chose = input("Please choose a number:")
        print("------")

        if chose == "1":
            idx = 1
            # Indiziere die Produkte ab 1 korrekt
            for product in store.get_all_products():
                print(f"{idx}. {product.show()}")
                idx += 1

        elif chose == "2":
            print(f"Total quantity in store: {store.get_total_quantity()}")

        elif chose == "3":
            shopping_list = []
            print("------")
            for i, product in enumerate(store.get_all_products(), 1):
                print(f"{i}. {product.show()}")

            while True:
                product_choice = input("------\nWhen you want to finish order, enter empty text.\nWhich product # do you want? ")
                if not product_choice:
                    break

                product_choice = int(product_choice) - 1
                if 0 <= product_choice < len(store.get_all_products()):
                    product = store.get_all_products()[product_choice]
                    quantity = int(input(f"What amount do you want? "))
                    shopping_list.append((product, quantity))
                    print("Product added to list!")
                else:
                    print("Invalid product selection.")

            if shopping_list:
                total_price = store.order(shopping_list)
                print(f"Order placed. Total cost: {total_price} dollars.")
            else:
                print("No products were ordered.")

        elif chose == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    start(best_buy)