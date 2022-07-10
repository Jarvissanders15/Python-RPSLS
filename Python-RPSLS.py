from random import randint


print("        ")
print("Welcome to Rock Paper Scissors Lizard Spock!")
print("        ")
print("The rules are simple  Scissors cuts paper, paper covers rock,")
print("rock crushes lizard,lizard poisons Spock, Spock smashes scissors,")
print("scissors decapitates lizard, lizard eats paper,")
print("paper disproves Spock, Spock vaporizes rock,")
print("and as it always has, rock crushes scissors.")
print("        ")
print("        ")

#------------Player Options----------------


player_choice = input("Choose either Rock, Paper, Scissors, Lizard, Spock:  ")
print("        ")

while player_choice == "Rock" or "Paper" or "Scissors" or "Lizard" or "Spock":
    #player_choice = input("Choose either Rock, Paper, Scissors, Lizard, Spock:  ")
      
    

    if player_choice == "Rock":
        print("The player chose Rock")
        print("        ")

    elif player_choice == "Paper":
        print("The player chose Paper")
        print("        ")

    elif player_choice == "Scissors":
        print("The player chose Scissors")
        print("        ")

    elif player_choice == "Lizard":
        print("The player chose Lizard")
        print("        ")

    elif player_choice == "Spock":
        print("The player chose Spock")
        print("        ")
    else:
        #while player_choice != "Rock" or "Paper" or "Scissors" or "Lizard" or "Spock":
        print("Invalid choice! Please choose again")
        print("        ")
        player_choice = input("Choose either Rock, Paper, Scissors, Lizard, Spock:  ")
        print("        ")
        if player_choice == "Rock" or "Paper" or "Scissors" or "Lizard" or "Spock":
            continue
            
            
     
       
        
    #---------Computer Options--------------------

    computer_options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    computer_choice = computer_options[randint(0,4)]

    if computer_choice == "Rock":
        print("The computer chose Rock")
        print("        ")

    if computer_choice == "Paper":
        print("The computer chose Paper")
        print("        ")

    if computer_choice == "Scissors":
        print("The computer chose Scissors")
        print("        ")

    if computer_choice == "Lizard":
        print("The computer chose Lizard")
        print("        ")

    if computer_choice == "Spock":
        print("The computer chose Spock")
        print("        ")



    #----------Game Play----------------

    #---Rock player choice---
        
    if player_choice == "Rock" and computer_choice == "Rock":
        print("The game is a tie!")
    elif player_choice == "Rock" and computer_choice == "Paper":
        print("Sorry. The computer wins!")
    elif player_choice == "Rock" and computer_choice == "Scissors":
        print("YAY! You won!")
    elif player_choice == "Rock" and computer_choice == "Lizard":
        print("YAY! You won!")
    elif player_choice == "Rock" and computer_choice == "Spock":
        print("Sorry. The computer wins!")

    #--Scissors player choice----

    if player_choice == "Scissors" and computer_choice == "Rock":
        print("Sorry. The computer wins!")
    elif player_choice == "Scissors" and computer_choice == "Paper":
        print("YAY! You won!")
    elif player_choice == "Scissors" and computer_choice == "Scissors":
        print("The game is a tie!")
    elif player_choice == "Scissors" and computer_choice == "Lizard":
        print("YAY! You won!")
    elif player_choice == "Scissors" and computer_choice == "Spock":
        print("Sorry. The computer wins!")

    #---Paper player choice---
        
    if player_choice == "Paper" and computer_choice == "Rock":
        print("YAY! You won!")
    elif player_choice == "Paper" and computer_choice == "Paper":
        print("The game is a tie!")
    elif player_choice == "Paper" and computer_choice == "Scissors":
        print("Sorry. The computer wins!")
    elif player_choice == "Paper" and computer_choice == "Lizard":
        print("Sorry. The computer wins!")
    elif player_choice == "Paper" and computer_choice == "Spock":
        print("YAY! You won!")

    #--- Lizard player choice ---

    if player_choice == "Lizard" and computer_choice == "Rock":
        print("Sorry. The computer wins!")
    elif player_choice == "Lizard" and computer_choice == "Paper":
        print("YAY! You won!")
    elif player_choice == "Lizard =" and computer_choice == "Scissors":
        print("Sorry. The computer wins!")
    elif player_choice == "Lizard" and computer_choice == "Lizard":
        print("The game is a tie!")
    elif player_choice == "Lizard" and computer_choice == "Spock":
        print("YAY! You won!")

    #--- Spock player choice ---

    if player_choice == "Spock" and computer_choice == "Rock":
        print("YAY! You won!")
    elif player_choice == "Spock" and computer_choice == "Paper":
        print("Sorry. The computer wins!")
    elif player_choice == "Spock" and computer_choice == "Scissors":
        print("YAY! You won!")
    elif player_choice == "Spock" and computer_choice == "Lizard":
        print("Sorry. The computer wins!")
    elif player_choice == "Spock" and computer_choice == "Spock":
        print("The game is a tie")

    print("        ")
    player_choice = input("Choose either Rock, Paper, Scissors, Lizard, Spock:  ")



    
    
