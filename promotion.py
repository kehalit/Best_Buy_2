from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentageDiscount(Promotion):
    def __init__(self, name, discount_percent):
        super().__init__(name)
        if not (0 <= discount_percent <= 100):
            raise ValueError("Discount percent must be between 0 and 100.")

        self.discount_percent = discount_percent


    def apply_promotion(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        discount = product.price * (self.discount_percent / 100)
        return (product.price - discount) * quantity

class SecondItemHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class BuyTwoGetOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        paid_items = (quantity // 3) * 2 + (quantity % 3)
        return paid_items * product.price
