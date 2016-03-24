from random import randint

NONE = 0
COMP = 1
HUMAN = 2
winner = NONE

def getWinner(spot1,spot2,spot3) :
	if COMP == spot1 == spot2 == spot3 :
		return COMP
	elif HUMAN == spot1 == spot2 == spot3 :
		return HUMAN
	else :
		return NONE

def gameStillGoing(board) :
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

def lightBoard(robot, position) :
	boardLeds = [0,0,0,0,0,0,0,0,0]
	boardLeds[position] = 255	
	robot.set_single_led(2,boardLeds[0])
	robot.set_single_led(3,boardLeds[1])
	robot.set_single_led(4,boardLeds[2])
	robot.set_tricolor_led(1,boardLeds[3],boardLeds[4],boardLeds[5])
	robot.set_tricolor_led(2,boardLeds[6],boardLeds[7],boardLeds[8])

def checkValidity(move,board) :

	moveIsInt = isinstance(move, int)	
	if not moveIsInt :
		print("Oops. Your strategy returned a position that is not an integer.")
		return False
	
	movePositive = (move >= 0)
	if not movePositive :
		print("Oops. Your strategy returned a position that is negative.")
		return False
	
	moveSmallEnough = (move <= 8)
	if not moveSmallEnough :
		print("Oops. Your strategy returned a position that is greater than 8.")
		return False
	
	moveAvailable = (board[move] == NONE)
	if not moveAvailable :
		print("Oops. Your strategy returned a position that is already taken.")
		return False

	return True


def defaultStrategy(board) :
	move = randint(0,8)
	while board[move] != NONE :
		move = randint(0,8)
	return move


class DefaultRobotVoice :
	def Speak(self, words) :
		print(words)


class DefaultRobot :
	def get_light_sensor(self,port) :
		return randint(0,255)
	def get_knob_value(self,port) :
		return randint(0,255)
	def set_single_led(self,port, color) :
		print("LED lit")
	def set_tricolor_led(self,port, color1, color2, color3) :
		print("LED lit")
	def close(self) :
		print("Closing default robot.")


