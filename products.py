class Product:
    def __init__(self, name, price, quantity, active= True):
        if not name:
            raise ValueError("Product name can not be empty.")
        if price < 0:
            raise ValueError("price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active if quantity > 0 else False


    def get_quantity(self):
        """Getter function for quantity.Returns the quantity (int)."""
        return self.quantity


    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity =quantity

        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        """Getter function for active.Returns True if the product is active, otherwise False."""

        return self.active


    def active(self):
        """Activates the product"""
        self.active = True


    def deactivate(self):
        """Deactivates the product"""
        self.active = False


    def show(self):
        """Returns a string that represents the product,"""
        return f"{self.name}, price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")

        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        return total_price

def main():

    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__=="__main__":
    main()