#Hook-up a single color LED to LED port 1.

from HummingbirdPython12.hummingbird import Hummingbird
from time import sleep
import atexit

myHummingbird = Hummingbird()

def goodbyeMyHummingbird() :
    myHummingbird.close()
    
atexit.register(goodbyeMyHummingbird)

while(True) :
    myHummingbird.set_single_led(1,255)
    sleep(1)
    myHummingbird.set_single_led(1,0)
    sleep(1)

