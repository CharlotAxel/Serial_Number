import os, sys
from tkinter import *

root = Tk()
root.title("Serial Number")
root.geometry("800x200")
def getMachineAdrr():
	os_type = sys.platform.lower()
	if 'win' in os_type:
			command = 'wmic bios get serialnumber'
	elif 'linux' in os_type:
			command = 'hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid'
	elif 'darwin' in os_type:
			command = "ioreg -l | grep IOPlatformSerialNumber"
	return os.popen(command).read().replace("\n","").replace("	","").replace(" ","")

label = Label(root, text = 'Your serial number is ' + str(getMachineAdrr())).pack()

root.mainloop()
