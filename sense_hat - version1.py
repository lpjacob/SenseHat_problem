from sense_hat import SenseHat
import time, random
#designed for SenseHat emulator https://trinket.io/sense-hat
#ammend library if using hardware sensehat
s= SenseHat()

tempReadings = []
standardPaint = 21.5
metallicPaint = 22.7
variance = 0.2
colorTemp = None #holds the RGB values for the temperature change

def getTemp():
	currentReading = []
	currentReading.append(random.triangular(18.0,27.5, 21.59))
	currentReading.append(time.strftime("%H:%M:%S"))
	return currentReading
	
def compTemp(newTemp, lastTemp):
	"""function to compare the most recent and previous temperatures
	returns a colour value as a tuple of RGB integers """
	red = (255,0,0)
	blue = (0,0,255)
	white = (255,255,255)
	if newTemp > lastTemp:
		return red
	elif newTemp < lastTemp:
		return blue
	else:
		return white

def showMessage(colorTemp, newReading):
"""Shows the message on the LED, accepets the list containing 
[0] the temp and [1] the time plus the colour """
	tempReading = newReading[0]
	tempReading = str(round(tempReading,2))
	s.show_message(tempReading, text_colour = colorTemp)


while True:
	newReading = getTemp()
	newTemp = newReading[0]
	readingLength = len(tempReadings)
	if readingLength > 0:
		lastTemp = tempReadings[readingLength-1][0]
		colorTemp= compTemp(newTemp, lastTemp)
		showMessage(colorTemp, newReading)
	tempReadings.append(newReading)
	time.sleep(2)


