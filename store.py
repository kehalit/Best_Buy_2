from products import Product

class Store:
    def __init__(self):
        self.products = []


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        """Removes a product from store."""
        self.products.remove(product)


    def get_total_quantity(self):
        """Returns how many items are in the store in total."""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        """Returns all products in the store that are active."""
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list):
        """Gets a list of tuples, where each tuple has 2 items:product (Product class) and quantity (int).
          Buys the products and returns the total price of the order."""
        total_price = 0.0
        for product, quantity in shopping_list:
            if product.is_active() and product.get_quantity() >= quantity:
                total_price += product.buy(quantity)
            else:
                raise ValueError(f"Not enough stock for {product.name}.")

        return total_price


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store()
    for product in product_list:
        best_buy.add_product(product)

        # Test methods
    print("Total quantity in store:", best_buy.get_total_quantity())  # Total quantity of all products
    print("Order total price:", best_buy.order([(product_list[0], 1), (product_list[1], 2)]))  # Example order

if __name__== "__main__":
    main()


