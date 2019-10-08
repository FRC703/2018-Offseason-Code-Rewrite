import wpilib
import wpilib.drive
import ctre
from magicbot import tunable, will_reset_to
from networktables import NetworkTables


class Drivetrain:
    shifter: wpilib.Solenoid

    train: wpilib.drive.DifferentialDrive
    forward_speed = will_reset_to(0)
    turn_speed = will_reset_to(0)

    kP = tunable(1)
    kI = tunable(0)
    kD = tunable(0)

    drive_multiplier = tunable(.7)
    turn_multiplier = tunable(.5)

    high_gear = tunable(False)

    currentSpeed = tunable(0)
    integral = tunable(0)
    previous_error = tunable(0)

    def execute(self):
        self.shifter.set(self.high_gear)
        self.train.arcadeDrive(self.forward_speed, self.turn_speed)

    def PID(self, targetSpeed):
        '''
        Uses the current speed alongside the target speed to create a smooth ramping
        '''
        error = self.currentSpeed - targetSpeed
        self.integral = self.integral + (error * .02)
        derivative = (error - self.previous_error) / .02
        return self.kP * error + self.kI * self.integral + self.kD * derivative

    def shift_toggle(self):
        self.high_gear = not self.high_gear

    def move(self, speed, turn):
        self.forward_speed = -speed * self.drive_multiplier
        self.turn_speed = turn * self.turn_multiplier

    def movePID(self, speed, turn):
        self.forward_speed = self.PID(speed)
        self.turn_speed = turn