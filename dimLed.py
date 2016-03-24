#Hook-up a single color LED to LED port 1.
#Hook-up a knob to sensor port 1.

from HummingbirdPython12.hummingbird import Hummingbird
import atexit

myHummingbird = Hummingbird()

def goodbyeMyHummingbird() :
    myHummingbird.close()
    
atexit.register(goodbyeMyHummingbird)

while(True) :
    
    knobOrientation = myHummingbird.get_knob_value(1)
    
    myHummingbird.set_single_led(1,knobOrientation)

