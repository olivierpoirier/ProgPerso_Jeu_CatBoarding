import keyboard


def threadKeyboardcheck():
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP:
        #print(event.name)
        print("+1 step")
    
    threadKeyboardcheck()

