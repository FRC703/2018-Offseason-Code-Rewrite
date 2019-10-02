from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

from components.Drivetrain import Drivetrain

class DriveForward(AutonomousStateMachine):
    MODE_NAME = 'Drive Forward'
    DEFAULT = True

    drivetrain: Drivetrain

    @timed_state(duration=3, first=True)
    def drive_forward(self):
        self.drivetrain.move(0.7, 0)
    
    def done(self):
        super().done()
        self.drivetrain.move(0,0)