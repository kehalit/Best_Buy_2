from products import Product, NonStockedProduct, LimitedProduct
from store import Store


def main():
    """Setup initial stock of inventory"""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

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
        print("Store Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Please choose a number: "))
        except ValueError:
            print("Invalid choice. Please choose a valid option.")
            continue

        if choice == 1:
            products = store.get_all_products()
            if not products:
                print("No active products available.")
            else:
                for product in products:
                    print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
        elif choice == 2:
            total_quantity = store.get_total_quantity()
            print(f"Total amount of products in store: {total_quantity}")
        elif choice == 3:
            shopping_list = []
            print("Enter products to buy (name and quantity). Type 'done' to finish.")

            product_stock = {p.name: p.quantity for p in store.get_all_products()}

            while True:
                product_name = input("Enter product name: ").strip()
                if product_name.lower() == 'done' or product_name == '':
                    break

                if product_name not in product_stock:
                    print(f"Product '{product_name}' not found. Please try again.")
                    continue

                while True:
                    quantity_input = input(f"Enter quantity of {product_name}: ").strip()

                    if quantity_input.lower() == 'done':
                        print("Returning to product selection.")
                        break  # Go back to product selection

                    if not quantity_input.isdigit():
                        print("Please enter a valid numeric quantity.")
                        continue

                    quantity = int(quantity_input)

                    if quantity <= 0:
                        print("Quantity must be greater than zero.")
                        continue

                    if quantity > product_stock[product_name]:
                        print(f"Not enough stock for {product_name}. Order cannot be completed. Try again.")
                        continue  # Retry asking for quantity

                    product_stock[product_name] -= quantity

                    product = next(p for p in store.get_all_products() if p.name == product_name)
                    shopping_list.append((product, quantity))
                    break  # Exit quantity loop and return to product selection

            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print(f"Total price of your order: ${total_price:.2f}")
                except ValueError as e:
                    print(f"Order Error: {e}")

            continue  # Return to menu after completing order

        elif choice == 4:
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()










