import keyboard


def threadKeyboardcheck():
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP:
        #print(event.name)
        print("+1 step")
    
    threadKeyboardcheck()

def checkIfKeyboardUsed(mainWindow) :

    #try:  # used try so that if user pressed other than the given key error will not be shown


    #except:
        #print("e")
    
    mainWindow.after(100, lambda:checkIfKeyboardUsed(mainWindow))