# Exr-1 Feet to Inches

def feet_to_inches():
    feet_number = float(input("Enter the number of feet: "))
    num_inches = feet_number*12
    print(num_inches)   
feet_to_inches()


# Exr-2 Math Quiz

import random
a = random.randint(1, 1001)
b = random.randint(1, 1001)
print(a, "+", b, "= ?")
answer = input("Enter your answer: ")
if answer == a + b:
    print("Congratulations!!!")
else:
    print("Ooops! The answer is ", answer)


# Exr-3 Maximum of Two Values

def maximum():
    a = int(input("a = "))
    b = int(input("b = "))
    if a>b:
        print("a is greater than b")
    elif b>a:
        print("b is greater than a")
    else:
        print("They are equal.")
    return
maximum()


# Exr-4 Falling Distance

def falling_distance(fallin_time):
    g = 9.8
    for t in range(11):
        d = 1/2 * g * t**2
    print("Falling distance is ", d)
    return 
falling_distance(12)


# Exr-5 Kinetic Energy

mass = float(input("Enter the amount of mass: "))
velocity = float(input("Enter the amount of velocity: "))
def kinetic_energy():
    ke = (mass*velocity**2)/2
    print("The amount of kinetic energy is ", ke)
    return
kinetic_energy()


# Exr-6 Test Average and Grade

def determine_grade():
    test_score = int(input("Enter your test score: "))
    while test_score<=100:
        if test_score>=90 and test_score<=100:
            print("A")
        elif test_score>=80 and test_score<=89:
            print("B")
        elif test_score>=70 and test_score<=79:
            print("C")
        elif test_score>=60 and test_score<=69:
            print("D")
        else:
            print("F")
        break
    else:
        print("Enter the right value!!!")
def calc_average():
    a = int(input("A = "))
    b = int(input("B = "))
    c = int(input("C = "))
    d = int(input("D = "))
    f = int(input("F = "))
    average = (a+b+c+f+d)/5
    print("The average value is ", average)

calc_average()
determine_grade()


# Exr-7 Odd/Even Counter

import random
even = 0
odd = 0
count = 0

for i in range(100):

    a = random.randint(1, 10000)
    if a%2!=0:
        odd +=1
    elif a%2==0:
        even +=1
    else:
        pass
print("Even numbers are ", even, "\nOdd numbers are ", odd)

    
# Exr-8 Prime Numbers

def is_prime():
    x = int(input("Enter an integer: "))
    while x>1:
        for y in range(2, x):
            if x%y==0:
                print(x, "is not a prime number")
                break
            else:
                print (x,"is a prime number")
                break
    else:
        print("Check the number that you entered!")
is_prime()

# Exr-9 Prime Number list

prime_numbers = []
#total = 0
for a in range(2, 101):
    is_prime = True
    for b in range(2, a):
        if a % b == 0:
            is_prime = False
        
    if is_prime:
        prime_numbers.append(a)

# If somebody wants to count primes
#for num in prime_numbers:
 #   total += 1
print(prime_numbers)


# Exr-10 Future Value

p = float(input("enter the present value of your account: "))
i = float(input("Monthly interest: "))
t = int(input("After how many months: "))

f = p*((1+i)**t)
print("After", t, "months, the monet in your account will be", f)


# Exr-11 Random Number Guessing Game

import random
count = 0
num = random.randint(1, 100)
guess = int(input("Guess the number: "))
while num!=guess:

    if num<guess:
        print("Too high, try again")
    elif num>guess:
        print("Too low, try again")
    count += 1
    guess = int(input("One more chance: "))
if num==guess:
    print("Congratulations! You find the number after", count, "chances!")


# Exr-12 Roc, Paper, Scissors Game

import random

flag = 0

while flag != 1 :
    user_choice = input("Your choice: Rock, Paper, Scissors  ")
    user_choice = user_choice.lower()
    comp = random.randint(1, 3)
    comp_choice = ""
    if comp==1:
        comp_choice = "rock"
    elif comp==2:
        comp_choice = "paper"
    else:
        comp_choice = "scissors"

    if comp==1 and user_choice=="scissors" or comp==2 and user_choice=="rock" or comp==3 and user_choice=="paper":
        print(comp_choice, " x ", user_choice)
        print("You lost!")
        flag = 1
    elif user_choice=="rock" and comp==3 or user_choice=="paper" and comp==1 or user_choice=="scissors" and comp==2:
        print(comp_choice, " x ", user_choice)
        print("You win!")
        flag = 1
    else:
        print(comp_choice, " x ", user_choice)
        print("DRAW")
        flag = 0