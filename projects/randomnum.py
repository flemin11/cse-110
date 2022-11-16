import random
magic_number= random.randint(1, 100)
print("Try to determine the magic number!")
guess= -1

while guess != magic_number:
    guess = int(input("What is your guess?"))

    if guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    else:
        print("Congrats you guessed it!!!")