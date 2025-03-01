from products import Product, NonStockedProduct, LimitedProduct
from store import Store
from promotion import PercentageDiscount, SecondItemHalfPrice, BuyTwoGetOneFree


def main():
    """Setup initial stock of inventory"""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create Promotions
    discount_20 = PercentageDiscount("20% Off", 20)
    half_price_promo = SecondItemHalfPrice("Second Item 50% Off")
    bogo_promo = BuyTwoGetOneFree("Buy 2, Get 1 Free")

    # Assign promotions to products
    product_list[0].set_promotion(discount_20)  # MacBook Air M2 - 20% Off
    product_list[1].set_promotion(half_price_promo)  # Bose Earbuds - Second Item 50% Off
    product_list[4].set_promotion(bogo_promo)  # Shipping - Buy 2, Get 1 Free

    """Create the Store instance"""
    best_buy = Store()

    """Add products to the store"""
    for product in product_list:
        best_buy.add_product(product)

    # Start the menu interface
    start(best_buy)  # Pass store object to start()


def start(store):
    """Accept store as a parameter"""
    while True:
        # Show the menu
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Please choose a number: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            products = store.get_all_products()
            if not products:
                print("No active products available.")
            else:
                print("\nAvailable Products:")
                for i, product in enumerate(products, start=1):
                    print(f"{i}. {product.show()}")  # Now products are numbered

        elif choice == 2:
            total_quantity = store.get_total_quantity()
            print(f"Total amount of products in store: {total_quantity}")

        elif choice == 3:
            shopping_list = []
            products = store.get_all_products()

            if not products:
                print("No products available for purchase.")
                continue

            print("\nAvailable Products:")
            for i, product in enumerate(products, start=1):
                print(f"{i}. {product.show()}")

            while True:
                product_input = input("Enter product # (or 'done' to finish): ").strip()

                if product_input.lower() == 'done' or product_input == '':
                    break

                if not product_input.isdigit() or not (1 <= int(product_input) <= len(products)):
                    print("Invalid product number. Please try again.")
                    continue

                product_index = int(product_input) - 1
                product = products[product_index]

                while True:
                    quantity_input = input(f"Enter quantity for {product.name}: ").strip()

                    if quantity_input.lower() == 'done':
                        break  # Return to product selection

                    if not quantity_input.isdigit():
                        print("Please enter a valid numeric quantity.")
                        continue

                    quantity = int(quantity_input)

                    if quantity <= 0:
                        print("Quantity must be greater than zero.")
                        continue

                    if quantity > product.get_quantity():
                        print(f"Not enough stock for {product.name}. Available: {product.get_quantity()}. Try again.")
                        continue  # Retry asking for quantity

                    # Add to shopping list
                    shopping_list.append((product, quantity))
                    break

            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print(f"Total price of your order: ${total_price:.2f}")
                except ValueError as e:
                    print(f"Order Error: {e}")

            continue

        elif choice == 4:
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
