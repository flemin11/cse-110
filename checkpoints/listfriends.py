print("List your friends, when you are finished type 'end'")
friends= []
name= None
while name != 'end':
    name= input("Type a name of your friend:")
    if name != 'end':
        friends.append(name)
print(" ")
print("Your friends are:")

for friend in friends:
    print(friend)