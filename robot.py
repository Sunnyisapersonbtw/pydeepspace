#!/usr/bin/env python3

import magicbot
import wpilib
import ctre

from components.test import Test


class Robot(magicbot.MagicRobot):

    def createObjects(self):
        """Create motors and stuff here."""
        self.Controller = wpilib.Xboxcontroller(0)
        self.Motor = ctre.TalonSRX(1)
        self.Button = wpilib.kA(2)

    def teleopInit(self):
        """Initialise driver control."""

    def teleopPeriodic(self):
        """Allow the drivers to control the robot."""
    def getAButtonPressed(self) -> bool:
        if self.Button == self.getRawButtonPressed(self.Button.kA):
            set self.Motor(10)
        else self.Motor_Output = 0
        

        


if __name__ == "__main__":
    wpilib.run(Robot)
