from tkinter import Tk
import constants
import threading
from tkinter import Frame
from tkinter import Label
import style
from keyboardManagement import threadKeyboardcheck
from loadAndSaveData import loadData
from PIL import Image
from PIL import ImageTk

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
menuFrame.grid(column=0,row=0)


chooseSectionFrame = infoFrame = Frame(menuFrame, width=constants.WIDTH_OF_WIN, height=constants.HEIGHT_OF_WIN*0.20, bg=style.COLOR_BG, highlightthickness=3, highlightbackground=style.COLOR_BORDER, highlightcolor=style.COLOR_BORDER)
chooseSectionFrame.pack(side="bottom")

characterFrame = Frame(menuFrame, width=constants.WIDTH_OF_WIN, height=constants.HEIGHT_OF_WIN*0.60, bg=style.COLOR_BG, highlightthickness=3, highlightbackground=style.COLOR_BORDER, highlightcolor=style.COLOR_BORDER)
characterFrame.pack(side="bottom")
characterFrame.grid_propagate(False)
characterFrame.pack_propagate(False)


infoFrame = Frame(menuFrame, width=constants.WIDTH_OF_WIN, height=constants.HEIGHT_OF_WIN*0.20, bg=style.COLOR_BG, highlightthickness=3,highlightbackground=style.COLOR_BORDER,  highlightcolor=style.COLOR_BORDER)
infoFrame.pack(side="top")


textStep = Label(infoFrame, text=f"Steps:{steps}", font=style.FONT, bg=style.COLOR_BG)
textStep.pack(side="left")

textCoin = Label(infoFrame, text=f"Coins:{coins}", font=style.FONT, bg=style.COLOR_BG)
textCoin.pack(side="top")

threadCheckKeyboard = threading.Thread(target=threadKeyboardcheck, args=(steps,textStep,coins, textCoin, 0))
threadCheckKeyboard.start()

imgCharacter = Image.open("images\chips-icon.png")
imgCharacter = imgCharacter.resize((round(constants.HEIGHT_OF_WIN*0.30), round(constants.HEIGHT_OF_WIN*0.30)))
imgCharacter = ImageTk.PhotoImage(imgCharacter)
labelImageCharacter = Label(characterFrame, image=imgCharacter).pack(side="top", pady=constants.HEIGHT_OF_WIN*0.10)








mainWindow.mainloop()
threadCheckKeyboard.join()