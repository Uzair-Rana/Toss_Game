import random
l = ["paper", "rock", "scissor"]

while True:
    userCount = 0
    computerCount = 0
    game = int(input('''
                   Game start...
                   1 Start playing...
                   2 No | Exit
                   '''))
    if game == 1:
        for a in range(1, 6):
            userchoice = int(input('''
                    1 Paper
                    2 Rock
                    3 Scissor
                  '''))
            computerChoice = random.choice(l)
            if userchoice == 1:
                userchoice = "Paper"
            elif userchoice == 2:
                userchoice = "rock"
            elif userchoice == 3:
                userchoice = "scissor"

            if userchoice == computerChoice:
                print("User choice is: ", userchoice)
                print("Computer choice is: ", computerChoice)
                print("Match draw")
                userCount = userCount+1
                print(userCount)
                computerCount = computerCount+1
                print(computerCount)
            elif (userchoice == "Paper" and computerChoice == "rock") or (userchoice == "rock" and computerChoice == "scissor") or (userchoice == "scissor" and computerChoice == "paper"):
                print("User choice is: ", userchoice)
                print("Computer choice is: ", computerChoice)
                print("User win")
                userCount = userCount+1
                print("User count is ", userCount)
                print("Computer count is", computerCount)
            else:
                print("User choice is: ", userchoice)
                print("Computer choice is: ", computerChoice)
                print("Computer win")
                computerCount = computerCount+1
                print("User count is ", userCount)
                print("Computer count is", computerCount)
            if computerCount > userCount:
                print("Computer win the game")
            elif computerCount < userCount:
                print("User win the game")
            else:
                print("Match is draw")
        else:
            break
11
