from sense_hat import SenseHat
#designed for SenseHat emulator https://trinket.io/sense-hat
#ammend library if using hardware sensehat
import time, random
s= SenseHat()#reference to senseHat object is 's'

tempReadings = []# empty list to store readings

def getTemp():
        #Blackbox code - do not alter
	currentReading = []
	currentReading.append(random.triangular(18.0,27.5, 21.59))
	currentReading.append(time.strftime("%H:%M:%S"))
	return currentReading
        #end of Blackbox


tempReadings.append(getTemp())

s.show_message("the temp is"+str(tempReadings[0]))
s.show_message("at"+str(tempReadings[1]))
