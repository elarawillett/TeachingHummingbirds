from random import randint
NONE = 0
COMP = 1
HUMAN = 2


# This function returns a position for the robot to play.
# To check if the board is empty, do for example:    (== means equal)
#
#	if board[0] == NONE :
#		return 0
#
# If the computer already played in position 0, then board[0] equals COMP.
# If the human already played in position 0, then board[0] equals HUMAN.
#
# Recall that the positions in the board are numbered like so:
#	 0 | 1 | 2
#	-----------
#	 3 | 4 | 5
#	-----------
#	 6 | 7 | 8
#
def strategy(board) :

	#
	#
	#
	# YOUR CODE HERE
	#
	#
	#

	return randomMove()	



# This function returns a random position that hasn't been played yet.
def randomMove() :
	move = randint(0,8)
	while board[move] != NONE :
		move = randint(0,8)
	return move



# This function returns the position of a winning move for the player specified.
# Put either COMP or HUMAN in the parenthesis. For example:
#
# 	move = winningMoveFor(COMP)
#
# If you write the above then 'move' will contain the position of a winning move 
# for the computer OR IF THERE IS NO WINNING MOVE then 'move' will contain -1
#
# Now you might use 'move' as follows:    (!= means not equal)
#
#	if move != -1 :
#		return move
#
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
		
#This is just a helper function for the winningMoveFor(player) function
def specificWinningMove(spot1,spot2,spot3,player) :
	if (board[spot1]==player) and (board[spot2]==player) and (board[spot3]==NONE) :
		return spot3
	if (board[spot1]==player) and (board[spot2]==NONE) and (board[spot3]==player) :
		return spot2
	if (board[spot1]==NONE) and (board[spot2]==player) and (board[spot3]==player) :
		return spot1
	return -1
