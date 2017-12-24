# SenseHat_problem
AS level CS project to use the SenseHat to display data.


A small manufacturing company has asked you to design software that will interface with one of its production lines. 
It's new line of painted widgets dry to an optimum glossy finish if kept at a constant temperature for 1 hour.
Standard painted widgets dry best at 21.5c but metallic finishes dry to a deep shine if kept at 22.7c. 
Your prototype program must alert the user if the temperature changes within +/- 0.2 degrees of optimum over a 5 minute period. 
At the end of the production batch, the operator will need to be able to view a range of statistics for the batch so that they can 
adjust ventilation and polishing time accordingly. 
You have been supplied with 'black box' function that will return a list containing the current temperature (as a float) 
from a sensor and the time the reading was taken (a string). You must not alter the black box code. 
You will be implementing the prototype using the SenseHat on a Raspberry Pi  https://www.raspberrypi.org/products/sense-hat/  
If you do not have access to this hardware, use the online emulator at 
https://trinket.io/sense-hat Run the code in the emulator. 

TASKS

1.	Test the above code  outputs values from the function in the SenseHat LEDs

2.	The program should take a reading and compare it to the temperature range for the current paint finish in production. If the temperature has increased, the amount of change should be output in red. If the reading has gone down, the amount of change should be shown in blue. 

3.	Investigate how to trim the temperature when it is displayed to 2 decimal places without reducing the accuracy of the data stored. (hint: there are several Python functions that could help, such as ‘round’ and ‘format’)

4.	The readings should repeat every 5 minutes over a 60 min period (for testing you may reduce this to seconds) and be stored in the list tempReadings(). (hint: you may want to look up the ‘sleep’ function in Python)


5.	At the end of the hour have been taken, sort tempReadings in to ascending temperature order, then output the readings  (hint: there are many methods for sorting a list, try looking up a ‘Bubble Sort’ in Python)

6.	Submit a flowchart for the general program showing any calls to functions but not the contents of the functions

7.	Submit pseudo code for any functions you have created

EXTENSION: Use the SenseHat’s sensors to generate the temperature reading (the emulator will let set the external temperatures and alter at the program is running) 

Useful links:
https://www.tutorialspoint.com/python/time_sleep.htm
https://pythonhosted.org/sense-hat/api/  
https://www.tutorialspoint.com/python/python_strings.htm
