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
        from promotion import Promotion  # Avoid circular import
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
        """Returns a string representation of the product including its name, price, quantity, and promotion (if any)."""
        quantity_str = "Unlimited" if isinstance(self, NonStockedProduct) else self.quantity
        promotion_str = self.promotion.name if self.promotion else "None"

        if isinstance(self, LimitedProduct):
            return (f"{self.name}, Price: ${self.price}, Quantity: {quantity_str}, "
                    f"Limited to {self.maximum} per order!, Promotion: {promotion_str}")

        return f"{self.name}, Price: ${self.price}, Quantity: {quantity_str}, Promotion: {promotion_str}"

    def buy(self, quantity):
        """Processes a purchase of the given quantity of the product and returns the total price."""
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = (self.promotion.apply_promotion(self, quantity)
                       if self.promotion else self.price * quantity)
        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """Represents a product that is not stocked (e.g., digital goods)."""

    def __init__(self, name, price):
        """Initializes a non-stocked product with a name and price."""
        super().__init__(name, price, quantity=0)

    def get_quantity(self):
        return float('inf')

    def is_active(self):
        """Non-stocked products should always be active."""
        return True

    def buy(self, quantity):
        """Processes a purchase of the given quantity and returns the total price."""
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return quantity * self.price

    def show(self):
        """Returns a string representation of the non-stocked product."""
        promotion_str = self.promotion.name if self.promotion else "None"
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited, Promotion: {promotion_str}"


class LimitedProduct(Product):
    """Represents a product with a purchase limit per order."""

    def __init__(self, name, price, quantity, maximum):
        """Initializes the limited product."""
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum per order must be greater than zero.")
        self.maximum = maximum

    def buy(self, quantity):
        """Processes a purchase of the given quantity, enforcing the maximum purchase limit."""
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} per order.")
        return super().buy(quantity)

    def show(self):
        """Returns a string representation of the limited product."""
        promotion_str = self.promotion.name if self.promotion else "None"
        return (f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, "
                f"Limited to {self.maximum} per order!, Promotion: {promotion_str}")


# Optional testing section
if __name__ == "__main__":
    # Regular Product
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    print(bose.show())

    # Non-stocked Product
    win = NonStockedProduct("Windows License", price=125)
    print(win.show())

    # Limited Product
    ship = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    print(ship.show())

    # Buying examples
    print("Buying Bose Earbuds:", bose.buy(2))  # Should subtract quantity
    print("Remaining Bose quantity:", bose.get_quantity())

    print("Buying Windows License:", win.buy(5))
    print("Buying Shipping:", ship.buy(1))
