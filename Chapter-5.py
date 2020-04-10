
# Exr-1 Bug Collector

total = 0

for a in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    print("Appeared number of bugs on", a, end=" ")
    
    daily_bugs = int(input(": "))
   
    total = total + daily_bugs

print(total, "number of bugs defined in this week.")


# Exr-2 Calories Burned

print("A human body loses 3.9 calories per minute.")
print("We investigate how much calories one will lose after 10, 15, ... , 30 minutes.")

for minutes in range(10, 31, 5):
    burned_cal = minutes*3.9
    print("You will lose", burned_cal, "after", minutes, "minutes")

# Exr-3 Budget Analysis

budget = float(input("For this month you budgeted: $"))
total = 0

for expense in ["Transportation", "Nutrition", "Intertainment", "On arrangements", "Medicine"]:
    print(expense, end="")
    expense = float(input(": $"))
    total = total + expense
if total<budget:
    print("Your expenses are still under budget.")
elif total==budget:
    print("You have spent the budget for this month!")
else: 
    print("Attention! Your expenses are over budget!!!")

# Exr-4 Distance Traveled

speed = float(input("What the speed of the vehicle is in mph: "))
hours = int(input("How many hours it has traveled: "))
print("Hour\t\tDistance Traveled")
for a in range(1, hours+1):
    distance = speed * a 
    print("", a, "\t\t     ", distance)

# Exr-5 Average Rainfall

years = int(input("Enter the period: "))
months = 0
total = 0
for year in range(1, years+1):
    print(year, "- period")
    for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
        print("Inches of rainfall for", month, end="")
        inches = float(input(": "))
        total = total + inches
    months +=12
    average = total/months
    
        
print("Number of months: ", months)
print("Total inches of rainfall: ", total)
print("The average rainfall per month for the entire period: ", average)

# Exr-6 Celsius to Fahrenheit Table

print("Celsius\t\tFahrenheit")
for celsius in range(21):
    fahrenheit = 9/5*celsius + 32
    print("  ", celsius, "\t\t  ", fahrenheit)

# Exr-7 Pennies for Pay

days = int(input("Number of days: "))
print("Days\t\tSalary")
salary = 0
total = 0
for day in range(1, days+1):
    salary = salary+1
    total += salary
    print("", day, "\t\t ", salary)
if total>=100:
    dollar = total//100
    penny = total%100
    print("Earned money $", dollar, end="")
    print(",", end="")
    print(penny)
else: 
    pass

# Exr-8 Sum of Numbers

total = 0 
while True:
    number = int(input("Enter the number: "))
    total = total+number
    if number<0:
        number = -1*number
        total = total + number
        break

print("Sum of numbers: ", total)

# Exr-9 

for a in range(7, 0, -1):
    print(a*"*")

# Exr-10
for a in range(0, 6):
    print("#", a*" ", end="")
    print("#")
for b in range(5, 0, -1):
    print("#", end="")
    print(b*" ", end="")
    print("#")