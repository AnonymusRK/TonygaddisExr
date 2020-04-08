

# Exr-1

print("Personal information")

print(input("Your name: "))
print(input("Your adress\nCity: "))
print(input("State: "))
print(input("Zip:"))
print(input("Your telephone number: "))
print(input("Your college major: "))

# Exr-2

def sales_tax():
    purchase = int(input("Amount of purchase: "))
    state_tax = purchase*0.04
    county_tax = purchase*0.02
    total_tax = state_tax + county_tax
    total_sale = total_tax + purchase
    print("State tax is", state_tax)
    print("County tax is", county_tax)
    print("Total sales tax is", total_tax)
    print("Total sale is", total_sale)
sales_tax()

# Exr-3

def insurance():
    repl_cost = float(input("Enter the replacement cost: "))
    insurance = repl_cost*0.8
    print("Minimum amount of insurance is", insurance)

insurance()

# Exr-4

def automobile_costs():
    print("You have following expenses for your car:")
    loan_payment = float(input("Loan payment: $"))
    insurance = float(input("Insurance: $"))
    gas = float(input("Gas: $"))
    oil = float(input("Oil: $"))
    tires = float(input("Tires: $"))
    maintenance = float(input("Maintenance: $"))
    monthly = loan_payment+insurance+gas+oil+tires+maintenance
    annual_cost = monthly*12
    print("Total monthly cost is $", monthly, "\nTotal annual cost is $", annual_cost)

automobile_costs()

# Exr-5

def property_tax():
    actual_value = float(input("Enter the actual value: $"))
    tax_value = actual_value*0.6
    assesment_value = actual_value*0.4
    print("Assesment value is: $", assesment_value, "\nProperty tax is $", tax_value)
    print("Note: Property tax is 60%")

property_tax()

# Exr-6

def body_mass():
    weight = float(input("Enter your weight: "))
    height = float(input("your height: "))
    body_mass = weight*703/height**2
    print("Your BMI is ", body_mass)
    print("Note! The parameters you entered are in pounds and inches respectively")

body_mass()

# Exr-7

def calories():
    fat_grams = float(input("Enter the amount of fat grams you consume in a day: "))
    carb_grams = float(input("Enter the amount of carbohydrate grams you consume in a day: "))
    fat_cal = fat_grams*9
    carb_cal = carb_grams*4
    print("The number of calories you consume from fat grams is ", fat_cal, "and from carbohydrate grams is ", carb_cal)

calories()

# Exr-8

def stadium_seats():
    print("Number of tickets were sold")
    class_a = int(input("Class A: "))
    class_b = int(input("Class B: "))
    class_c = int(input("Class C: "))
    total_income = class_a*15 + class_b*12 + class_c*9
    print("Total income is $", total_income)

stadium_seats()

# Exr-9

def paint_job_estimater():
    painting_area = int(input("Enter the square feet of wall space to be painted: "))
    price_gallon = float(input("Price of the paint per gallon: $"))
    while painting_area>=115:
        num_gallons = painting_area//115
        labor_hours = (painting_area//115)*8
        cost_paint = price_gallon*(painting_area//115)
        labor_charge = labor_hours*20000
        total_cost = cost_paint + labor_charge
        print("The number of gallons of paint required: ", num_gallons)
        print("The hours of labor required: ", labor_hours)
        print("The cos of the paint: ", cost_paint)
        print("The labor charges: ", labor_charge)
        print("The total cost of paint job: ", total_cost)
        break
paint_job_estimater()

# Exr-10

def monthly_tax():
    total_sales = float(input("Enter the total sales for the month: $"))
    county_tax = total_sales*0.04
    state_tax = total_sales*0.02
    total_tax = county_tax + state_tax
    print("The amount of county sales tax: $", county_tax)
    print("The amount of state sales tax: $", state_tax)
    print("The sum of sales tax: $", total_tax)

monthly_tax()
