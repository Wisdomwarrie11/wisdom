from random import randint

EASY = 10
HARD = 5

try_again =0

def check_num(guess_num, answer, turns):
    if guess_num == answer:
        print(f"{guess_num} is correct.")

    elif guess_num > answer:
        print(f"{guess_num} is too high.")
        return turns -1
    else:
        print(f"{guess_num} is too low.")
        return turns - 1

def difficulty():
    level = str(input("choose difficulty. Do you choose easy or hard?: "))
    if level == "easy":
        return EASY
    else:
        return HARD

def play_game():
    print("WELCOME TO THIS NUMBER GUESSING GAME. You will have to guess a number between 1 and 100")
    print("")
    answer = randint(1, 100)
    print(answer)
    try_again = difficulty()


    guess_num = 0
    while guess_num != answer:
        print(f"You have {try_again} attempts remaining")
        guess_num = int(input("guess a number: "))
        try_again = check_num(guess_num, answer, try_again)
        if try_again == 0:
            print("You cant try again. You've lost!")
            return
        elif guess_num != answer:
            print("you can guess again")

play_game()


