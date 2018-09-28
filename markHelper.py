import sys, termios, tty, os, time, pyautogui
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.0

deltaX = 1
deltaY = 1
while True:
    char = getch()
    if (char == "p"):
        print("Stop!")
        exit(0)
 
    currentMouseX, currentMouseY = pyautogui.position()
    newPosition = list((currentMouseX, currentMouseY))
    if (char == "a"):
        print("Left pressed")
        newPosition[0] -=  deltaX
        time.sleep(button_delay)
        pyautogui.moveTo(newPosition[0], newPosition[1])
    elif (char == "d"):
        print("Right pressed")
        newPosition[0] += deltaX
        time.sleep(button_delay)
        pyautogui.moveTo(newPosition[0], newPosition[1])
    elif (char == "w"):
        print("Up pressed")
        newPosition[1] -= deltaY
        time.sleep(button_delay)
        pyautogui.moveTo(newPosition[0], newPosition[1])
    elif (char == "s"):
        print("Down pressed")
        newPosition[1] += deltaY
        time.sleep(button_delay)
        pyautogui.moveTo(newPosition[0], newPosition[1])
    elif (char == "1"):
        print("Number 1 pressed")
        time.sleep(button_delay)
    elif (char == "m"):
        print("m pressed")
        time.sleep(button_delay)
        pyautogui.click()
        pyautogui.keyDown('alt')
        pyautogui.typewrite(['tab'])
        pyautogui.keyUp('alt')

    else:
        pass
