from tkinter import Tk
import constants
import threading
from keyboardManagement import threadKeyboardcheck

mainWindow = Tk()
mainWindow.minsize(constants.WIDTH_OF_WIN,constants.HEIGHT_OF_WIN)
mainWindow.title('catBoarding')

threadCheckKeyboard = threading.Thread(target=threadKeyboardcheck)
threadCheckKeyboard.start()


mainWindow.mainloop()
threadCheckKeyboard.join()