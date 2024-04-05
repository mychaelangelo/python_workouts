import random

def guessing_game():
    number = random.randint(0,100)
    print(number)
    tries = 3
    
    while tries > 0:
        user_guess = int(input("Provide a guess: "))
        if user_guess < number:
            print("Too low")
            tries -= 1
        elif user_guess > number:
            print("Too high")
            tries -= 1
        else:
            print("Just right")
            break
    print("You run out of tries")

guessing_game()



