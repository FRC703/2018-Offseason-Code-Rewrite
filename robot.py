import wpilib
import magicbot
import ctre
import util

from components.Drivetrain import Drivetrain
from components.Intake import Intake
from components.Arm import Arm

from networktables import NetworkTables


class Robot(magicbot.MagicRobot):
    drivetrain: Drivetrain
    intake: Intake
    arm: Arm
    joystick: wpilib.Joystick

    def createObjects(self):
        NetworkTables.initialize()

        # Create drivetrain motors
        self.lf_motor = ctre.WPI_TalonSRX(util.DRIVE_LEFT_FRONT)
        self.lr_motor = ctre.WPI_TalonSRX(util.DRIVE_LEFT_BACK)
        self.rf_motor = ctre.WPI_TalonSRX(util.DRIVE_RIGHT_FRONT)
        self.rr_motor = ctre.WPI_TalonSRX(util.DRIVE_RIGHT_BACK)

        self.lr_motor.follow(self.lf_motor)
        self.rr_motor.follow(self.rf_motor)

        self.train = wpilib.drive.DifferentialDrive(self.lf_motor,
                                                    self.rf_motor)

        # Create solenoids
        self.shifter = wpilib.Solenoid(util.SOLENOID_SHIFTER)
        self.arm_solenoid = wpilib.Solenoid(util.SOLENOID_LIFT)

        # Create intake motors
        self.intake_left_motor = ctre.WPI_TalonSRX(util.INTAKE_LEFT_MOTOR)
        self.intake_right_motor = ctre.WPI_TalonSRX(util.INTAKE_RIGHT_MOTOR)

        self.joystick = wpilib.Joystick(util.JOYSTICK_PORT)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):

        forward = -self.joystick.getRawAxis(1)
        turn = -self.joystick.getRawAxis(2)

        # Intake
        if self.joystick.getRawButton(util.JOYSTICK_INTAKE_IN_BUTTON):
            self.intake.suck()
        elif self.joystick.getRawButton(util.JOYSTICK_INTAKE_OUT_BUTTON):
            self.intake.push()

        # Shift
        if self.joystick.getRawButtonPressed(
                util.JOYSTICK_SHIFTER_TOGGLE_BUTTON):
            self.drivetrain.shift_toggle()
        # Lift
        if self.joystick.getRawButtonPressed(util.JOYSTICK_LIFT_TOGGLE_BUTTON):
            self.arm.toggle()

        # Drive
        self.drivetrain.move(forward, turn)

    def disabledInit(self):
        self.drivetrain.move(0, 0)


if __name__ == "__main__":
    wpilib.run(Robot)