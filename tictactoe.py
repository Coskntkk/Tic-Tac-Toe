import random,tictactoeai,time
# this is a simple tic-tac-toe game
# ----------------- GLOBAL VARIABLES ----------------- 

# liste that is the map of tic-tac-toe
liste = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"],
]

# empty areas on map
playable = []

win_check = False

# print map
def maps(liste):
    map = """
      | 0 | 1 | 2 | 
    --+---+---+---+
    0 | {} | {} | {} 
    --+---+---+---+
    1 | {} | {} | {} 
    --+---+---+---+
    2 | {} | {} | {} 
    """.format(liste[0][0],liste[0][1],liste[0][2],liste[1][0],liste[1][1],liste[1][2],liste[2][0],liste[2][1],liste[2][2])
    return map

# player movement 
def playerMove(liste):
    print("Player 1's turn.")
    row = int(input("Row: "))
    column = int(input("Column: "))
    if(liste[row][column] == "-"):
        liste[row][column] = "X"
    else:
        print("Player can't move here.")
        print("Try again.")
        playerMove(liste)
    print(maps(liste))

# player2 movement
def player2Move(liste):
    print("Player 2's turn.")
    row = int(input("Row: "))
    column = int(input("Column: "))
    if(liste[row][column] == "-"):
        liste[row][column] = "O"
    else:
        print("Player can't move here.")
        print("Try again.")
        player2Move(liste)
    print(maps(liste))

# computer movement
def computerMove(liste,playable):
    tictactoeai.computerAI(liste)

    print("Computer moved")
    print(maps(liste))


# function to check if there is any win situation
def winCheck(liste):
    # check row 
    for row in range(3):
        if(liste[row][0] == liste[row][1] and liste[row][0] == liste[row][2] and liste[row][0] != "-"):
            return True

    # check column 
    for column in range(3):
        if(liste[0][column] == liste[1][column] and liste[0][column] == liste[2][column] and liste[0][column] != "-"):
            return True

    # check diagonally
    if(liste[0][0] == liste[1][1] and liste[0][0] == liste[2][2] and liste[1][1] != "-"):
        return True
    if(liste[0][2] == liste[1][1] and liste[0][2] == liste[2][0] and liste[1][1] != "-"):
        return True

    # there is no win..
    else:
        return False

# function for waiting
def waiting():
    print("Computer moving")
    print("...")
    time.sleep(0.75)
    print("..")
    time.sleep(0.75)
    print(".")
    time.sleep(0.75)

# player vs computer mod
def gamePvC(liste):
    print("""Player is "X".""")
    print(maps(liste))
    print("-------------------------------")
    pvcCount = 9
    while(winCheck(liste) == False):
        playerMove(liste)
        pvcCount -= 1
        print("-------------------------------")
        if(winCheck(liste) == True):
            print("Player won.")
            break
        if(pvcCount == 0):
            print("Draw. Nobody won, nobody lost.")
            break
        waiting()
        computerMove(liste,playable) ###############################################
        pvcCount -= 1
        print("-------------------------------")
        if(winCheck(liste) == True):
            print("Computer won.")
            break
        if(pvcCount == 0):
            print("Draw. Nobody won, nobody lost.")
            break

# player vs player mod
def gamePvP(liste):
    print("""Player 1 is "X".""")
    print("""Player 2 is "O".""")    
    print(maps(liste))
    print("-------------------------------")
    pvpCount = 9
    while(winCheck(liste) == False):
        playerMove(liste)
        pvpCount -= 1
        print("-------------------------------")
        if(winCheck(liste) == True):
            print("Player 1 won.")
            break
        if(pvpCount == 0):
            print("Draw. Nobody won, nobody lost.")
            break
        player2Move(liste)
        pvpCount -= 1
        print("-------------------------------")
        if(winCheck(liste) == True):
            print("Player 2 won.")
            break
        if(pvpCount == 0):
            print("Draw. Nobody won, nobody lost.")
            break

# main menu function
def main():
    print("Welcome to Tic-Tac-Toe Game! ")
    print("Choose one:")
    print("""
1 - Read Tic-Tac-Toe Rules
2 - Play Tic-Tac-Toe against computer.
3 - Play Tic-Tac-Toe against player.
""") 
    choice = int(input(">>>"))
    if(choice == 1):
        print("this is a game.")
        choice2 = input("wanna play? (y/n)")
        if(choice2 == "y" or choice2 == "Y"):
            main()
        else:
            game_exit()
    elif(choice == 2): 
        liste = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"],
        ]
        gamePvC(liste)
    elif(choice == 3):
        liste = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"],
        ]
        gamePvP(liste)
    play_again = input("Do you want to play again? (Y/N): ")
    if(play_again == "Y" or play_again == "y"):
        main()
    elif(play_again == "N" or play_again == "n"):
        game_exit()

def game_exit():
    print("Bye...")
        
# 1 - Read Tic-Tac-Toe Rules
# 2 - Play Tic-Tac-Toe
main()

# UPDATES -->
# 06.03.21
    # simple win mechanic is implemented.
    # menu added
    # need to be improved: 
        # game explanation is.. a bit short.
        # computer is silly af 
# 07.03.21
        # pvp option added
        # draw option is recognized.

# CREDITS: CAGLA & COSKUN 