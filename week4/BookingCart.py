items = []
prices = []

def additem():
    item = input("Enter the name of the item you want to add: ")
    price = float(input("Enter the price of the item: "))
    items.append(item)
    prices.append(price)
    print(item, "added to cart.")

def removeitem():
    if len(items) == 0:
        print("Cart is empty.")
    else:
        item = input("Enter the name of the item you want to remove: ")
        if item in items:
            index = items.index(item)
            removed_item = items.pop(index)
            removed_price = prices.pop(index)
            print(removed_item, "removed from cart.")
        else:
            print("Item not found in cart.")

def viewcart():
    if len(items) == 0:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        i = 0
        while i < len(items):
            print(items[i], "-", prices[i])
            i = i + 1

def viewbill():
    total = 0
    i = 0
    while i < len(prices):
        total = total + prices[i]
        i = i + 1
    print("Total bill amount:", total)

def checkout():
    print("Thank you for using the App!")
    viewcart()
    viewbill()
    print("Bye!")


while True:
    print("------ WELCOME TO BOOKINGCART ------")
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. View Cart")
    print("4. View Bill")
    print("5. Checkout and Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        additem()
    elif choice == 2:
        removeitem()
    elif choice == 3:
        viewcart()
    elif choice == 4:
        viewbill()
    elif choice == 5:
        checkout()
        break
    else:
        print("Invalid choice. Please try again.")

