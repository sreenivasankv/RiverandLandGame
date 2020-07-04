#########Step2############

import pandas as pd
data = pd.read_csv("Task_Training_Data .csv")
chance = 1
data["Name"] = data["Name"].map(str.strip)
data["Email"] = data["Email"].map(str.strip)


while True:
    if chance == 3:
        print("You are not allowed to play the game")
        exit()
    name, email = input("Enter name and email seperated by comma").split(',')
    name = name.strip()
    email = email.strip()
    if name in data["Name"].values and email in data["Email"].values:
        print("Congratulations. You can play the game")
        break
    chance += 1

print("\"Welcome to the brain game of River and Land : Just Remember what you give\"")
print("Quote: This game can boot your Stress or you will be happy , will become a myth")
choice = input("Do you want to enter the game (Yes or No)")
if choice == 'No':
    print("Thank You")
    exit()
play=""
while True:
    try:
        if play == "P":
            break
        if play != 'P' or play == "":
            play = input("Press P to play")
            if play != 'P' or play == "":
                assaa
    except:
        print("You Entered the wrong choice, Enter P to play")
        pass


def River(grid):
    L=[]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            k = [0]
            if grid[r][c] == "1":
                compute(grid, r, c, k)
                L.append(k)
    return L


def compute(grid, i, j, k):
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    grid[i][j] = "0"
    k[0] += 1
    for dir in directions:
        newr, newc = i + dir[0], j + dir[1]
        if newr >= 0 and newc >= 0 and newr < len(grid) and newc < len(grid[0]):
            if grid[newr][newc] == "1":
                compute(grid, newr, newc, k)


def play_game():
    row,col = input("Enter Rows and Columns seperated by space").split()
    row,col = int(row), int(col)
    grid = []
    for i in range(row):
        print("Enter values for row", i+1)
        inp = []
        inp = list(num for num in input("Enter the column numbers separated by space ").strip().split())[:col]
        grid.append(inp)
    grid = [['1', '0', '0', '1', '0'], ['1', '0', '1', '0', '0'], ['0', '0', '1', '0', '1'],
            ['1', '0', '1', '0', '1'], ['1', '0', '1', '1', '0']]
    riv = River(grid)
    output = [item for sublist in riv for item in sublist]
    realLen = len(output)
    guessLen = 0
    for i in range(realLen):
        print("Enter your guess for row", i + 1)
        guessNum = int(input())
        if guessNum == output[i]:
            print("You guessed correct")
            guessLen += 1
        else:
            print("You guessed wrong")
    if guessLen == realLen:
        print("You are the winner!!!")
    elif (guessLen / realLen) * 100 == 60:
        print("You got second position!!!")
    else:
        print("Invest more money on Almonds, then come back")
    if input("Do you want to play again (Yes/No)") == 'Yes':
        play_game()
    else:
        print("Thank You for playing the game")


play_game()







