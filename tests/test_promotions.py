import unittest
from ..products import Product
from ..promotion import PercentageDiscount, SecondItemHalfPrice, BuyTwoGetOneFree


class TestPromotions(unittest.TestCase):

    def setUp(self):
        self.product = Product("Test Product", price=100, quantity=50)

    def test_percentage_discount(self):
        promo = PercentageDiscount("10% Off", 10)
        self.product.set_promotion(promo)

        discounted_price = promo.apply_promotion(self.product, 1)
        self.assertEqual(discounted_price, 90)

    def test_second_item_half_price(self):
        promo = SecondItemHalfPrice("Second Half Price")
        self.product.set_promotion(promo)

        # Buy 1 = full price
        price_1 = promo.apply_promotion(self.product, 1)
        self.assertEqual(price_1, 100)

        # Buy 2 = 1 full + 1 half
        price_2 = promo.apply_promotion(self.product, 2)
        self.assertEqual(price_2, 100 + 50)

        # Buy 3 = 2 full + 1 half
        price_3 = promo.apply_promotion(self.product, 3)
        self.assertEqual(price_3, 100 + 100 + 50)

    def test_buy_two_get_one_free(self):
        promo = BuyTwoGetOneFree("Buy 2 Get 1 Free")
        self.product.set_promotion(promo)

        # Buy 1 = full price
        price_1 = promo.apply_promotion(self.product, 1)
        self.assertEqual(price_1, 100)

        # Buy 2 = 2 full price
        price_2 = promo.apply_promotion(self.product, 2)
        self.assertEqual(price_2, 200)

        # Buy 3 = 2 full price + 1 free
        price_3 = promo.apply_promotion(self.product, 3)
        self.assertEqual(price_3, 200)

        # Buy 6 = 4 paid, 2 free
        price_6 = promo.apply_promotion(self.product, 6)
        self.assertEqual(price_6, 400)


if __name__ == '__main__':
    unittest.main()
