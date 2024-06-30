from tkinter import Tk
import constants
import threading
from tkinter import Frame
from tkinter import Label
import style
from keyboardManagement import threadKeyboardcheck
from loadAndSaveData import loadData

mainWindow = Tk()
mainWindow.minsize(constants.WIDTH_OF_WIN,constants.HEIGHT_OF_WIN)
mainWindow.title('catBoarding')

global steps
global coins
steps = int(loadData('stepsData.txt'))
coins = int(loadData('coinsData.txt'))


mainFrame = Frame(mainWindow, width=constants.WIDTH_OF_WIN, height=constants.HEIGHT_OF_WIN, bg=style.COLOR_BG)
mainFrame.pack(side="left")

menuFrame = Frame(mainFrame, width=constants.WIDTH_OF_WIN, height=constants.HEIGHT_OF_WIN, bg=style.COLOR_BG)
menuFrame.pack(side="left")

textStep = Label(menuFrame, text=f"Steps:{steps}", font=style.FONT, bg=style.COLOR_BG)
textStep.grid(column=0, row=0)

textCoin = Label(menuFrame, text=f"Coins:{coins}", font=style.FONT, bg=style.COLOR_BG)
textCoin.grid(column=1, row=0)

threadCheckKeyboard = threading.Thread(target=threadKeyboardcheck, args=(steps,textStep,coins, textCoin, 0))
threadCheckKeyboard.start()








mainWindow.mainloop()
threadCheckKeyboard.join()