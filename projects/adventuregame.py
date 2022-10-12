from secrets import choice


first_choice= input("You are walking through a dark spooky jungle and look down and spot two items: a KNIFE and a FLASHLIGHT. Which one do you want to pick up?")
if first_choice.lower() == 'knife':
    knife= input("You now have a weapon but no light. A cougar snuck up on you and scratched you. Do you want to RUN or use your KNIFE to fight back?")
elif first_choice.lower() == 'flashlight':
    flashlight = input("You picked up the flashlight and began walking \
through the now lit jungle. You avoid most dangers but are faced with a huge \
rock wall. Do you want to CLIMB, WALK AROUND or CALL for help?")
else:
    print("That was not an option. Try again.")
