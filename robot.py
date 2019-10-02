import wpilib
import magicbot
import ctre
import util

from components.Drivetrain import Drivetrain
from components.Intake import Intake
from components.Arm import Arm

class Robot(magicbot.MagicRobot):
    drivetrain: Drivetrain
    intake: Intake
    arm: Arm

    def createObjects(self):
        # Create drivetrain motors
        self.lf_motor = ctre.WPI_TalonSRX(util.DRIVE_LEFT_FRONT)
        self.lr_motor = ctre.WPI_TalonSRX(util.DRIVE_LEFT_BACK)
        self.rf_motor = ctre.WPI_TalonSRX(util.DRIVE_RIGHT_FRONT)
        self.rr_motor = ctre.WPI_TalonSRX(util.DRIVE_RIGHT_BACK)

        self.lr_motor.follow(self.lf_motor)
        self.rr_motor.follow(self.rf_motor)

        self.train = wpilib.drive.DifferentialDrive(self.lf_motor, self.rf_motor)

        # Create solenoids
        self.shifter = wpilib.Solenoid(util.SOLENOID_SHIFTER)
        self.arm_solenoid = wpilib.Solenoid(util.SOLENOID_LIFT)

        # Create intake motors
        self.intake_left_motor = ctre.WPI_TalonSRX(util.INTAKE_LEFT_MOTOR)
        self.intake_right_motor = ctre.WPI_TalonSRX(util.INTAKE_RIGHT_MOTOR)


    
    def teleopInit(self):
        pass
    
    def teleopPeriodic(self):
        pass
    
    def disabledInit(self):
        self.drivetrain.move(0,0)


if __name__ == "__main__":
    wpilib.run(Robot)