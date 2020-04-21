import random

print("This is a guessing game.")

player_level = []
while player_level == [ ]:
  player_level = input("Chose a difficulty level; Easy, Medium or Hard: ")

  if player_level == "Easy":
    chances = 0
    max_guess = 6
    number = random.randint(1, 10)
    print("Guess a number between 1 and 10")
    
    while chances < max_guess:
      guess = int(input("Guess: "))
      max_guess -= 1
      print(f"You have {max_guess} guess(es) left.")
      
      if guess == number:
        print("You got it right!")
        break
       
      elif guess < number:
        print("That was wrong! Guess a higher number.")
        
      else:
        print("That was wrong! Guess a lower number.")
        
    if chances == max_guess:
      print("Game Over! The number is", number)
      
      
      
  elif player_level == "Medium":
    chances = 0
    max_guess = 4
    number = random.randint(1, 20)
    print("Guess a number between 1 and 20")
    
    while chances < max_guess:
      guess = int(input("Guess: "))
      max_guess -= 1
      print(f"You have {max_guess} guess(es) left.")
      
      if guess == number:
        print("You got it right!")
        break
       
      elif guess < number:
        print("That was wrong! Guess a higher number.")
        
      else:
        print("That was wrong! Guess a lower number.")
        
    if chances == max_guess:
      print("Game Over! The number is", number)
      
      
      
  elif player_level == "Hard":
    chances = 0
    max_guess = 3
    number = random.randint(1, 50)
    print("Guess a number between 1 and 50")
    
    while chances < max_guess:
      guess = int(input("Guess: "))
      max_guess -= 1
      print(f"You have {max_guess} guess(es) left.")
      
      if guess == number:
        print("You got it right!")
        break
       
      elif guess < number:
        print("That was wrong! Guess a higher number.")
        
      else:
        print("That was wrong! Guess a lower number.")
        
    if chances == max_guess:
      print("Game Over! The number is", number) 
      
      
      
    












