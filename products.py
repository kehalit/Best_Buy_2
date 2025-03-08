class Product:
    """Represents a product with a name, price, quantity, and an optional promotion."""

    def __init__(self, name, price, quantity, active=True):
        """Initializes a product with a name, price, quantity, and active status."""
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active if quantity > 0 else False
        self.promotion = None  # Promotion will be assigned later

    def get_quantity(self):
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the product quantity and deactivates it if quantity becomes zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def get_promotion(self):
        """Returns the current promotion applied to the product, if any."""
        return self.promotion

    def set_promotion(self, promotion):
        """Sets a promotion for the product."""
        from promotion import Promotion  # Import inside the method to avoid circular import
        if not isinstance(promotion, Promotion):
            raise TypeError("Invalid promotion type.")
        self.promotion = promotion

    def remove_promotion(self):
        """Removes any promotion applied to the product."""
        self.promotion = None

    def is_active(self):
        """Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Returns a string representation of the product including its name, price,
        quantity, and promotion (if any)."""
        promo_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_text}"

    def buy(self, quantity):
        """Processes a purchase of the given quantity of the product and returns the total price."""
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.promotion.apply_promotion(self, quantity) if self.promotion else self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """Represents a product that is not stocked (e.g., digital goods)."""

    def __init__(self, name, price):
        """Initializes a non-stocked product with a name and price."""
        super().__init__(name, price, quantity=0)

    def buy(self, quantity):
        """Processes a purchase of the given quantity and returns the total price."""
        return quantity * self.price

    def show(self):
        """Returns a string representation of the non-stocked product."""
        return f"{self.name} (Non-Stocked), Price: {self.price}"


class LimitedProduct(Product):


    def __init__(self, name, price, quantity, maximum):
        """Represents a product with a purchase limit per order."""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """Processes a purchase of the given quantity, enforcing the maximum purchase limit."""
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} per order.")
        return super().buy(quantity)

    def show(self):
        """Returns a string representation of the limited product."""
        return f"{self.name} (Limited: Max {self.maximum} per order), Price: {self.price}, Quantity: {self.quantity}"


# Testing the functionality
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    win = NonStockedProduct("Windows License", price=125)
    ship = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    print(win.buy(50))
    print(ship.buy(1))
    print(win.is_active())

    print(win.show())
    print(ship.show())

    bose.set_quantity(1000)
    print(bose.show())
