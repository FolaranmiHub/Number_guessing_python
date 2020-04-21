import random

user_level = []
while user_level == [ ]:
  user_level = input("Please, enter Easy, Medium or Hard for your level: ")
    

chances = 0
max_guess = 6
while user_level == 'Easy':
  number = random.randint(1, 10)
  print("Guess a number between 1 and 10")
  
  try:
    guess = int(input())
    chances += 1
    max_guess -= 1
    print(f"You have {max_guess} guesses left")
    
    while chances < max_guess:
      
      if guess == number:
        
        print("You got it right")
        break
        
      elif guess < number:
        print("That was wrong: guess a number higher.")
        
      else:
        print("That was wrong: guess a number lower.")
      
      chances += 1
      
    if not chances < max_guess:
      print("Game Over! The number is", guess)
      
      
      
  except ValueError:
    print("Only integers are allowed.")
    
    
    

chances = 0
max_guess = 4
while user_level == 'Medium':
  number = random.randint(1, 20)
  print("input a number between 1 and 20")
  
  try:
    guess = int(input())
    chances += 1
    max_guess -= 1
    print(f"You have {max_guess} guesses left")
    
    if guess == number:
      print("You got it right")
      break
    elif guess < number:
      print("That was wrong: guess a number higher.")
    else:
      print("That was wrong: guess a number lower.")
      
      chances += 1
      
    if not chances < max_guess:
      print("Game Over! The number is", guess)
      break
      
      
  except ValueError:
    print("Only integers are allowed.")
    
    
 
 
chances = 0
max_guess = 3
while user_level == 'Hard':
  number = random.randint(1, 50)
  print("input a number between 1 and 50")
  
  try:
    guess = int(input())
    chances += 1
    max_guess -= 1
    print(f"You have {max_guess} guesses left")
    
    if guess == number:
      print("You got it right")
      break
    elif guess < number:
      print("That was wrong: guess a number higher.")
    else:
      print("That was wrong: guess a number lower.")
      
      chances += 1
      
    if not chances < max_guess:
      print("Game Over! The number is", guess)
      break
      
      
  except ValueError:
    print("Only integers are allowed.")
  
  
  
  
  
  
  