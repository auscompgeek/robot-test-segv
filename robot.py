#!/usr/bin/env python3

import rev
import wpilib


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        self.motor = rev.CANSparkMax(1, rev.CANSparkMax.MotorType.kBrushless)

    def autonomousInit(self) -> None:
        raise Exception("lol")


if __name__ == "__main__":
    wpilib.run(Robot)
