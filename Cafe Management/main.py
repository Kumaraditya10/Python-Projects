# Updated Menu with your new items
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
    'Chai': 10,
    'Biscuit': 5,
    'Manchurian': 40,
    'Noodles': 40,
    'Momos': 20,
    'Cold Coffee': 20,
    'Cold Drink': 40,
    'Chili Potato': 50
}

# Greet and Display Menu dynamically
print("Welcome to Python Restaurant")
print("----------------------------")
for item, price in menu.items():
    print(f"{item}: Rs {price}")
print("----------------------------")

order_total = 0

# First Item Order
item_1 = input("Enter the name of the item you want to order = ").title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Sorry, '{item_1}' is not available yet!")

# Asking for a second item
another_order = input("Do you want to add another item? (Yes/No) ").lower()

if another_order == "yes":
    item_2 = input("Enter the name of the second item = ").title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to order.")
    else:
        print(f"Sorry, '{item_2}' is not available!")

# Final Bill
print("----------------------------")
print(f"The total amount to pay is: Rs {order_total}")
print("Thank you for visiting!")