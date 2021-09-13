print("***WELCOME TO GUESSING GAME NUMBER***")
question=input("Do u want to play this game? ")
if question=="yes":
    print("let's start the number guessing game.")
import random
num=random.randint(1,10)
count=0
num=5
# while num!="guess":
#     if count==3:
#         print("sorry you lost the game !!!Better luck next time.")
#         break
#     guess=int(input("Enter a guessing number: "))
#     if guess<num:
#         print("guess is low.")
        
#     elif guess>num:
#         print("guess is high.")
        
#     else:
#         print("you guess it .")
#         break
    # count+=1
guess=int(input("enter ur guess number: "))
while num!="guess":
    if guess<num:
        print("guess is too low.")
    elif guess>num:
        print("guess is too high.")
    else:
        print("you guess it.")
        break
count+=1