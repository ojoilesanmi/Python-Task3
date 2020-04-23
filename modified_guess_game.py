from random import randint
import sys

def level():
    
    print("Hello dear! kindly choose your difficulty ")
    diff = input("Easy, hard, medium: ")
    difficulty = diff.lower()
    if difficulty == "easy":
        easy()
    if difficulty == "medium":
        medium()
    else:
        hard()
    
def easy():
    try:
        counter = 0
        random_number = randint(1, 10)
        print("You have 6 guesses")
        while counter < 6:
            number = int(input("Enter a number between 1 and 10: "))
            if number != random_number:
                print("that was wrong")
                counter +=1
                print("You have {} guess(es) left".format(6-counter))
                continue
            if number == random_number:
                print("You guessed right!")
                break
        if counter == 6:
                print("GAME OVER!")
        print("Do you want to continue playing? ")
        game_continue()
    except ValueError:
        print("This is not a number. Kindly input a number ")
        

def game_continue():
    continue_game = int(input("Press 1 to continue 0 to terminate    "))
    if continue_game == 1:
        level()
    else:
        print("Thank you for playing")
        sys.exit()
        

def medium():
    try:
        counter = 0
        random_number = randint(1, 20)
        print("You have 4 guesses")
        while counter < 4:
            number = int(input("Enter a number between 1 and 20: "))
            if number != random_number:
                print("that was wrong")
                counter += 1
                print("You have {} guess(es) left".format(4-counter))
                continue
            else:
                print("You are right!")
                break
        if counter == 4:
            print("GAME OVER!")
        game_continue()
    except ValueError:
        print("This is not a number. Kindly input a number ")

def hard():
    try:
        counter = 0
        random_number = randint(1, 50)
        print("You have 3 guesses")
        while counter < 3:
            number = int(input("Enter a number between 1 and 50: "))
            if number != random_number:
                print("that was wrong")
                counter += 1
                print("You have {} guess(es) left".format(3-counter))
                continue
            else:
                print("You are right!")
                break
                
        if counter == 3:
            print("GAME OVER!")
        game_continue()
    except ValueError:
        print("This is not a number. Kindly input a number ")

            

level()
