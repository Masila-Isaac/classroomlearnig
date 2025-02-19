height = float(input("What is your height? ")) 
surerity = input("Is height in meters or centimeters? (m/cm) ")

if surerity.lower() == "m":
    height_in_cm = height * 100
elif surerity.lower() == "cm":
    height_in_cm = height
else:
    print("Invalid input for units.")
    height_in_cm = None
if height_in_cm is not None:
    print("Your height is " + str(height_in_cm) + " cm")
