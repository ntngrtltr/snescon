# snescon
Snescon will let you use an SNES controller with your PC.
It uses an ESP8266 Arduino-like microcontroller to establish communication between a SNES Controller and a Linux or Windows machine
using the ESPs serial connection. 
A python script running on this machine reads the data and translates it to keyboard or mouse input.

Works with OS: Linux and Windows (as long as python, pynput and pyserial are installed). MacOS was not tested.

Works with microcontroller: ESP8266 (tested), theoratically any other Arduino board with a serial connection.

## Hardware
Connect the wires in the cable of the SNES controller to the according pins on the ESP. 
You can find the controllers pinout in this article (which this project is based on): 
https://www.gamefaqs.com/snes/916396-super-nintendo/faqs/5395 (Point 4)

To find the pins used on the microcontroller, take a look at the sketch.ino file.

_Please note that the colors of the wires can vary in your case!_

## Software

Build and flash the sketch.ino on your device. The official Arduino-IDE should be the easiest way to do so.

On the PC, run snescon.py by running `python snescon.py` in the command line (You have to be in directory where snescon.py is located.). 

_Make sure that `ser = serial.Serial('/dev/ttyUSB0', 115200)` matches the name the Arduino has on your computer!_
(COM-Port on Windows)

To change the key bindings, edit the `keys` array. Reading the pynput documentation can be helpful.

## Background
Snescon was computer science team-project in school.

Turns out that building bridges between old and new technology is a great (and fun) way 
to learn about how devices work and communicate (and to get good grades).
