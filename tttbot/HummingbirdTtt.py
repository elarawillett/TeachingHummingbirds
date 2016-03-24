# This is a program to help a Hummingbird play tic-tac-toe.
# For the program to work properly:
# -plug a light sensor into sensor port 1
# -plug a knob into sensor port 2
# -plug single LEDs into ports 2,3, aan 4
# -hack three single LEDs into each tricolor LED port :) 



######## SET-UP

# get code from other files
from time import sleep
#? import win32com.client
#? from HummingbirdPython12.hummingbird import Hummingbird
import RobotPersonality
import RobotStrategy
import HummingbirdTttHelper


# depending on the ambient light, set a threshold for the light sensor
# so we can use it like a button
lightThreshold = 20

# to make the code easier to read, we give names to the values used 
# to represent the computer and the human on the game board
NONE = 0
COMP = 1
HUMAN = 2

# these are the variables we use to keep track of the game
board = [NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE]
turn = COMP

# we create a robot variable that can control the Hummingbird
try :
	robot = Hummingbird()
except :
	print("Hummingbird is messed up. Using default robot.")
	robot = HummingbirdTttHelper.DefaultRobot()

# we create another variable that can talk through the computer
try :
	robotVoice = win32com.client.Dispatch("SAPI.SpVoice")
except :
	print("Talking is messed up. Using default voice.")
	robotVoice = HummingbirdTttHelper.DefaultRobotVoice()



######## PLAYING THE GAME

# robot does an intro dance
RobotPersonality.introDance(robot, robotVoice)

# we figure out who will go first
robotVoice.Speak(RobotPersonality.TURNQUERY)
sleep(2)
if robot.get_light_sensor(1) < lightThreshold :
	turn = HUMAN
	robotVoice.Speak(RobotPersonality.HUMANGOESFIRST)
else :
	robotVoice.Speak(RobotPersonality.ROBOTGOESFIRST)


# we keep repeating this loop until someone wins or there is a tie	
# each time through the loop either the computer moves or the human moves	

while HummingbirdTttHelper.gameStillGoing(board) :
	if turn == COMP :
		computerMove = RobotStrategy.strategy(board)
		validMove = HummingbirdTttHelper.checkValidity(computerMove, board)
		if not validMove :
			print("Using default strategy.")
			computerMove = HummingbirdTttHelper.defaultStrategy(board)
		board[computerMove] = COMP
		HummingbirdTttHelper.lightBoard(robot,computerMove)
		robotVoice.Speak(RobotPersonality.MOVEANNOUNCMENT)
		sleep(1)
		turn = HUMAN
	else :
		robotVoice.Speak(RobotPersonality.MOVEQUERY)	
		validMove = False
		humanMove = 0
		while (robot.get_light_sensor(1) < lightThreshold) or not validMove :
			
			knobPosition = robot.get_knob_value(2)
			if  knobPosition < 28 :
				if board[0] == NONE :
					HummingbirdTttHelper.lightBoard(robot, 0)
					humanMove = 0
					validMove = True
				else :
					validMove = False
			elif knobPosition < 56 :
				if board[1] == NONE :
					HummingbirdTttHelper.lightBoard(robot, 1)
					humanMove = 1
					validMove = True
				else :
					validMove = False
			elif knobPosition < 84 : 
				if board[2] == NONE :
					HummingbirdTttHelper.lightBoard(robot, 2)
					humanMove = 2
					validMove = True
				else :
					validMove = False
			elif knobPosition < 112 :
				if board[3] == NONE :
					HummingbirdTttHelper.lightBoard(robot, 3)
					humanMove = 3
					validMove = True
				else :
					validMove = False
			elif knobPosition < 140 :
				if board[4] == NONE :
					HummingbirdTttHelper.lightBoard(robot, 4)
					humanMove = 4
					validMove = True
				else :
					validMove = False
			elif knobPosition < 168 :
				if board[5] == NONE :
					HummingbirdTttHelper.lightBoard(robot, 5)
					humanMove = 5
					validMove = True
				else :
					validMove = False
			elif knobPosition < 196 :
				if board[6] == NONE :
					HummingbirdTttHelper.lightBoard(robot, 6)
					humanMove = 6
					validMove = True
				else :
					validMove = False
			elif knobPosition < 124 :
				if board[7] == NONE :
					HummingbirdTttHelper.lightBoard(robot, 7)
					humanMove = 7
					validMove = True
				else :
					validMove = False
			else :
				if board[8] == NONE :
					HummingbirdTttHelper.lightBoard(robot, 8)
					humanMove = 8
					validMove = True
				else :
					validMove = False
		
		board[humanMove] = HUMAN
		turn = COMP
		robotVoice.Speak(RobotPersonality.MOVERESPONSE)

# robot does a dance dependent on who won		
if HummingbirdTttHelper.winner == HUMAN :
	RobotPersonality.winningDance(robot,robotVoice)
elif HummingbirdTttHelper.winner == COMP :
	RobotPersonality.losingDance(robot,robotVoice)
else : 
	RobotPersonality.catDance(robot,robotVoice)

# we close the connection to the Hummingbird
robot.close()
