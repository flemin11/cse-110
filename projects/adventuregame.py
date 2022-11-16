print("Welcome to The Adventure Game. Choose your path and see if you survive the dangers of the jungle!")
print("--------------------------------------------------------------------------------------------------")
first_choice= input("You are walking through a dark spooky jungle and look down and spot two items: a KNIFE and a FLASHLIGHT. Which one do you want to pick up?")
if first_choice.lower() == 'knife':
    knife= input("You now have a weapon but no light. A cougar snuck up on you and scratched you. Do you want to RUN or use your knife to FIGHT back?")
    if knife.lower()== 'run':
        run1= input("You start running but trip over a rock! You're lying there hurt. Do you want to REST or KEEP RUNNING?")
        if run1.lower()== 'rest':
            print("You get eaten by the cougar. Shouldn't have taken a break. You're in a jungle. Game over.")
        elif run1.lower()== 'keep running':
            print("Good job for continuing onward. You escaped the jungle and made it out alive. You live to see another day.")
    if knife.lower()== 'fight':
        fight= input("You slash the cougar several times and he's down. You keep walking and see some vines. Do you want to SWING or start a FIRE?")
        if fight.lower()== 'swing':
            print("Turns out your not a monkey and you fell straight into some trees and got hit and died. Game Over.")
        elif fight.lower()== 'fire':
            print("You start a fire and attract every creature in the jungle. You are first bitten by a snake and then devoured and dragged deep into the jungle. Game over.")

elif first_choice.lower() == 'flashlight':
    flashlight = input("You picked up the flashlight and began walking through the now lit jungle. You avoid most dangers but are faced with a huge rock wall. Do you want to CLIMB, WALK AROUND or CALL for help?")
    if flashlight.lower()== 'climb':
        climb= input("You start climbing with rope but its old and you hear tearing and snapping sounds. You anxiously hurry to climb. Do you want to TRY to keep climbing or get off the rope and FREE SOLO?")
        if climb.lower()== 'try':
            print("The rope snaps and you fall to your death. Game Over.")
        elif climb.lower()== 'free solo':
            print("It was a hard and tough climb but you made it to the top. You continue on your journey and live to see another day.")
    if flashlight.lower()== 'walk around':
        walk= input("Your walking around but you stuble upon a lions den. Do you SNEAK past the lions or GO BACK and try climbing the rock wall?")
        if walk.lower()== 'sneak':
            print("You try to sneak past the lions but you trip over a tree root and stumble right into their den. The lions eat you alive. Game over.")
        elif walk.lower()== 'go back':     
            print("You go back to the rock wall and you try to climb but the rope thats holding you snaps and you plummet to your death. Game over.")
    if flashlight.lower()== 'call':
        call= input("You pull out a satelite phone and try to call for help. You can't get a signal and are just stuck trying to figure it out. Do you TRY AGAIN or start the CLIMB to the top to get a better signal.")
        if call.lower()== 'call':
            print("You are sitting prey for every predator in the jungle. A crocodile comes out of the river next to you and pulls you under and you are killed under the water. Game over.")
        climb= input("You start climbing with rope but its old and you here tearing and snapping sounds. You anxiously hurry to climb. Do you want to TRY to keep climbing or get off the rope and FREE SOLO?")
        if climb.lower()== 'try':
            print("The rope snaps and you fall to your death. Game Over.")
        elif climb.lower()== 'free solo':
            print("It was a hard and tough climb but you made it to the top. You continue on your journey and live to see another day.")
else:
    print("That was not an option. Try again.")

print("Thanks for playing. Try again for a different adventure.")




