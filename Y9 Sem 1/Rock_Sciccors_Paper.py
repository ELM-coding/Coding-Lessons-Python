#rock paper scissors
import random
Rock=1
Paper=2
Scissors=3
gameOver=False
print("Game ON!")
while gameOver==False:
    #your choice
    player1 = int(input("1 for Rock, 2 for Paper, 3 for Scissors :"))
    #the computer choice
    player2 = random.randint(1,3)
    if(player2==1):
        choiceComputer="Rock"
    elif(player2==2):
        choiceComputer="Paper"
    elif(player2==3):
        choiceComputer="Scissors"
    #the player choice
    if(player1==1):
        choicePlayer="Rock"
    elif(player1==2):
        choicePlayer="Paper"
    elif(player1==3):
        choicePlayer="Scissors"
    #lets check who wins
    if (player1 == 1 and player2 == 1) or (player2 == 2 and player1 == 2) or (player1 == 3 and player2 == 3) or(player1 == 1 and player2==2):
        print("The computer chose: "+choiceComputer+ " And you chose: "+ choicePlayer)
        print("you thought you would win!! its a draw:")
    elif (player1 ==3 and player2 == 2) or (player2 == 1 and player1 == 2) or (player1 == 3 and player2 == 3) or(player1 == 2 and player2==3):
        print("Computer won!! you loose!")
        print("The computer chose: "+choiceComputer+ " And you chose: "+ choicePlayer)
    else:
        print("You won!!! ")
        print("The computer chose: "+choiceComputer+ " And you chose: "+ choicePlayer)
    keepOn =int(input("Do you want to try again ? (1=yes && 2=no ) :"))
    if keepOn==2:
        gameOver=True