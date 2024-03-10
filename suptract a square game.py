# File: CS112_A1_T2_3_20231118.py
# Purpose:
"""This is a two-player mathematical game of strategy. It is played by two
 people with a pile of coins (or other tokens) between them. The players take turns removing
 coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, ...).
 The player who removes the last coin wins."""
# Author: Fatma Gad Mahmoud Alsaid
# ID: 20231118


import random
import math

print("***Welcome to subtract a square game***")


#the game description
print("This is a two-player mathematical game of strategy.")
print("It is played by two people with a pile of coins (or other tokens) between them. The players take turns removing coins from the pile,")
print("always removing a non-zero square number of coins (1, 4, 9, 16, …). The player who removes the last coin wins")
#start the game
choice1 = (input("Please enter A to start the game ")).upper()
while choice1 != "A" :
  choice1 = (input("Invalid choice please enter A to start the game")).upper()
  
tokens_number = random.randrange(200,500)#to choose a random number for tokens
print("tokens_number: ",tokens_number)
while True:
    player1_number =int(input("player1 please enter a number: "))#to check if player1 entered a siutable number
    while player1_number <=0 or player1_number > tokens_number or player1_number % math.sqrt(player1_number) !=0 :
        player1_number = int(input("invalid player1 please enter a number: "))
    tokens_number = tokens_number - player1_number#the new number of tokens
    if tokens_number <1 :#to check if the player1 is the winner
        print("player1 won")
        break
    else:print (tokens_number)
    player2_number =int(input("player2 please enter a number: "))#to check if player2 entered a siutable number
    while player2_number <=0 or player2_number > tokens_number or player2_number % math.sqrt(player2_number) !=0 :
        player2_number = int(input("invalid player2 please enter a number: "))
    tokens_number = tokens_number - player2_number#the new number of tokens
    if tokens_number <1 :#to check if the player2 is the winner
        print("player2 won")
        break
    else:print (tokens_number)
    
    
if tokens_number <1 :
    print("The game ended")



