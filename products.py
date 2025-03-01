class Product:
    def __init__(self, name, price, quantity, active=True):
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
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        from promotion import Promotion  # Import inside the method to avoid circular import
        if not isinstance(promotion, Promotion):
            raise TypeError("Invalid promotion type.")
        self.promotion = promotion

    def remove_promotion(self):
        self.promotion = None

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        promo_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_text}"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.promotion.apply_promotion(self, quantity) if self.promotion else self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def buy(self, quantity):
        return quantity * self.price

    def show(self):
        return f"{self.name} (Non-Stocked), Price: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} per order.")
        return super().buy(quantity)

    def show(self):
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
