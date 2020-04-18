# Exr-1 Total Sales

"""days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sales = 0
total = 0
for day in days:
    print("The amount sales on", day, end=": ")
    sales = int(input())
    total += sales

print("Total sales for the last week:", total)"""


# Exr-2 Lottery Number Generator

"""import random
lottery_num = []
num = 0 
generated = 0

while num<7:
    generated = random.randint(0, 9)
    lottery_num.append(generated)
    num += 1
for a in lottery_num:
    print(a)"""


# Exr-3 Rainfall Statistics

"""rainfall = []
total = 0
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print("Enter the amount of rainfall for")
for month in months:
    print(month, end=" ")
    a = int(input())
    rainfall.append(a)
    total += a

print("The highest rate is", max(rainfall))
print("The lowest rate is", min(rainfall))
print("The total amount of rainfall", total)
print("The average rainfall for this year is", total/12"""


# Exr-4 Number Analysis Program 

"""lst = []
total, l = 0, 0
while l<20:
    a = int(input("Enter a number: "))
    lst.append(a)
    total += a
    l += 1
print("The highest number is", max(lst))
print("The lowest number is", min(lst))
print("The sum of numbers is", total)
print("The average of sum is", total/len(lst))"""


# Exr-5 Charge Account Validation

"""import random

def create_charge_account_lst():
    charge_account = []
    num = 0

    for a in range(100):
        num = random.randint(1000000, 9999999)
        charge_account.append(num)

    outfile = open("charge_account.txt", 'w')
    for item in charge_account:
        outfile.write(str(item) + '\n')
    outfile.close()

def check_account_lst():
    
    infile = open('charge_account.txt', 'r')
    user_input = input("Enter an account number: ")
    if user_input in infile:
        print(user_input, "is valid account")
    else:
        print(user_input, "is invalid account")

create_charge_account_lst()
check_account_lst()"""


# Exr-6 Driver's License Exam

"""def answers():
   
    lst = ["B", "D", "A", "A", "C", "A", "B", "A", "C", "D", "B", "C", "D", "A", "D", "C", "C", "B", "D", "A"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    index = 0
    outfile = open('answers_list.txt', 'w')
    while index<20:
        
        outfile.write(str(numbers[index]) + ". " + lst[index] + '\n')
        index += 1
    outfile.close()


def students_answers():
    index = 0
    student_answers = []
    print("Enter your answers.")
    for num in range(1, 21):
        print(num, ".", end=" ")
        answer = input()
        answer = answer.upper()
        student_answers.append(answer)
    outfile = open("student_answers.txt", 'w')
    while index<20:
        outfile.write(student_answers[index] + '\n')
        index += 1
    outfile.close()


def checking():
    
    lst = ["B", "D", "A", "A", "C", "A", "B", "A", "C", "D", "B", "C", "D", "A", "D", "C", "C", "B", "D", "A"]
    infile = open('student_answers.txt', 'r').read().splitlines()
    student_answers = list(infile)
    #student_answers = list(student_answers)
    right = 0
    wrong = 0
    for a in range(20):
        if lst[a]==student_answers[a]:
            right += 1
        else:
            wrong += 1
    print("Results.\n")
    if right>=15:
        print("right answers", "\twrong answers\n", "    ", right, "\t    ", wrong)
        print("Congratulations! You have succesfully passed the exam.")
    else:
        print("right answers", "\twrong answers\n", "    ", right, "\t    ", wrong)
        print("Sorry. You failed.")"""


# Exr-7


"""boy_names=open('boysnames.txt', 'r').read().splitlines()
girl_names = open('girlsnames.txt', 'r').read().splitlines()
print("Enter boys'/girls' names")
name = input("Enter the name: ")
name = name.capitalize()
if name in boy_names:
    print(name, "is popular name.")
elif name in girl_names:
    print(name, "is popular name.")
else:
    print(name, "is not so popular.")"""

# I could not find .txt files from the given website address.
# Even I myself made girls and boys names files in exr-7
# So, in case of somebody will search for these exercises,
# it's better than use wrong one to use nothing, I have not 
# made any kind of changes at all. And prefered to left two 
# last two exercises.