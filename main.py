import random
import os
from time import sleep


choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']  # List to make writing if statements easier

# Make clearing the console universal
def clear():
    os.system('cls' if os.name=='nt' else 'clear')


# Draw the title
def drawTitle():
    clear()
    print(' ____  __   ___ __ _    ____  __  ____ ____ ____    ____  ___ __ ____ ____  __ ____  ____ ')
    print('(  _ \/  \ / __|  / )  (  _ \/ _\(  _ (  __|  _ \  / ___)/ __|  ) ___) ___)/  (  _ \/ ___)')
    print(' )   (  O | (__ )  (    ) __/    \) __/) _) )   /  \___ ( (__ )(\___ \___ (  O )   /\___ \\')
    print('(__\_)\__/ \___|__\_)  (__) \_/\_(__) (____|__\_)  (____/\___|__|____(____/\__(__\_)(____/')
    print(' __   __ ____ ____  __  ____ ____    ____ ____  __   ___ __ _                             ')
    print('(  ) (  |__  |__  )/ _\(  _ (    \  / ___|  _ \/  \ / __|  / )                            ')
    print('/ (_/\)( / _/ / _//    \)   /) D (  \___ \) __(  O | (__ )  (                             ')
    print('\____(__|____|____)_/\_(__\_|____/  (____(__)  \__/ \___|__\_)                            \n\nBy: Zachary Robinson\n\n')


# Get user input
def userInput():
    print('Type your choice: |ROCK|, |PAPER|, |SCISSORS|, |LIZARD|, |SPOCK|: ', end='')
    playerChoice = input().lower()

    # Check if user input is valid
    try:
        playerChoice = choices.index(playerChoice)  # Make player choice equal a number to make if statements easier to write
        return playerChoice
    except:
        print("Invalid option! Press enter to try again...", end='')
        input()
        main()


# Get computers choices
def computerMove():
    choice = random.randint(0, len(choices)-1)
    return choice


# Countdown to result
def countdown():
    buffer = 0.8
    print('\nROCK')
    sleep(buffer)
    print('PAPER')
    sleep(buffer)
    print('SCISSORS')
    sleep(buffer)
    print('SHOOT\n')
    sleep(buffer)


# Check who wins the game
def calculateWin(userChoice, computerChoice):
    print(f'{choices[userChoice]} VS. {choices[computerChoice]}\n')
    sleep(0.5)

    if userChoice == computerChoice:
        return 'tie'
    elif userChoice == 0 and computerChoice == 3 or userChoice == 0 and computerChoice == 2:
        return True
    elif userChoice == 1 and computerChoice == 0 or userChoice == 1 and computerChoice == 4:
        return True
    elif userChoice == 2 and computerChoice == 1 or userChoice == 2 and computerChoice == 3:
        return True
    elif userChoice == 3 and computerChoice == 4 or userChoice == 3 and computerChoice == 1:
        return True
    elif userChoice == 4 and computerChoice == 2 or userChoice == 4 and computerChoice == 0:
        return True
    else:
        return False


# Main function
def main():
    drawTitle()
    playerChoice = userInput()
    computerChoice = computerMove()
    countdown()
    winOrLoose = calculateWin(playerChoice, computerChoice)

    if winOrLoose != 'tie':
        if winOrLoose == True:
            print("You win!!")
        else:
            print("You loose!!")

    else:
        print('You tie!!')

    again = input("Would you like to play again? |Y| |N|  ").lower()
    if again == 'y':
        main()
    else:
        clear()
        quit()


main()