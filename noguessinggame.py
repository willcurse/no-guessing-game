from random import randint
easy_level=10
hard_level=5

def check(guess,turn,number):
  if guess>number:
    print("Nhhh!TOOO HIGH")
    return turn-1
  elif guess<number:
    print("Nhhh!TOO LOW")
    return turn-1
  else:
    print(f"Hurrey! you got it right {number}")


def set_difficulty():
  level=input("enter the level of difficulty 'easy' & 'hard'-: ")
  if level=="easy":
    return easy_level
  else:
    return hard_level

def game():
  print("WELCOME TO THE UTKARSH NUMBER GUESSING GAME")
  print("Good! Now guess the number between 1-100 ")
  number=randint(1,100)
  turn=set_difficulty()

  guess=0
  while guess!=number:
    print(f"you have {turn} turns left now...")
    guess=int(input("enter the number to guess\n"))

    turn=check(guess,turn,number)
    if turn==0:
      print("you loose, cz you ran out of turns...")
    elif guess!=number:
      print("guess again")

game()






