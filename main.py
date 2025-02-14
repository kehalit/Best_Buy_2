from products import Product
from store import Store


def main():
    """Setup initial stock of inventory"""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
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
            for product in products:
                print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
        elif choice == 2:
            total_quantity = store.get_total_quantity()
            print(f"Total amount of products in store: {total_quantity}")
        elif choice == 3:

            try:
                shopping_list = []
                print("Enter products to buy (name and quantity). Type 'done' to finish.")
                while True:
                    product_name = input("Enter product name: ")
                    if product_name.lower() == 'done':
                        break
                    quantity = int(input(f"Enter quantity of {product_name}: "))
                    products = store.get_all_products()  # Correct method call on the instance
                    product = next((p for p in products if p.name == product_name), None)
                    if product:
                        shopping_list.append((product, quantity))
                    else:
                        print(f"Product '{product_name}' not found.")

                if shopping_list:
                    total_price = store.order(shopping_list)  # Correct method call on the instance
                    print(f"Total price of your order: ${total_price:.2f}")
            except Exception as e:
                print(f"Error in placing order: {e}")
        elif choice == 4:
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
