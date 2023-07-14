import random

print("Do you want to roll?")
print("Enter either y or n.")
responce = input(">> ")

while responce == "y":
    num = random.randint(1, 6)
    if num == 1:
        print(" _____")
        print("|     |")
        print("|  0  |")
        print("|_____|")
    elif num == 2:
        print(" _____")
        print("|0    |")
        print("|     |")
        print("|____0|")
    elif num == 3:
        print(" _____")
        print("|0    |")
        print("|  0  |")
        print("|____0|")
    elif num == 4:
        print(" _____")
        print("|0   0|")
        print("|     |")
        print("|0___0|")
    elif num == 5:
        print(" _____")
        print("|0   0|")
        print("|  0  |")
        print("|0___0|")
    else:
        print(" _____")
        print("|0   0|")
        print("|0   0|")
        print("|0___0|")
    
    print("Enter y to roll again or n to exit.")
    choice = input(">> ")
    responce = choice