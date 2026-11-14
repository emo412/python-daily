# Cafe ordering program for two menu items.
# Menu prices are stored as item names and their fixed prices.
menu = {
    "cappuccino": 5.00,
    "latte": 4.50,
    "tea": 3.00,
}

# Collect customer information and the first order.
name = input("Enter your name: ")
item1 = input("What would you like? ").lower().strip()
quantity_item1 = int(input("How many units do you need? "))

# Collect the second order.
item2 = input("What would you like? ").lower().strip()
quantity_item2 = int(input("How many units do you need? "))

# Validate the first menu item and its quantity.
if item1 in menu and quantity_item1 > 0:
    price1 = menu[item1]
    total1 = price1 * quantity_item1

    # Validate the second menu item and its quantity.
    if item2 in menu and quantity_item2 > 0:
        price2 = menu[item2]
        total2 = price2 * quantity_item2
        all_total = total1 + total2

        # Display the customer's order and final bill.
        print(f"Customer: {name}")
        print(f"{item1} x {quantity_item1} = ${total1:.2f}")
        print(f"{item2} x {quantity_item2} = ${total2:.2f}")
        print(f"Total bill: ${all_total:.2f}")
    else:
        print("Invalid second item or quantity.")
else:
    print("Invalid first item or quantity.")
