import audio
import motor
from inputs import get_gamepad
import threading
from time import sleep

#define controller class
class XboxController(object):
    MAX_TRIGGER_VALUE = 255
    MAX_JOYSTICK_VALUE = 32767

    def __init__(self):
        self.LeftJoystickX = 0
        self.LeftJoystickY = 0
        self.RightJoystickX = 0
        self.RightJoystickY = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.A = 0
        self.B = 0
        self.X = 0
        self.Y = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def read(self):
        x = self.LeftJoystickX
        y = self.LeftJoystickY
        a = self.A
        b = self.X #returns 1 if b, 2 if x
        lookX = self.RightJoystickX
        lookY = self.RightJoystickY
        return [x,y,a,b,lookX,lookY]
    
    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOYSTICK_VALUE
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOYSTICK_VALUE
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOYSTICK_VALUE
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOYSTICK_VALUE
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_WEST':
                    self.X = event.state

def RPsetup():
    motor.setup()
if __name__ == '__main__':
    RPsetup()
    c = XboxController()
    while True:
        x,y,a,b,lookX,lookY = c.read()
        if a != 0: #play random sound from voicelines if a is pressed
            audio.play_random()
        if b != 0: #emergency stop if b is pressed
            motor.stop()
        motor.move(x,y)
        motor.look(lookX,lookY)
        sleep(0.1)