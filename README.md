# Store Management System

This project simulates a store's inventory system where users can view products, check store totals, and place orders. The store supports various types of products and promotional offers, including:

- Regular stocked products
- Non-stocked products (e.g., software licenses)
- Limited-quantity products (e.g., shipping)
- Promotions like percentage discounts, second-item-half-price, and buy-two-get-one-free.

## Features

- **Product Catalog**: List and manage products, including product name, price, and quantity.
- **Promotions**: Apply promotions like percentage discounts, second-item-half-price, and buy-two-get-one-free to products.
- **Order Management**: Users can place orders by selecting products and specifying quantities. The system calculates the total price with applied promotions.
- **Store Overview**: View the total amount of products in the store.

## Requirements

To run this project, you'll need Python 3.x installed. The program also depends on standard Python libraries.

## Setup

1. Clone the repository:
   git clone
2.Run the program:
  python main.py
3. Follow the interactive menu to view products, check totals, or make an order.

## Code Structure
  - products.py: Defines classes for different types of products:
  - Product: Regular products with price and stock quantity.
  - NonStockedProduct: Products that don't require stock tracking, like digital products or services.
  - LimitedProduct: Products that have a maximum quantity limit.

- store.py: Contains the Store class responsible for managing the store's inventory, product listings, and order processing.

- promotion.py: Defines promotional offers, including:

    - PercentageDiscount: A discount of a specified percentage.

    - SecondItemHalfPrice: A promotion that offers a 50% discount on the second item in a purchase.

    - BuyTwoGetOneFree: A promotion where the third item in a set of three is free.

-main.py: The entry point of the program, which initializes the store with products, sets promotions, and provides the interactive menu for the user.

