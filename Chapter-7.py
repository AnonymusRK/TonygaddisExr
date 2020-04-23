# Exr-1 File Display

infile = open('numbers.txt', 'w')
for num in range(1, 101):
    infile.write(str(num) + "\n")

infile.close()

file = open('numbers.txt', 'r').read().splitlines()
for l in list(file):
    print(int(l))


# Exr-2 File Head Lines

def file_lines():
    file_name = input("Enter the file name (.txt): ")
    file_name = open(file_name, 'r').read().splitlines()
    file_name = list(file_name)
    five_lines = len(file_name)
        
    if five_lines < 5:
        for el in file_name:
            print(el)   
            
    else:
        print(file_name[0:5])
file_lines()


# Exr-3 line numbers

def line_numbers():
    file_name = input("Enter the file name (.txt): ")
    file_name = open(file_name, 'r').read().splitlines()
    file_name = list(file_name)
    lines = len(list(file_name))
    num = 1
    for el in file_name:
        print("{0}:".format(num), el)
        num += 1
line_numbers()


# Exr-4 Item Counter

def item_counter():
    file_name = input("Enter the file name (.txt): ")
    file_name = open(file_name, 'r').read().splitlines()
    file_name = list(file_name)
    items = len(file_name) # First method
    counter = 0            # Second method
    for item in file_name:
        counter += 1
    print(counter)
    print(items)
item_counter()


# Exr-5 Sum of Numbers

def sum_of_numbers():
    file_name = input("Enter the file name (.txt): ")
    file_name = open(file_name, 'r').read().splitlines()
    file_name = list(file_name)
    total = 0 
    for number in file_name:
        number = int(number)
        total += number
    print(total)
sum_of_numbers()


# Exr-6 Average of Numbers

def average_num():
    file_name = input("Enter the file name (.txt): ")
    file_name = open(file_name, 'r').read().splitlines()
    file_name = list(file_name)
    total = 0 
    for number in file_name:
        number = int(number)
        total += number
    average = total/len(file_name)
    print(average)
average_num()


# Exr-7 Random File Writer

import random

def rand_file():

    how_many = int(input("How many eandom numbers you want: "))
    rand_num = random.randint(1, 100)
   
    infile = open("randomNumbers.txt", 'w')
    for a in range(how_many):
        infile.write(str(rand_num) + '\n')
    infile.close()

rand_file()


# Exr-8 Random Number File Reader

def file_reader():

    outfile = open('randomNumbers.txt', 'r').read().splitlines()
    outfile = list(outfile)
    total = 0
    counter = 0
    for num in outfile:
        print(num)
        total += int(num)
        counter += 1
    print("Total: ", total)
    print("Number of items: ", counter)

file_reader()


# Exr-9 Exception Holding

def average_num():

    total = 0 
    try:
        file_name = input("Enter the file name (.txt): ")
        file_name = open(file_name, 'r').read().splitlines()
        file_name = list(file_name)
        
        for number in file_name:
            number = int(number)
            total += number
        average = total/len(file_name)
        print(average)
    except IOError:
        print("An error occured trying to read the file!")
    except ValueError:
        print("Non-numeric variable!")
average_num()


# Exr-10 Golf Scores

def golf_scores():
    num_players = int(input("How many players: "))
    infile = open("golf.txt", 'w')
    
    for count in range(1, num_players+1):
        print("Player #", count, sep="")
        name = input("Name: ").capitalize()
        score = input("Score: ")

        infile.write(name + '\n')
        infile.write(score + '\n')
        print()
    infile.close()

golf_scores()

def golf_score_read():
    outfile = open("golf.txt", 'r')
    name = outfile.readline()

    while name!="":
        score = outfile.readline()

        name = name.rstrip('\n')
        score = score.rstrip('\n')

        print("Name: ", name)
        print("Score: ", score)
        print()
        
        name = outfile.readline()
    outfile.close()
golf_score_read()