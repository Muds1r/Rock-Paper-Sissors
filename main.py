import random


def get_choices():
  player_choice = input('Enter a choice (Rock,Paper,Sissors:)')
  options = ['rock','paper','sissors']
  computer_choice = random.choice(options)
  choices = {'player': player_choice,'computer' : computer_choice}
  return choices


def check_win(player, computer):
  print(f'You Chose:{player} , Computer Chose:{computer}')
  if player == computer: return "It's a tie!"
  
  elif player == "rock":
    if computer == "sissors":
      return "Rock Smashes Sissors! You Win!"
    else:
      return 'Paper Covers Rock! You Lose.'
  elif player == "paper":
    if computer == "rock":
      return "Paper Covers Rock! You Win!"
    else:
      return 'Sissors Cut Paper! You Lose.'
  
  elif player == "sissors":
    if computer == "paper":
      return "Sissors Cut Paper! You Win!"
    else:
      return 'Rock Smashes Paper! You Lose.'
      
choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)