from random import randint


def compare(user, computer):
    """
    Compare the user's and computer's selections to determine the 
    winner of the game.
    We use the .lower() string method to ensure that each of the choices that we're 
    checking for are lowercase. 
    
    """
    if user.lower() == computer.lower():
        print("It's a tie!")
    elif user.lower() == 'rock':
        if computer.lower() == 'scissors':
            print("You win!")
        else:
            print("The computer wins!")
    elif user.lower() == 'scissors':
        if computer.lower() == 'paper':
            print("You win!")
        else:
            print("The computer wins!")
    elif user.lower() == 'paper':
        if computer.lower() == 'rock':
            print("You win!")
        else:
            print("The computer win!")
    # Else, a valid choice (rock, paper, or scissors) was not selected so we
    # prompt the user to try again.
    else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")


def get_computers_choice():
    """
    Generate a random selection for the computer based on the three available
    selections: Rock, Paper and Scissors.
    """
    choices = ["Rock", "Paper", "Scissors"]
    choice_index = randint(0, 2)
    choice = choices[choice_index]
    return choice


def game_loop():
    """
    This is our main game loop. This code will
    run the game until the user explictly decides to
    quit.
    """
    play_game = True
    
    # The while loop that will continuously run the game
    while play_game:
        
        # Get input from the user and generate a random selection for the computer
        user = input("Rock, paper, or scissors?")
        computer = get_computers_choice()
        
        # Use the compare function to determine the victor of the game
        compare(user, computer)
        
        # Ask the user if they wish to play the game again
        play_again = input("Woud you like to play again? y/N:")
        
        # If the user selects no, or "n" then the play_game will be set to False 
        # to exit the game loop
        if play_again.lower() == "n":
            play_game = False
            
    print("Thanks for playing!")

game_loop()