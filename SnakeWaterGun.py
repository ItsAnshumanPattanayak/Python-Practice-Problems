'''
1 for snake 
-1 for water
0 for gun
'''

import random
youDict = {"s":1 , "w":-1 , "g" : 0}
reverseDict = {1:"Snake" , -1:"Water" , 0:"Gun"}

while True:
    user = input("Enter Your choice (s = snake , w = water , g = gun , q = quit : )")

    if user == "q":
        print("Thanks for playing")
        break

    computer = random.choice([1,-1,0])
    you = youDict[user]
    print("You choose" , reverseDict[you],"\n", "Computer choose " , reverseDict[computer])

    #cases 
    if(computer == you):
        print("Its a DRAW!")
    else:

        if(computer == 1 and you == -1):
            print("You Loose!")
        elif(computer == 1 and you == 0):
            print("You Win!")
        if(computer == -1 and you == 1):
            print("You Win!")
        elif(computer == -1 and you == 0):
            print("You Loose!")
        if(computer == 0 and you == -1):
            print("You Win!")
        elif(computer == 0 and you == 1):
            print("You Loose!")

