#Hello my name is Ammon Flemign and this is my code for the id badge generator
print("Please enter the following information")
first_name= input("First name?")
last_name= input ("Last name?") 
email_adress= input("Email adress?")
phone_number= input("Phone number?")
job_title= input("Job title?")
id_number= input("Id number?")
color_eyes= input("Eye Color?")
hair_color= input("Hair color?")
month_start= input("Starting month?")
training_yesno= input("Do you have training: Yes or No?")
#Start of id badge code
print(" ")
print("The ID Card is:")
print("--------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job_title.title())
print("ID:", id_number )
print("   ")
print(email_adress.lower())
print(phone_number)
print(" ")
print("Hair:", hair_color.capitalize(), "       ","Eyes:", color_eyes.capitalize())
print("Month:", month_start.capitalize(), "  ","Training:", training_yesno.capitalize())
print("--------------------------------")