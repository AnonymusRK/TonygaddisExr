# Exr-1

n = int(input("N = "))

ming = n // 1000
yuz = (n % 1000) // 100
on = (n % 100) // 10
bir = n % 10

if ming == 1:
    print("M", end='')
elif ming == 2:
    print("MM", end='')
elif ming == 3:
    print("MMM", end='')
elif ming == 4:
    print("MMMM", end='')
elif min == 5:
    print("MMMMM", end='')

if yuz == 1:
    print("C", end='')
elif yuz == 2:
    print("CC", end='')
elif yuz == 3:
    print("CCC", end='')
elif yuz == 4:
    print("CD", end='')
elif yuz == 5:
    print("D", end='')
elif yuz == 6:
    print("DC", end='')
elif yuz == 7:
    print("DCC", end='')
elif yuz == 8:
    print("DCCC", end='')
elif yuz == 9:
    print("CM", end='')


if on == 1:
    print("X", end='')
elif on == 2:
    print("XX", end='')
elif on == 3:
    print("XXX", end='')
elif on == 4:
    print("XL", end='')
elif on == 5:
    print("L", end='')
elif on == 6:
    print("LX", end='')
elif on == 7:
    print("LXX", end='')
elif on == 8:
    print("LXXX", end='')
elif on == 9:
    print("XC", end='')


if bir == 1:
    print("I", end='')
elif bir == 2:
    print("II", end='')
elif bir == 3:
    print("III", end='')
elif bir == 4:
    print("IV", end='')
elif bir == 5:
    print("V", end='')
elif bir == 6:
    print("VI", end='')
elif bir == 7:
    print("VII", end='')
elif bir == 8:
    print("VIII", end='')
elif bir == 9:
    print("IX", end='')

print("")

# Exr-2

print("First rectangle:")
a = float(input("a = "))
b = float(input("b = "))
first_rec_area = a*b
print("Second rectangle:")
c = float(input("c = "))
d = float(input("d = "))
sec_rec_area = c*d
if first_rec_area>sec_rec_area:
    print("First rectangle is greater.")
elif sec_rec_area>first_rec_area:
    print("Second rectangle is greater.")
else:
    print("They are equal.")

# Exr-3 Mass and Weight

mass = float(input("Enter object's mass: "))

weight = mass*9.8

if weight>1000:
    print("It is too heavy!")
elif weight<10:
    print("It is too light!")
else:
    print(weight)

# Exr-4 Magic Dates

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Two digit year:"))

if day*month==year:
    print(month, "x", day, "=", year, "\nIt is a magic date!")
elif day*month!=year:
    print(month, "/", day, "/", year, "\nIt is not a magic date!")


# Exr-5 Color Pixel

color_1 = input("First primary color: ")
color_2 = input("Second primary color: ")
color_1 = color_1.lower()
color_2 = color_2.lower()

if color_1=="red" and color_2=="blue" or color_1=="blue" and color_2=="red":
    print("You created purple!")
elif color_1=="red" and color_2=="yellow" or color_1=="yellow" and color_2=="red":
    print("Now you have orange!")
elif color_1=="blue" and color_2=="yellow" or color_1=="yellow" and color_2=="blue":
    print("You get green!")
else:
    print("You chose wrong color!!!")

# Exr-6 Change for a Dolar Game

choice = input("What kind of coins you want to play with: ")

if choice=="penny":
    penny = int(input("Enter the number of pennies:"))
    if penny==100:
        print("Congratulations! You win the game!")
    else:
        print("You failed.")
elif choice=="nickel":
    nickel = int(input("Enter the number of nickels:"))
    if nickel==20:
        print("Congratulations! You win the game!")
    else:
        print("You failed.")
elif choice=="dime":
    dime = int(input("Enter the number of dimes:"))
    if dime==10:
        print("Congratulations! You win the game!")
    else:
        print("You failed.")
elif choice=="quarter":
    quarter = int(input("Enter the number of quarters:"))
    if quarter==20:
        print("Congratulations! You win the game!")
    else:
        print("You failed.")
else:
    print("Choose the right option.")


# Exr-7 Book Club Points

purchases = int(input("Enter the number of books you bought in this month: "))

if purchases==1:
    print("You earned 5 point!")
elif purchases==2:
    print("You earned 15 points!")
elif purchases==3:
    print("You earned 30 points!")
elif purchases>=4:
    print("You earned 60 points!")
else:
     print("You have no points.")

# Exr-7 Software Sales

purchased = int(input("Enter the number of packages purchased: "))

print("Quantity of purchase         Discount\n")
print("       ", purchased, end="")

if purchased>=100:
    print("                    50%")
elif purchased>=50 and purchased<=99:
    print("                    40%")
elif purchased>=20 and purchased<=49:
    print("                    30%")
elif purchased>=10 and purchased<=19:
    print("                    20%")
else:
    print("                   There is no \n                            discount for \n                            0 purchase!")

# Exr-9 Shipping Charges

weight = int(input("Enter the weight of a package: "))

if weight<=2:
    print("$1.10")
elif weight>2 and weight<=6:
    print("$2.20")
elif weight>6 and weight<=10:
    print("$3.70")
else:
    print("$3.80")

# Exr-10 Body Mass Index Program Enhancement

def body_mass():
    weight = float(input("Enter your weight: "))
    height = float(input("your height: "))
    body_mass = weight*703/height**2
    if body_mass<18.5:
        print("Your BMI is ", body_mass, "and you are underweight")
    elif body_mass>=18.5 and body_mass<=25:
        print("Your BMI is ", body_mass, "and you have optimal weight")
    elif body_mass>25:
        print("Your BMI is ", body_mass, "and you are overweight")
       
    print("Note! The parameters you entered are in pounds and inches respectively")

body_mass()

# Exr-11 Time Calculator

seconds = int(input("Enter the number of seconds: "))

days = seconds//86400
hours = seconds%86400//3600
minutes = seconds%3600//60
seconds = seconds%60

if days:
    if days:
        print(days, "day,", hours, "hours,", minutes, "minutes,", seconds, "seconds")
    elif days==0 and hours:
        print(hours, "hours,", minutes, "minutes,", seconds, "seconds")
    elif days==0 and hours==0 and minutes:
        print(minutes, "minutes,", seconds, "seconds")
    elif days==0 and hours==0 and minutes==0 and seconds:
        print(seconds, "seconds")
elif hours:
    if hours:
        print(hours, "hours,", minutes, "minutes,", seconds, "seconds")
    elif hours==0 and minutes:
        print(minutes, "minutes,", seconds, "seconds")
    elif minutes==0 and seconds:
        print(seconds, "seconds")
elif minutes:
    if minutes:
        print(minutes, "minutes,", seconds, "seconds")
    elif seconds:
        print(seconds, "seconds")  
else:
    print(seconds, "seconds") 
