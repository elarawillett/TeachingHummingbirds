#Hook-up two single color LED to LED ports 1 and 2.
#Hook-up a knob to sensor port 1.

import threading
from HummingbirdPython12.hummingbird import Hummingbird
from time import sleep
import atexit


def blinkLed() :
    while(True) :
        myHummingbird.set_single_led(1,255)
        sleep(1)
        myHummingbird.set_single_led(1,0)
        sleep(1)



def dimLed() :
    while(True) :
        knobOrientation = myHummingbird.get_knob_value(1)
        myHummingbird.set_single_led(2,knobOrientation)


def goodbyeMyHummingbird() :
    myHummingbird.close()


    
atexit.register(goodbyeMyHummingbird)

myHummingbird = Hummingbird()

t1 = threading.Thread(target=blinkLed)
t2 = threading.Thread(target=dimLed)

t1.start()
t2.start()
    
    

