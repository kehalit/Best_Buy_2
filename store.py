from products import Product,NonStockedProduct


class Store:
    """Represents a store that holds and manages products."""

    def __init__(self):
        """Initializes an empty store with a list of products."""
        self.products = []

    def add_product(self, product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self):
        """Calculates and returns the total quantity of all products in the store."""
        total = 0
        for product in self.products:
            if isinstance(product, NonStockedProduct):  # Skip NonStockedProduct for quantity
                continue  # Skip products with unlimited stock
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """Returns a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """Processes an order given a list of (product, quantity) tuples.
        Buys the specified quantities of products and returns the total price of the order.

        Raises:
            ValueError: If a product does not have enough stock.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product.is_active() and product.get_quantity() >= quantity:
                total_price += product.buy(quantity)
            else:
                raise ValueError(f"Not enough stock for {product.name}.")

        return total_price


def main():
    """Creates a store, adds products, and tests store functionalities."""
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


if __name__ == "__main__":
    main()
