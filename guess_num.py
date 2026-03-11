# guessing number

# import random
# target = random.randint(1, 100)

# while True:
#     userchoice = input("guess the target or QUIT : ")
#     if (userchoice == "QUIT"):
#         break
#     userchoice= int(userchoice)
#     if (userchoice == target):
#         print("succes : correct guess !!")
#         break
    
#     elif(userchoice < target):
#         print("your number was too small. take a bigger guess... ")
#     else:
#         print("your number was too big. take a smaller guess... ")


# print("____GAME OVER____")                  



import random
tgt=random.randint(1,50)

while True:
    usr=input("guess or quit: ")
    if usr=="quit":
        break
    usr=int(usr)
    if(usr==tgt):
        print("sucss")
        break
    elif(usr>tgt):
        print("greater")
    else:
        print("small")
print("game over")        