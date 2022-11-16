secret_word= "goober"
len_count= len(secret_word)
count= 1
guess= ''
i= 0
print("Welcome to the secret word game. Try and guess the word in as little as guesses as you can. Good luck!")
print(" ")
print("Your hint is: _ _ _ _ _ _")
print(" ")
guess = input("What is your first guess of the word?")
if guess != secret_word:
    count= count + 1
    while len(guess) != len(secret_word):
        count = + 1
        print(f"That word does not have {len_count} letters")
        guess = input("What is your guess of the word?")
    print("That is not the right word!")

while guess.lower() != secret_word:
    print('Your hint is:', end= '')
    for i in range(len(guess)):
        if i < len(secret_word) and guess[i] == secret_word[i]:
            print(guess[i].upper() + '', end='')
        elif guess[i] in secret_word:
            print(guess[i] + '', end="")
        else:
            print('_ ', end='')
    while  i < len(secret_word) - 1:
        print('_ ', end='')
        i += 1
    guess = input('\nWhat is your guess of the word?')
    while len(guess) != len(secret_word):
        count = count +1
        print(f'That word does not have {len_count} letters')
        guess = input('What is your guess of the word?')
    if guess != secret_word:
        count = count + 1
        print('That is not the right word!')
    else:
        break

print("Kid you guessed it, you was right!! Congrats!!!")
if count == 1:
    print("Yeet Yeet Skeet. Your as fly as lil peep. Gottem catch em' with one leap. Skitti Beep Bop Pow, you wipe the furrow off your brow. That was lit.")
else:
    print(f'It took you {count} tries! Great job!')
