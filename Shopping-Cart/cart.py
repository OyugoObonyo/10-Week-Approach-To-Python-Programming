"""
A shopping cart application that allows users to add, remove, clear, and show the products in the cart.
"""
cart = []

def add_item(user_item):
    """Adds item selected by a user to the cart"""
    cart.push(user_item)
    print(f"{user_item} successfully added to cart")

def remove_item(user_item):
    """Removes a particular item from the cart"""
    if user_item not in cart:
       print(f"Sorry, {user_item} does not exist in the cart")
    else: 
       cart.remove(user_item)
       print(f"{user_item} successfully removed from cart"

def clear_cart(cart):
    """Clears all items from the cart"""
    if len(cart) == 0:
       print("Cart is already EMPTY")
    else:
       cart.clear()
       print("Cart has been successfully cleared")

def show_cart(cart):
    """Displays all items in the cart"""
    for item in cart:
        position = 1
        print(f"{position}: {item}")
        position += 1

def main():
    """The main program function that handles the program's logic"""
    user_action = input("You can either add,remove,clear or show items on your cart. Select an option.  ")
    user_action.lower()
    user_item = input(f"Enter item you would like to {user_action}. ")
    
    if user_action == "add":
        add_item(user_item)
    elif user_action == "remove":
        remove_item(user_item)
    elif user_action == "clear":
        clear_cart(cart)
    elif user_action == "show":
        show_cart(cart)
    
main()
