import pyautogui, time, sys,tty,termios

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        print(str(k))
        if k=='\x1b[A':
                print("up")
                return 1
        elif k=='\x1b[B':
                print("down")
                return 2
        elif k=='\x1b[C':
                print("right")
                return 3
        elif k=='\x1b[D':
                print("left")
                return 4
        elif k == 'm':
        		print("enter")
        		return 5
       	elif k == 'q':
       			print("quit")
       			return -1
        else:
                print("not an arrow key!")
                return -1

while True:
	currentMouseX, currentMouseY = pyautogui.position()
	keyPressed = get()
	if keyPressed == 1:
		pass
	elif keyPressed == 2:
		pass
	elif keyPressed == 3:
		pass
	elif keyPressed == 4:
		pass
	elif keyPressed == 5:
		pass
	elif keyPressed == -1:
		exit()
	else:
		pass