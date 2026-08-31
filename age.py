import random
def guess_age():
    print("Hello!")
    name = input("What is your name?")
    answer = ""
    while answer != "y":
        age = random.randint(15,40)
        answer = input(f"Is your age {age}? (y/n)")
        if answer == "y":
            break
        else:
            print('Rats.')
    print(f"{name} is {age} years old.")
    

guess_age()
