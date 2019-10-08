# ![703](docs/703.png) 2018 Offseason Bot



This is a rewrite of the codebase for the 2018 robot. It's using python with robotpy, running the magicbot framework. Most of this is just for testing purposes, but should be a fully working program that can be used in an official event.

### How to run the code

1. Install robotpy on the roborio

Navigate to the robotpy `installer.py` file, downloaded from [https://github.com/robotpy/robotpy-wpilib/releases](https://github.com/robotpy/robotpy-wpilib/releases)

```
py -3 installer.py install-robotpy
```

2. Deploy the code to the robot

In the robot code directory, run

```
py -3 robot.py deploy
```