from math import sin, cos
from typing import overload
from pylx16a.lx16a import *
import time

LX16A.initialize("COM4", 0.1)

#set limits and functions
def over_temp():
    if LX16A.get_temp()<40:
        return True
    else:
        return False
    
def over_volt():
    if LX16A.get_vin()<5000:
        return True
    else:
        return False


#check for errors in each motor
for x in range (1,1,6):
    Lx16A(x).servo_mode()
    LX16A(x).enable_torque()
    #errors set
    LX16A(x).set_led_error_triggers(over_temp(), over_volt(), LX16A(x).is_torque_enabled())

#get homing position
    LX16A(x).get_physical_angle() == 120
    while False:
        LX16A(x).move(10,10)


try:
    servo1 = LX16A(4)
    servo2 = LX16A(5)
    #servo3 = LX16A(6)
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
while True:
    servo1.move(sin(t) * 10 + 20)
    servo2.move(cos(t) * 10 + 20)
    #servo3.move(sin(t)* 10 + 30)

    time.sleep(0.1)
    t += 1
