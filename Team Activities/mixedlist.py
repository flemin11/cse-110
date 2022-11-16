print("Enter the names and blances of bank accounts (type: quit when done)")
account= []
balances = []
item= None
while item != 'quit':
    item= input("What is the name of this account?")
    if item != "quit":
        balance = float(input("What is the balance?"))


    account.append(item)
    balances.append(balance)

total= 0
print("\nAccount Information:")

for i in range(len(account)):
    if account[i] != "quit":
        print(f"{account[i]}- {balances[i]}")
    

total += balances[i]
average = total / len(balances)
print(" ")
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")
