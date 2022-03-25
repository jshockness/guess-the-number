#Number Guessing Game Objectives:
# Include an ASCII art logo.
from art import logo
from random import randint

def play_game():
  answer = randint(1, 100)
  
  player_turns = 5
  print(logo)
  print("Welcome to Guess A Number! The random number guessing game.")
  print("I'm thinking of a number between 1 and 100.")
  print(f"The correct number is {answer}")
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if level == "easy":
    player_turns = 10

  guess = 0

  while guess != answer:
    print(f"You have {player_turns} chances left.")
    guess = int(input("Take a guess: "))

    if guess == answer:
      print("Correct You Win!")
    elif guess < answer:
      player_turns -= 1
      print("Too Low, try again")
      print("Guess Again.")
    elif guess > answer:
      player_turns -= 1
      print("Too High, try again")
      print("Guess Again.")
    else:
      player_turns -= 1
      print("Guess Again.")

    if player_turns == 0:
      return "You have no more turn, you lose"
  
play_game()  
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

