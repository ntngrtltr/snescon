import serial
from pynput.keyboard import Key, Controller
import pynput

keyboard = Controller()
mouse = pynput.mouse.Controller()

keys = [
    pynput.keyboard.KeyCode.from_char('z'), # B
    pynput.keyboard.KeyCode.from_char('a'), # Y
    Key.shift_r,                            # SELECT
    Key.enter,                              # START
    Key.up,                                 # UP
    Key.down,                               # DOWN
    Key.left,                               # LEFT
    Key.right,                              # RIGHT
    pynput.keyboard.KeyCode.from_char('x'), # A
    pynput.keyboard.KeyCode.from_char('s'), # X
    pynput.keyboard.KeyCode.from_char('d'), # LS
    pynput.keyboard.KeyCode.from_char('c'), # RS4
]
ser = serial.Serial('/dev/ttyUSB0', 115200)

mouseMode = True

buttonState = 0
oldButtonState = 0
while 1:
    ser.write(1) # write something to grab the data

    oldButtonState = buttonState
    buttonState = int.from_bytes(ser.read(2), byteorder='big')

    print(bin(buttonState))

    for i in range(0, 12):
        down = ((buttonState & pow(2, i)) == 0)
        wasDown = ((oldButtonState & pow(2, i)) == 0)
        if not mouseMode:
            if down and not wasDown:
                print(keys[i])
                keyboard.press(keys[i])
            if not down and wasDown:
                keyboard.release(keys[i])
        elif down:
            x = 0
            y = 0
           
            # move mouse
            if i == 4:
                y -= 1
            if i == 5:
                y += 1
            if i == 6:
                x -= 1
            if i == 7:
                x += 1

            mouse.move(x,y)

            #click
            if i == 8:
                mouse.press(pynput.mouse.Button.left)
        elif wasDown:
            mouse.release(pynput.mouse.Button.left)

ser.close()
