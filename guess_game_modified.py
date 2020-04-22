#To generate random numbers(random integers)
from random import randint
counter = 0
print("Hi there! Kindly enter your difficulty below ")
diff = input("easy, medium and hard: ")
difficulty = diff.lower()

try:
        if difficulty == "easy":
            random_number = randint(1, 10)
            print("You have a total of 6 guesses")
            while counter < 6:  
                number = int(input("Enter a number between 1 and 10: "))                
                if number != random_number:
                    print("That was wrong")
                    counter +=1
                    print("You have {} guess(es) left".format(6-counter))
                    continue   
                else:
                    print("You guessed right!")
                    break
        if counter == 6:
            print("GAME OVER!")
        
        if difficulty == "medium":
            random_number = randint(1, 20)
            print("You have 4 guesses")
            while counter < 4:
                number = int(input("Enter a number between 1 and 20: "))
                if number != random_number:
                    print("That was wrong")
                    counter += 1
                    print("You have {} guess(es) left".format(4-counter))
                    continue
                else:
                    print("You guessed right!")
                    break
        if counter == 4:
            print("GAME OVER!")

        if difficulty == "hard":
            random_number = randint(1, 50)
            print("You have 3 guesses")
            while counter < 3:
                number = int(input("Enter a number between 1 and 50: "))
                if number != random_number:
                    print("That was wrong")
                    counter += 1
                    print("You have {} guesses left".format(3-counter))
                    continue
                else:
                    print("You guessed right!")
                    break
        if counter == 3:
            print("GAME OVER!")
        else:
            print("Enter easy, hard or medium")

except ValueError:
    print("This is not a number. Kindly input a number ")
    
