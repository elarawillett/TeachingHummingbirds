TURNQUERY = "cover the light sensor for 3 seconds if you want to go first"
HUMANGOESFIRST = "fine. you first. use the nob to select your move then cover the lite sensor"
ROBOTGOESFIRST = "cool. me first. wen its your turn, use the nob to select your move then cover the lite sensor"
MOVEANNOUNCMENT = "heres my move"
MOVEQUERY = "wats your move"
MOVERESPONSE = "oh kay my turn"


def introDance(robot, robotVoice) :
	robotVoice.Speak("lets play")


def winningDance(robot, robotVoice) :
	robotVoice.Speak("i won")


def losingDance(robot, robotVoice) :
	robotVoice.Speak("i lost")


def catDance(robot, robotVoice) :
	robotVoice.Speak("we tied")