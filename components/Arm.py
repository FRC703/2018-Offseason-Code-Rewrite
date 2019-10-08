import wpilib
from magicbot import tunable

class Arm:
    solenoid: wpilib.Solenoid
    arm_up = tunable(False)

    def execute(self):
        self.solenoid.set(self.arm_up)

    def toggle(self):
        '''
        Toggles whether the arm is up or down,
        depending on its current position.
        '''
        self.arm_up =  not self.arm_up

    def toTop(self):
        '''
        Makes the arm go up, no matter what.
        '''
        self.arm_up = True
    
    def toBottom(self):
        '''
        Makes the arm go down, no matter what.
        '''
        self.arm_up = False