import random
import time
options = ("rock", "paper","scissors")
cpu = random.choice (options) # uses  choice method of 'random' libary to give random word from 'options' variable
player_win = 0
cpu_win = 0
draw = 0
rock = 0
paper = 0
scissors = 0
target = 3 # amount of times either player or cpu has to win or hit draw for game to end
print("ROCK PAPER SCISSORS!!")

while True:
   time.sleep(0.5) # sleep method of 'library' to add small delay before next line
   cpu = random.choice (options)
   player = input("""choose rock, paper or scissors
you chose: """)
   if player == "rock": #increases by 1 if player chose respective weapon
      rock = rock + 1
   elif player == "paper":
      paper = paper + 1
   elif player == "scissors":
      scissors = scissors + 1

   if player == "rock" and cpu == "scissors" or player == "paper" and cpu == "rock" or player == "scissors" and cpu == ("paper"): # sets the rules for the game
      player_win = player_win + 1 # increase player_win count if won
      time.sleep(0.5)
      print("cpu chose:", cpu) # print the weapon the cpu played in round
      print("Player won!")
      print("player has won:", player_win, "cpu has won:", cpu_win, "draws:", draw) # print number of times player won, cpu won and amount of draws
      print("rock,", rock, "paper,", paper, "scissors,", scissors) # print amount of times player played a weapon
   elif player == cpu: # check if player and cpu chose same weapon and if so prints draw and adds +1 to draws var
      time.sleep(0.5)
      draw = draw + 1
      print("cpu chose:", cpu)
      print("draw!")
      print("player has won:", player_win, "cpu has won:", cpu_win, "draws:", draw)
      print("rock,", rock, "paper,", paper, "scissors,", scissors)
   else:
      time.sleep(0.5)
      cpu_win = cpu_win + 1
      print("cpu chose:", cpu)
      print("cpu won!")
      print("player has won:", player_win, "cpu has won:", cpu_win, "draws:", draw)
      print("rock,", rock, "paper,", paper, "scissors,", scissors)
    
      if player_win == 3: # end the game (code) after target is reached
         print("GAME OVER") # print respective statement before break
         break # break func is used to end the code
      elif cpu_win == 3:
         print("GAME OVER")
         break
      else:
         draw == 3
         print("GAME ENDED IN TIE")
         break