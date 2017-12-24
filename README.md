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
