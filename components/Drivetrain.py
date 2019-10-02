import wpilib
import wpilib.drive
import ctre
from magicbot import tunable, will_reset_to

class Drivetrain:
    shifter: wpilib.Solenoid

    train: wpilib.drive.DifferentialDrive
    forward_speed = will_reset_to(0)
    turn_speed = will_reset_to(0)

    kP = tunable(1)
    kI = tunable(0)
    kD = tunable(0)

    currentSpeed = tunable(0)
    integral = tunable(0)
    previous_error = tunable(0)

    def execute(self):
        self.train.arcadeDrive(self.forward_speed, self.turn_speed)
    
    def PID(self, targetSpeed):
        '''
        Uses the current speed alongside the target speed to create a smooth ramping
        '''
        error = self.currentSpeed - targetSpeed
        self.integral = self.integral + (error*.02)
        derivative = (error - self.previous_error) / .02
        return self.kP*error + self.kI*self.integral + self.kD*derivative


    def move(self, speed, turn):
        self.forward_speed = -speed #self.PID(speed)
        self.turn_speed = turn