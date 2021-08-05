"""
A shopping cart application that allows users to add, remove, clear
and show the products in the cart.
"""
cart = []


def add_item(user_item):
    """Adds item selected by a user to the cart"""
    cart.append(user_item)
    print(f"{user_item} successfully added to cart")


def remove_item(user_item):
    """Removes a particular item from the cart"""
    if user_item not in cart:
        print(f"Sorry, {user_item} does not exist in the cart")
    else:
        cart.remove(user_item)
        print(f"{user_item} successfully removed from cart")


def clear_cart(cart):
    """Clears all items from the cart"""
    if len(cart) == 0:
        print("Cart is already EMPTY")
    else:
        cart.clear()
        print("Cart has been successfully cleared")


def show_cart(cart):
    """Displays all items in the cart"""
    if len(cart) == 0:
        print("Sorry, Cart is empty")
    else:
        print(*cart, sep="\n")

# TODO: Add save_cart function

def main():
    """The main program function that handles the program's logic"""
    flag = 1
    valid_actions = ["add", "remove", "clear", "show", "done"]

    while flag == 1:
        user_action = input("Do you want to add, remove, clear or show items on your cart.\
        (Type done after you're finished shopping) ")
        
        user_action.lower()        
        if user_action not in valid_actions:
            print("Please select a either add, remove, clear or show")
        if user_action == "add" or user_action == "remove":
            user_item = input(f"Enter item you would like to {user_action}. ")

        if user_action == "add":
            add_item(user_item)
        elif user_action == "remove":
            remove_item(user_item)
        elif user_action == "clear":
            clear_cart(cart)
        elif user_action == "show":
            show_cart(cart)
        elif user_action == "done":
            prompt = input("Would you like to view your cart before leaving? (Y/N) ")
            if prompt == "Y":
                show_cart(cart)
                print("Thanks for shopping with us, Bye!")
                break
            elif prompt == "N":
                break


main()
