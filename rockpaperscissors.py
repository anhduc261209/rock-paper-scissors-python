"""
Rock Paper Scissors Game by Anh Đức
Gtihub Profile: https://github.com/anhduc261209/
"""
from random import randint
from time import sleep
# Generate computer choice
def generateComputerChoice():
    i = randint(1, 3)
    if i == 1:
        choice = 'rock'
    elif i == 2:
        choice = 'paper'
    else:
        choice = 'scissors'
    
    return choice
# Calculate result
def whoWin(p, c):
    who = ''
    if p == 'rock' and c == 'rock': who = 'draw'
    elif p == 'rock' and c == 'paper': who = 'c'
    elif p == 'rock' and c == 'scissors': who = 'p'

    elif p == 'paper' and c == 'rock': who = 'p'
    elif p == 'paper' and c == 'paper': who = 'draw'
    elif p == 'paper' and c == 'scissors': who = 'c'
    
    elif p == 'scissors' and c == 'rock': who = 'c'
    elif p == 'scissors' and c == 'paper': who = 'p'
    elif p == 'scissors' and c == 'scissors': who = 'draw'

    return who
# Get player choice
def getPlayerChoice():
    playerChoice = int(input("What's your choice? (1, 2, 3): "))
    if playerChoice == 1: playerChoice = 'rock'
    elif playerChoice == 2: playerChoice = 'paper'
    elif playerChoice == 3: playerChoice = 'scissors'
    else:
        while playerChoice != 1 or playerChoice != 2 or playerChoice != 3:
            print("Invalid response!")
            playerChoice = int(input("What's your choice? (1, 2, 3): "))
    return playerChoice
def playAgain():
    playAgain = ''
    while playAgain != 'y' and playAgain != 'n':
        playAgain = str(input("Do you want to play again? (Y/n) ")).lower()
        if playAgain == 'y': main()
        elif playAgain == 'n': break
        else: print("Invalid response!")
# Main function
def main():
    # Intro
    print("Welcome to this amazing game - Rock Paper Scissors!")
    sleep(1.5)
    print("In this game, you have to compete with a computer")
    sleep(0.5)
    print("Type 1 if you choose rock, type 2 if you choose paper, type 3 if you choose scissors")
    sleep(0.5)
    # Getting player choice
    playerChoice = getPlayerChoice()
    # Calculate result
    computerChoice = generateComputerChoice()
    print(f"Computer choose {computerChoice}")
    win = whoWin(playerChoice, computerChoice)
    if win == 'p': print("Congratulations! You beat the computer :))")
    elif win == 'c': print("Oh no! The computer beats you :((")
    elif win == 'draw': print("Nah, it's draw :|")
    # Check if want to play again
    playAgain()
# Call the main function
if __name__ == '__main__':
    main()

