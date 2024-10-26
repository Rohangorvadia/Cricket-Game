import random
import numpy as np

def main():

      print("Welcome to Hand Cricket game!");
      print("You will be playing aganist the computer to win..")
      playerChoice = 0;
      try:
            # select no of overs
            over = int(input("Select the no of overs (1-10): "));
            print("Total overs: ",over)
            # checks if player is toss winner or not
            tossWinner = toss()
            
            if tossWinner == 1:
                  print("You won the toss!!");
                  playerChoice = int(input("Select 1 to bat, 2 to bowl:"));
                  playerScore, computerScore = playGame(over,playerChoice);
            else:
                  print("You loss the toss..");
                  computerChoice = random.randint(1,2);
                  playerChoice = 1 if computerChoice == 2 else 2;
                  playerScore, computerScore = playGame(over,playerChoice);
            # starts the game
            winner(playerScore,computerScore);
      except ValueError:
            print("Invalid input, exiting game...");
            
def toss():
      print("It's time for a toss:");
      playerChoice = int(input("Choose heads(1) or tails(2):"));
      tossResult = random.randint(1,2);
      print("its","Heads!" if tossResult == 1 else "Tails!");

      # here if player1 choose the same as tossResult then he wins the toss and decides what to do
      if(playerChoice == tossResult):
            return 1;
      else:
            return 2;
      # retuns 1 if player won the toss else 2


def playGame(overs, playerChoice):
      playerScore = 0;
      playerWicketsRemaining = 10;
      computerWicketsRemaining = 10;
      computerScore = 0;

      for over in range(overs):
            # print(f"\nOver {over + 1} Player: {playerWicketsRemaining} wickets remaining")
            # MOST IMPORTANT THING..
            #  1 = batting and 2 = bowling  

            if playerChoice == 1:
                  playerScore , playerWicketsRemaining = Turn(playerScore,playerWicketsRemaining ,playerChoice, over , np.inf)
            else:
                  computerScore , computerWicketsRemaining = Turn(computerScore,computerWicketsRemaining ,playerChoice, over, np.inf)
            
      
      print("1'st inngins is Over.");
      toChase = playerScore+1 if playerChoice == 1 else computerScore+1;
      print("To win","opponent" if playerChoice == 1 else "you","need ",toChase,"runs to win in ",overs,"overs")
      newPlayerChoice = 2 if playerChoice == 1 else 1;

      for over in range(overs):
            # print(f"\nOver {over + 1} Player: {playerWicketsRemaining} wickets remaining")
            # MOST IMPORTANT THING..
            #  1 = batting and 2 = bowling  

            if newPlayerChoice == 1:
                  playerScore , playerWicketsRemaining = Turn(playerScore,playerWicketsRemaining ,newPlayerChoice, over, toChase)
            else:
                  computerScore , computerWicketsRemaining = Turn(computerScore,computerWicketsRemaining ,newPlayerChoice, over, toChase)
            
      return playerScore , computerScore
      

def Turn(score,wicketsRemaining ,playerChoice, over, toChase):
      print("==========");
      print(f"Player is","battng" if playerChoice == 1 else "bowling");
      balls = 0;
      playerRun = 0;
      computerRun = 0;

      while balls < 6 and wicketsRemaining > 0:
            # player is batting
            if playerChoice == 1:
                  print(f"Runs: {score}")
                  print(f"Over: {over}.{balls}")
                  playerRun = int(input("Enter your Shot (1-6): "));
                  computerBall = random.randint(1,6);
                  print(f"You choose: {playerRun} , opponent choose: {computerBall}");
            # Player is bowing
            else:
                  print(f"Runs: {score}")
                  print(f"Over: {over}.{balls}")
                  playerBall = int(input("Enter your Shot (1-6): "));
                  computerRun = random.randint(1,6);
                  print(f"You choose: {playerBall} , opponent choose: {computerRun}");

            # player is battin gand he got out
            if playerChoice == 1 and playerRun == computerBall:
                  print("You are out!");
                  wicketsRemaining -= 1;
                  if wicketsRemaining > 0:
                        print(f"You have {wicketsRemaining} wickets remaining..");
            # player is bowling and he took wicket
            elif playerChoice == 2 and playerBall == computerRun:
                  print("Opponent is Out!");
                  wicketsRemaining -= 1;
                  if wicketsRemaining > 0:
                        print(f"Opponent have {wicketsRemaining} wickets remaining..");
            # player scored some runs
            elif playerChoice == 1:
                  score += playerRun;
                  print(f"Player score is: {score}");
                  # checking if we had successfully chased the score
                  if score >= toChase:
                        print("You Won");
                        break;
            # opponent scored some runs
            else:
                  score += computerRun; 
                  print(f"Opponent score is: {score}");
                  # checking if we had successfully chased the score
                  if score >= toChase:
                        print("Opponent Won!");
                        break;
            balls += 1;
      
      
      displayScore(score,over,wicketsRemaining);
      return score,wicketsRemaining;

def displayScore(Score , over ,wicketsRemaining):
      print("\nScoreboard")
      print("==========")
      print(f"Over {over + 1}:")
      print(f"Runs: {Score} , {wicketsRemaining} wickets remaining")

def winner(playerScore , computerScore):
      print("==========");
      print("Match Result");
      print("Your Score: ",playerScore);
      print("Opponent Score: ", computerScore);
      if playerScore > computerScore:
            print("You won the Match!!");
      elif computerScore > playerScore:
            print("You lost the Match!");
      else:
            print("The match ended in a draw")
      print("Thank you for playing and have a good day :) ")

main()