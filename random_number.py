import random

#player setup
player = str(input("who are you?")).title()


def main():

#how the number is picked
    def guess(x):
        random_number = random.randint(1, x)
        guess = 0
        while guess != random_number:
            guess = int(input(f"Please guess a number between 1 and {x}: "))
            if guess < random_number:
                print("Guess again to low ")
            elif guess > random_number:
                print("Guess again too high ")
        print("Super cool " + (player) + f", you have guess the number {random_number} correctly ")
        
    guess(100)
    repeat = input("Would like to play again? Yes or No: ").lower()
    if repeat == 'yes':
        main()
    else:
        print("See ya")
        exit()

main()