##Rock Paper Scissor Game''==
#from Random we import random int 
import random
#assigning a random play optioms
comp_wins = 0
player_wins = 0
#assigning computer and user to choose one

print(" Winning rules of the rock paper scissors game as follows: \n"
+ "Rock Vs Paper -> Paper Wins \n"
+ "Rock Vs Scissor -> Rock Wins \n"
+ "Paper vs Scissor -> Paper Wins \n" )

def Choose_Option () :
    user_choice = input ("choose rock, paper or scissor: ")
    if user_choice in ["Rock", "rock", "r", "R"] :
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"] :
        user_choice = "p"    
    elif user_choice in ["Scissors", "scissors", "s", "S"] :
        user_choice = "s"
    else:
        print("=====I don't understand, try again.=====")
        Choose_Option ()
    return user_choice
def Computer_Option () :
    comp_choice = random.randint (1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    elif comp_choice == 3:
        comp_choice = "s"
    return comp_choice
# for loop     
while True:
    print("")
    user_choice = Choose_Option ()
    comp_choice = Computer_Option ()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print ("You chose rock. The Computer Chose rock. You Tied")

        elif comp_choice == "p":
            print ("You chose rock. The Computer Chose paper. You lose")
            comp_wins += 1

        elif comp_choice == "s":
            print ("You chose rock. The Computer Chose scissors. You lose")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("===you chose paper, The computer chose rock. you win.")
            player_wins += 1

        elif comp_choice == "p":
            print ("===You chose paper. The Computer Chose paper. You tied")

        elif comp_choice == "s":
            print ("You chose paper. The Computer Chose scissors. You lose.")
            comp_wins += 1

    elif user_choice == "s" :
        if comp_choice == "r":
            print ("You chose scissors. The Computer Chose rock. You lose")
            comp_wins += 1

        elif comp_choice == "p" :
            print ("You chose scissors. The Computer Chose paper. You won")
            player_wins += 1

        elif comp_choice == "s" :
            print ("You chose scissors. The Computer Chose scissors. You tied")

    #printing either user or computer wins 
        if result == user_choice:
            print("<== Users wins  ==>")
        else:
            print("<== Computer Wins ==>")

    print("Do You want to play again? (Y/N)")
    ans = input()

    # if user input n or N then condition is True 
    if ans == 'n' or ans == 'n':
        break
    #after loop
    # print thanks for playing 

    print("\n ====Thanks for playing===")