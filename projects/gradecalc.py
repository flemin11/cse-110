grade= int(input("What is your grade percentage in the class?"))
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter= "B"
elif grade >= 70: 
    letter = "C"  
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
sign= ""
last_digit = grade % 10
if last_digit >= 7:
    sign= "+"
elif last_digit < 3:
    sign= "-"
else:
    sign= ""
print(" ")
print(f"Your letter grade is: {letter}{sign}")
if grade > 70:
    print("Way to go! You passed this course!")
else:
    print("Try a little harder next time, you'll get it.")
