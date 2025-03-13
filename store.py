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



if __name__ == "__main__":
    main()
