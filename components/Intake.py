import ctre
from magicbot import tunable, will_reset_to


class Intake:
    left_motor: ctre.WPI_TalonSRX
    right_motor: ctre.WPI_TalonSRX

    intake_speed = will_reset_to(0)
    kIntakeSpeed = tunable(.7)

    def execute(self):
        self.left_motor.set(self.intake_speed)
        self.right_motor.set(-self.intake_speed)

    def suck(self):
        self.intake_speed = -self.kIntakeSpeed

    def push(self):
        self.intake_speed = self.kIntakeSpeed