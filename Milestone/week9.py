print("Welcome to the Shopping Cart Program!")
shopping= []
prices=[]
action= ''
while action != 5:
    print("Please select one of the following:")
    print('1. Add item')
    print('2. View Cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    action= int(input("Please enter an action:"))
    if action == 1:
        add_item= input("What item would you like to add?")
        if add_item != "quit":
            price= float(input(f"What is the price of '{add_item}'?"))

            shopping.append(add_item)
            prices.append(price)
            print(f"'{add_item}' has been added to the cart.")

    elif action == 2:
        print("The contents of the shopping cart are:")
        for i in range(len(shopping)):

            print(f"{i + 1}. {shopping[i]} - ${prices[i]:.2f}")
    elif action == 3:
        item = int(input("Which item would you like to remove?"))
        shopping.pop(item-1)
        print("Item Removed.")
    elif action == 4:
        total= 0
        for items in prices: 
            total= total + price
        print(f"The total is ${total:.2f}")
print("Thank you for shopping. We hope to see you again, goodbye.")


