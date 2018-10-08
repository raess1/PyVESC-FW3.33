# NOTE: this is for VESC firmware 3.33 
# ( https://github.com/tlalexander/bldc/tree/e74d3a3e4c2047b239084c152b4cbfddafbe3145 )

from pyvesc.messages.base import VESCMessage



class SetDutyCycle(metaclass=VESCMessage):
    """ Set the duty cycle.

    :ivar duty_cycle: Value of duty cycle to be set (range [-1e5, 1e5]).
    """
    id = 5   # COMM_SET_DUTY
    can_id = None
    fields = [
        ('duty_cycle', 'i')
    ]


class SetRPM(metaclass=VESCMessage):
    """ Set the RPM.

    :ivar rpm: Value to set the RPM to.
    """
    id = 8  # COMM_SET_RPM
    can_id = None
    fields = [
        ('rpm', 'i')
    ]


class SetCurrent(metaclass=VESCMessage):
    """ Set the current (in milliamps) to the motor.

    :ivar current: Value to set the current to (in milliamps).
    """
    id = 6  # COMM_SET_CURRENT
    fields = [
        ('current', 'i')
    ]


class SetCurrentBrake(metaclass=VESCMessage):
    """ Set the current brake (in milliamps).

    :ivar current_brake: Value to set the current brake to (in milliamps).
    """
    id = 7  # 	COMM_SET_CURRENT_BRAKE
    can_id = None
    fields = [
        ('current_brake', 'i')
    ]

class SetPosition(metaclass=VESCMessage):
    """Set the rotor angle based off of an encoder or sensor
    
    :ivar pos: Value to set the current position or angle to.
    """
    id = 9  # COMM_SET_POS
    can_id = None
    fields = [
        ('pos', 'i', 1000000)
    ]
    
class SetPositionLarge(metaclass=VESCMessage):
    """Set the rotor angle based off of an encoder or sensor
    
    :ivar pos: Value to set the current position or angle to.
    """
    id = 40  # COMM_SET_POS_LARGE
    can_id = None
    fields = [
        ('pos', 'i', 100000)
    
    
class SetRotorPositionMode(metaclass=VESCMessage):
    """Sets the rotor position feedback mode.
        
    It is reccomended to use the defined modes as below:
        * DISP_POS_OFF
        * DISP_POS_MODE_ENCODER
        * DISP_POS_MODE_PID_POS
        * DISP_POS_MODE_PID_POS_ERROR
    
    :ivar pos_mode: Value of the mode
    """

    DISP_POS_OFF = 0
    DISP_POS_MODE_INDUCTANCE = 1
    DISP_POS_MODE_OBSERVER = 2
    DISP_POS_MODE_ENCODER = 3
    DISP_POS_MODE_PID_POS = 4
    DISP_POS_MODE_PID_POS_ERROR = 5
    DISP_POS_MODE_ENCODER_OBSERVER_ERROR = 6
    
    id = 11  #  COMM_SET_DETECT
    can_id = None
    fields = [
        ('pos_mode', 'b')
    ]

    
class SetCurrentGetPosCumulative(metaclass=VESCMessage):    
    id = 39  # COMM_SET_CURRENT_GET_POSITION
    fields = [
        ('current', 'i')
    ]

    