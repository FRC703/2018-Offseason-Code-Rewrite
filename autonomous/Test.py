from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

from components.Drivetrain import Drivetrain
from components.Arm import Arm
from components.Intake import Intake


class DriveForward(AutonomousStateMachine):
    MODE_NAME = 'Test Auton'
    DEFAULT = False

    drivetrain: Drivetrain
    arm: Arm
    intake: Intake

    @timed_state(duration=1, first=True, next_state="arm_up")
    def drive_forward(self):
        self.drivetrain.movePID(0.7, 0)

    @timed_state(duration=2, next_state="drop")
    def arm_up(self):
        self.arm.toTop()

    @timed_state(duration=1.5)
    def drop(self):
        self.intake.push()

    def done(self):
        super().done()
        self.drivetrain.movePID(0, 0)
