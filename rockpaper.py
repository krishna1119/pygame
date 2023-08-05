
import random

def play():
    user_count=0
    computer_count=0
    total=input("enter the total score")
    i=0
    while i< int(total):  
      user= input("enter 'r' for rock 'p'p for paper 's' for scissors" )
      computer= random.choice(['r', 'p','s'])
      print("ur choice:" + user)
      print("computers choice:" + computer)

      if user== computer:
          print("tie")
    
      elif win(user,computer):
          print( "you have won")
          user_count= user_count + 1
    
      else:
          print( "you have lost")
          computer_count= computer_count+ 1
      print("user points is: " + str(user_count))
      print("computer points: " + str(computer_count))      
     
      if  computer_count>user_count:
           greatest= computer_count
      else:
          greatest= user_count
      i= greatest
    if computer_count < total:  
        print("YOU HAVE LOST")
    else:
        print("YOU HAVE WON")

def win(player, computer):
    if (player=='r' and computer=='s') or (player=='s' and computer=='p') or (player=='p' and computer=='r'):
        return True

play()


