import ctre
from magicbot import tunable, will_reset_to

class Intake:
    left_motor: ctre.WPI_TalonSRX
    right_motor: ctre.WPI_TalonSRX

    intake_speed = will_reset_to(0)

    def execute(self):
        pass