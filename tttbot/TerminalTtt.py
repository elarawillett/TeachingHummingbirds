from time import sleep
from random import randint
import sys

NONE = 0
COMP = 1
HUMAN = 2

board = [0,0,0,0,0,0,0,0,0]
turn = HUMAN
winner = NONE


def printBoard() :
	displayBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	for i in range(9) :
		player = board[i]		
		if player == COMP :
			displayBoard[i] = 'X'
		elif player == HUMAN :
			displayBoard[i] = 'O'

	print("%s | %s | %s" % (displayBoard[0],displayBoard[1],displayBoard[2]))
	print("---------")
	print("%s | %s | %s" % (displayBoard[3],displayBoard[4],displayBoard[5]))
	print("---------")
	print("%s | %s | %s" % (displayBoard[6],displayBoard[7],displayBoard[8]))	


def getWinner(spot1,spot2,spot3) :
	if COMP == spot1 == spot2 == spot3 :
		return COMP
	elif HUMAN == spot1 == spot2 == spot3 :
		return HUMAN
	else :
		return NONE

def gameStillGoing() :
	global winner
	winner = max(winner,getWinner(board[0],board[1],board[2]))
	winner = max(winner,getWinner(board[3],board[4],board[5]))
	winner = max(winner,getWinner(board[6],board[7],board[8]))
	winner = max(winner,getWinner(board[0],board[3],board[6]))
	winner = max(winner,getWinner(board[1],board[4],board[7]))
	winner = max(winner,getWinner(board[2],board[5],board[8]))
	winner = max(winner,getWinner(board[0],board[4],board[8]))
	winner = max(winner,getWinner(board[2],board[4],board[6]))
	if winner == NONE :
		gameBoardFull = True
		for i in range(9) :
			if board[i] == NONE :
				gameBoardFull = False
		return not gameBoardFull
	else :
		return False

def strategy() :
	move = winningMoveFor(COMP)
	if move != -1 :
		return move	

	move = winningMoveFor(HUMAN)
	if move != -1 :
		print("You can't fool me that easily, human!")
		return move

	if board[0] == NONE :
		return 0
	
	if board[8] == NONE :
		return 8

	if board[2] == NONE :
		return 8

	if board[6] == NONE :
		return 8

	return randomMove()


def winningMoveFor(player) :

	move = specificWinningMove(0,1,2,player)
	if move != -1 :
		return move

	move = specificWinningMove(3,4,5,player)
	if move != -1 :
		return move

	move = specificWinningMove(6,7,8,player)
	if move != -1 :
		return move

	move = specificWinningMove(0,3,6,player)
	if move != -1 :
		return move

	move = specificWinningMove(1,4,7,player)
	if move != -1 :
		return move

	move = specificWinningMove(2,5,8,player)
	if move != -1 :
		return move

	move = specificWinningMove(0,4,8,player)
	if move != -1 :
		return move

	move = specificWinningMove(2,4,6,player)
	if move != -1 :
		return move
	
	return -1
		

def specificWinningMove(spot1,spot2,spot3,player) :
	if (board[spot1]==player) and (board[spot2]==player) and (board[spot3]==NONE) :
		return spot3
	if (board[spot1]==player) and (board[spot2]==NONE) and (board[spot3]==player) :
		return spot2
	if (board[spot1]==NONE) and (board[spot2]==player) and (board[spot3]==player) :
		return spot1
	return -1


def randomMove() :
	move = randint(0,8)
	while board[move] != NONE :
		move = randint(0,8)
	return move


if len(sys.argv) == 1 :
	print("Let's play tic-tac-toe!")
	sleep(1)
	print("You'll need to input your moves as numbers between 0 and 8.")
	sleep(2)
	print("See how the numbers indicate positions on the board: ")
	sleep(2)
	print("0 | 1 | 2")
	print("---------")
	print("3 | 4 | 5")
	print("---------")
	print("6 | 7 | 8")
	sleep(2)

print("I would really like to go first. Is that okay?")
playerInput = int(raw_input("Press 1 if okay, and 0 otherwise: "))
if playerInput == 1 :
	turn = COMP
	print("Ok, me first. I'm always X's.")
elif playerInput == 0 :
	turn = HUMAN
	print("Ok, you first, but I'm always X's")
else :
	print("I didn't understand that, so I'll just go first. I'm always X's.")
	turn = COMP
sleep(.5)
	
		
while gameStillGoing() :
	if turn == COMP :
		computerMove = strategy()
		board[computerMove] = COMP
		print("My move is %d." % computerMove)
		printBoard()
		sleep(.5)
		turn = HUMAN
	else :
		print("What's your move?")
		sleep(.5)
		humanMove = int(input("Enter 0-8: "))
		if (0 <= humanMove < 9) and (board[humanMove]==NONE) :
			board[humanMove] = HUMAN
			turn = COMP
		else : 
			print("Not valid move.")
		sleep(.5)


		
if winner == HUMAN :
	print("Well played, human. You won.")
elif winner == COMP :
	print("Ahhhahhhaaa I won!")
else : 
	print("Cat's game!")
