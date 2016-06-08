X = "X";
O = "O";
EMPTY = " ";
SIZE = 9;

turn = "";
human = "";
computer = "";

def main():
    if (yes_no("Would you like to go first?") == "y"):
        human = X;
        computer = O;
        turn = human;
    else:
        human = O;
        computer = X;
        turn = computer;
    board = [];
    setup_board(board);
    showInstructions();
    isInGame = inGame(board);
    while (isInGame):
        takeTurn(turn, board, human, computer);
        drawBoard(board, human, computer);
        if (checkWin(board, human, computer) == "human"):
            print("\n"+win("human"));
            break;
        elif (checkWin(board, human, computer) == "computer"):
            print("\n"+win("computer"));
            break;
        turn = switchTurn(turn, human, computer);
        temp = inGame(board);
        if (temp == "yes"):
            isInGame = "yes";
        else:
            break;
    return "";
def showInstructions():
    sep = " | ";
    print("\n 0 " + sep + " 1 " + sep + " 2 ");
    print(" 3 " + sep + " 4 " + sep + " 5 ");
    print(" 6 " + sep + " 7 " + sep + " 8 \n");
    
def checkWin(b, h, c):
    combinations = ([0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]);
    for comb in combinations:
        if (b[comb[0]] == h and b[comb[1]] == h and b[comb[2]] == h):
            return "human";
        if (b[comb[0]] == c and b[comb[1]] == c and b[comb[2]] == c):
            return "computer";
    return "no";

def drawBoard(b, h, c):
    sep = " | ";
    print("\n"+b[0]+sep+ b[1]+sep+b[2]);
    print(b[3]+sep+b[4]+sep+b[5]);
    print(b[6]+sep+b[7]+sep+b[8]+"\n");
    print("---KEY---\nPlayer - " + h + "\nComputer - " + c);
    
def switchTurn(turn, h, c):
    if (turn == h):
        return c;
    else:
        return h;
 
 
def takeTurn(t, b, h, c):
    if (t == h):
        legal = legalMoves(b);
        index = int(input("\nWhere would you like to go?\n"));
        while (index not in legal):
            index = int(input("That is not a legal move, please try again. The legal moves are:\n" + str(legal)));
        b[index] = h;
    else:
        legal = legalMoves(b);
        index = legal[0];
        print("Computer taking the position of: " + str(index));
        b[index] = c;
    

def willWin(space, h, b):
    combinations = ([0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]);
    for combination in combinations:
        if (space in combination):
            for com in combination:
                if (com != space):
                    if (b[com] == h):
                        return "no";
    return "yes";

def win(winner):
    if (winner == "human"):
        return "You win! Congratulations.";
    elif (winner == "computer"):
        return "You lose.";
    else:
        return "Huh?";

def inGame(b):
    if(len(legalMoves(b)) > 0):
        return "yes";
    return "no";
 
 
def legalMoves(b):
    legal = [];
    c = 0;
    for square in b:
        if (square == EMPTY):
            legal.append(c);
        c += 1;
    return legal;
    

def setup_board(b):
    counter = 0;
    while (counter < SIZE):
        b.append(EMPTY);
        counter += 1;

def yes_no(q):
    i = input("\n" + q + " (y/n)\n");
    while (i is not "y" and i is not "Y" and i is not "N" and i is not "n"):
        i = input("\n" + q + "(y/n)\n");
    return i.lower();
    
    
def ComputerMoves(c):
     def decision(mytype):
	mymove = 10
	enemytype = "O"
	if mytype == "O":
		enemytype = "X"
	for move in board:
		if board[move] == mytype:
			topmove = True
			bottommove = True
			leftmove = True
			rightmove = True
			if move <= 3:
				topmove = False
			if (move - 1) % 3 == 0:
				leftmove = False
			if move % 3 == 0:
				rightmove = False
			if move >= 7:
				bottommove = False

			if not bottommove:
				if board[move - 3] == mytype and not board[move - 6]:
					mymove = move - 6
					break
				elif not leftmove and board[5] == mytype and not board[3]:
					mymove = 3
					break
				elif not rightmove and board[5] == mytype and not board[1]:
					mymove = 1
					break
				elif board[move - 3] == mytype and not board[move - 6]:
					mymove = move - 6
					break
				elif not board[move - 3] and board[move - 6] == mytype:
					mymove = move - 3
					break
				elif not leftmove and board[5] == mytype and not board[3]:
					mymove = 3
					break
				elif not leftmove and not board[5] and board[3] == mytype:
					mymove = 5
					break
				elif not rightmove and board[5] == mytype and not board[1]:
					mymove = 1
					break
				elif not rightmove and not board[5] and board[1] == mytype:
					mymove = 5
					break
			elif not topmove:
				if board[move + 3] == mytype and not board[move + 6]:
					mymove = move + 6
					break
				elif not board[move + 3] and board[move + 6] == mytype:
					mymove = move + 3
					break
				elif not leftmove and board[5] == mytype and not board[9]:
					mymove = 9
					break
				elif not leftmove and not board[5] and board[9] == mytype:
					mymove = 5
					break
				elif not rightmove and board[5] == mytype and not board[7]:
					mymove = 7
					break
				elif not rightmove and not board[5] and board[7] == mytype:
					mymove = 5
					break
			else:
				if board[move - 3] == mytype and not board[move + 3]:
					mymove = move + 3
					break
				elif board[move + 3] == mytype and not board[move - 3]:
					mymove = move - 3
					break
				elif not leftmove and board[5] == mytype and not board[6]:
					mymove = 6
					break
				elif not leftmove and not board[5] and board[6] == mytype:
					mymove = 5
					break
				elif not rightmove and board[5] == mytype and not board[4]:
					mymove = 4
					break
				elif not rightmove and not board[5] and board[4] == mytype:
					mymove = 5
					break
main();
print("Thank you for playing.");
