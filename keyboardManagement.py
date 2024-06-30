import keyboard
from loadAndSaveData import saveData
from random import randint

def threadKeyboardcheck(steps, textStep, coins, textCoin, succesiveSteps):
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP:
        #print(event.name)
        steps +=1
        succesiveSteps +=1
        print("+1 step")
        print(steps)
        textStep["text"] = f"Steps:{steps}"
        if(succesiveSteps % 10 == 0) :
            if(randint(0,1) == 1):
                coins += 1
                textCoin["text"] = f"Coins:{coins}"
                print("+1 coin")
                print(coins)
                saveData(coins, 'coinsData.txt')
        
        saveData(steps, 'stepsData.txt')

        
    
    threadKeyboardcheck(steps, textStep, coins, textCoin, succesiveSteps)

