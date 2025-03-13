import unittest

from ..promotion import PercentageDiscount, SecondItemHalfPrice, BuyTwoGetOneFree
from ..products import Product


class TestPromotions(unittest.TestCase):

    def setUp(self):
        self.product = Product("Test Product", 100, 10)

    def test_percentage_discount(self):
        promo = PercentageDiscount("20% Off", 20)
        self.product.set_promotion(promo)
        discounted_price = promo.apply_promotion(self.product, 1)
        self.assertEqual(discounted_price, 80)

    def test_second_item_half_price(self):
        promo = SecondItemHalfPrice("Second Half Price")
        self.product.set_promotion(promo)
        price = promo.apply_promotion(self.product, 2)
        expected = self.product.price + (self.product.price * 0.5)
        self.assertEqual(price, expected)

    def test_buy_two_get_one_free(self):
        promo = BuyTwoGetOneFree("Buy 2 Get 1 Free")
        self.product.set_promotion(promo)
        price = promo.apply_promotion(self.product, 3)
        expected = 2 * self.product.price
        self.assertEqual(price, expected)


if __name__ == '__main__':
    unittest.main()
