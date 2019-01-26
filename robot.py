#!/usr/bin/env python3

import magicbot
import wpilib
from automations.hatch import HatchController
from components.hatch import Hatch


class Robot(magicbot.MagicRobot):

    hatch: Hatch
    hatch_controller: HatchController

    def createObjects(self):
        """Create motors and stuff here."""
        self.top_puncher = wpilib.Solenoid(2)
        self.left_puncher = wpilib.Solenoid(0)
        self.right_puncher = wpilib.Solenoid(3)

        self.gamepad = wpilib.XboxController(2)
        
        self.top_limit_switch = wpilib.DigitalInput(1)
        self.left_limit_switch = wpilib.DigitalInput(2)
        self.right_limit_switch = wpilib.DigitalInput(3)
        # self.compressor = wpilib.Compressor()

    def teleopInit(self):
        """Initialise driver control."""
        pass

    def teleopPeriodic(self):
        """Allow the drivers to control the robot."""
        if self.gamepad.getAButtonPressed():
            self.hatch_controller.start_punch()


if __name__ == "__main__":
    wpilib.run(Robot)
