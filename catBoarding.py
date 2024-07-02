from tkinter import Tk
import constants
import threading
from tkinter import Frame
from tkinter import Listbox
from tkinter import Scrollbar
from tkinter import Label
from tkinter import Button
import style
from keyboardManagement import threadKeyboardcheck
from loadAndSaveData import loadData
from PIL import Image
from PIL import ImageTk
from changePage import changePage

mainWindow = Tk()
mainWindow.minsize(constants.WIDTH_OF_WIN,constants.HEIGHT_OF_WIN)
mainWindow.title('catBoarding')

global steps
global coins
steps = int(loadData('stepsData.txt'))
coins = int(loadData('coinsData.txt'))


mainFrame = Frame(mainWindow, width=constants.WIDTH_OF_WIN, height=constants.HEIGHT_OF_WIN, bg=style.COLOR_BG)
mainFrame.pack(side="left")
mainFrame.pack_propagate(False)




chooseSectionFrame = Frame(mainFrame, width=constants.WIDTH_OF_WIN, height=constants.HEIGHT_OF_WIN*0.10, bg=style.COLOR_BG, highlightthickness=3, highlightbackground=style.COLOR_BORDER, highlightcolor=style.COLOR_BORDER)
chooseSectionFrame.pack(side="bottom")
chooseSectionFrame.pack_propagate(False)

characterFrame = Frame(mainFrame, width=constants.WIDTH_OF_WIN, height=constants.HEIGHT_OF_WIN*0.80, bg=style.COLOR_BG, highlightthickness=3, highlightbackground=style.COLOR_BORDER, highlightcolor=style.COLOR_BORDER)
characterFrame.pack(side="bottom")
characterFrame.grid_propagate(False)
characterFrame.pack_propagate(False)

#History frame
historyFrame = Frame(mainFrame, width=constants.WIDTH_OF_WIN, height=constants.HEIGHT_OF_WIN*0.8, bg=style.COLOR_BG, highlightthickness=3,highlightbackground=style.COLOR_BORDER,  highlightcolor=style.COLOR_BORDER)
historyScrollBar = Scrollbar(historyFrame, orient="vertical")
listElemets = Listbox(historyFrame, yscrollcommand=historyScrollBar.set, width=80, height=constants.HEIGHT_OF_WIN)
historyScrollBar.config(command=listElemets.yview)
historyScrollBar.pack(side="right", fill='y')
historyScrollBar.pack_propagate(False)

listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "looooo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.insert("active", "allo")
listElemets.pack(fill="both", expand="yes")


infoFrame = Frame(mainFrame, width=constants.WIDTH_OF_WIN, height=constants.HEIGHT_OF_WIN*0.1, bg=style.COLOR_BG, highlightthickness=3,highlightbackground=style.COLOR_BORDER,  highlightcolor=style.COLOR_BORDER)
infoFrame.pack(side="top")
infoFrame.pack_propagate(False)


textStep = Label(infoFrame, text=f"Steps:{steps}", font=style.FONT, bg=style.COLOR_BG)
textStep.pack(side="left")

textCoin = Label(infoFrame, text=f"Coins:{coins}", font=style.FONT, bg=style.COLOR_BG)
textCoin.pack(side="left")

threadCheckKeyboard = threading.Thread(target=threadKeyboardcheck, args=(steps,textStep,coins, textCoin, 0))
threadCheckKeyboard.start()

imgCharacter = Image.open("images\chips-icon.png")
imgCharacter = imgCharacter.resize((round(constants.HEIGHT_OF_WIN*0.30), round(constants.HEIGHT_OF_WIN*0.30)))
imgCharacter = ImageTk.PhotoImage(imgCharacter)
labelImageCharacter = Label(characterFrame, image=imgCharacter).pack(side="top", pady=constants.HEIGHT_OF_WIN*0.10)



buttonToBackpack = Button(chooseSectionFrame, text="backpack", command=lambda:changePage("backpack", characterFrame, historyFrame))
buttonToBackpack.pack(side="left")

buttonToHistory = Button(chooseSectionFrame, text="history", command=lambda:changePage("history", characterFrame, historyFrame))
buttonToHistory.pack(side="right")






mainWindow.mainloop()
threadCheckKeyboard.join()