can_ride = False
print("Welocme to the Incredi-Coaster. please indicate the following:")
age = int(input("What is the age of the first rider? "))
height = int(input("What is the height of the first rider? "))
is_second_rider = input("Is there a second rider (yes/no)? ")
if age>=12 and age< 18:
    golden1= input("Does this rider have a golden passport (yes/no)?")

if is_second_rider.lower() == "yes":
    age2 = int(input("What is the age of the second rider?"))
    height2 = int(input("What is the height of the second rider?"))
    if age2>= 12 and age2< 18:
        golden2= input("Does this rider have a golden passport (yes/no)?")


    if height < 36 or height2 < 36:
        can_ride = False
    else:
    
        if age >= 18 or age2 >= 18 or golden1.lower()== 'yes' or golden2.lower()== 'yes':
    
            can_ride = True
        else:
        
            can_ride = False
else:
    if age >= 18 and height >= 62:
        can_ride = True
    else:
        can_ride = False

if can_ride:
    print("Welcome to the Incredi-Coaster. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")
