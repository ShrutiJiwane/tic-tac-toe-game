import random

gameboard= ['-','-','-','-','-','-','-','-','-']
player= "x"
winner = None
gamerunning = True

#printing the game board
def printboard(gameboard):
    print(gameboard[0]+"|"+gameboard[1]+"|"+gameboard[2])
    print("-----")
    print(gameboard[3]+"|"+gameboard[4]+"|"+gameboard[5])
    print("-----")
    print(gameboard[6]+"|"+gameboard[7]+"|"+gameboard[8])   

#take input from player
def playerinput(gameboard):
    inp = int(input("enter position number : "))
    if inp>=1 and inp<=9 and gameboard[inp-1] == "-":
        gameboard[inp-1]= player
    else:
        print("oops! player is already in that spot OR give the input from 1-9 ")

#check for win or tie

def checkhorizontal(gameboard):
    global winner
    if gameboard[0]==gameboard[1]==gameboard[2] and gameboard[1]!= "-":
        winner = gameboard[0]
        return True
    elif gameboard[3]==gameboard[4]==gameboard[5] and gameboard[4]!= "-":
        winner = gameboard[3]
        return True
    elif gameboard[6]==gameboard[7]==gameboard[8] and gameboard[7]!= "-":
        winner = gameboard[6]
        return True
    
def checkverticle(gameboard):
    global winner
    if gameboard[0]==gameboard[3]==gameboard[6] and gameboard[3]!= "-":
        winner = gameboard[0]
        return True
    elif gameboard[1]==gameboard[4]==gameboard[7] and gameboard[4]!= "-":
        winner = gameboard[1]
        return True
    elif gameboard[2]==gameboard[5]==gameboard[8] and gameboard[5]!= "-":
        winner = gameboard[2]
        return True

def checkdiagonal(gameboard):
    global winner
    if gameboard[0]==gameboard[4]==gameboard[8] and gameboard[0]!= "-":
        winner = gameboard[0]
        return True
    elif gameboard[2]==gameboard[4]==gameboard[6] and gameboard[2]!= "-":
        winner = gameboard[2]
        return True
    
#check tie
def checktie(gameboard):
    global gamerunning
    if "-" not in gameboard:
        printboard(gameboard)
        print("it is a tie!")
        gamerunning = False


#check win
def checkwin(gameboard):
    global gamerunning
    if checkdiagonal(gameboard) or checkhorizontal(gameboard) or checkverticle(gameboard):
        printboard(gameboard)
        print(f"the winner is {winner}")
        gamerunning = False
        

# switch player
def switchplayer(gameboard):
    global player
    if player == "x":
        player = "o"
    else:
        player = "x"

# computer
def computer(gameboard):
    while player == "o":
        position = random.randint(0,8)
        if gameboard[position] == "-":
            gameboard[position] = "o"
            switchplayer(gameboard)

while gamerunning:
    printboard(gameboard)
    playerinput(gameboard)
    checkwin(gameboard)
    checktie(gameboard)
    switchplayer(gameboard)
    computer(gameboard)
