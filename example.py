from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.Encoder import *
from Phidget22.Devices.CurrentInput import *
import time
import math
cpr = 12*4*45

def onPositionChange(self, positionChange, timeChange, indexTriggered):
	print("PositionChange: " + str(positionChange))
	print("TimeChange: " + str(timeChange))
	print("IndexTriggered: " + str(indexTriggered))
	print("getPosition: " + str((self.getPosition()%cpr)*2*math.pi))
	print("----------")

def onCurrentChange(self, current):
	print("Current: " + str(current))

def main():
	dcMotor0 = DCMotor()
	encoder0 = Encoder()
	currentInput0 = CurrentInput()

	encoder0.setOnPositionChangeHandler(onPositionChange)
	currentInput0.setOnCurrentChangeHandler(onCurrentChange)

	dcMotor0.openWaitForAttachment(5000)
	encoder0.openWaitForAttachment(5000)
	currentInput0.openWaitForAttachment(5000)

	dcMotor0.setTargetVelocity(.5)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	dcMotor0.close()
	encoder0.close()
	currentInput0.close()

main()