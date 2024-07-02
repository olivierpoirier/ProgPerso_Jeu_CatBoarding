def changePage(wantedPage, characterFrame, historyFrame):
    if(wantedPage == "backpack"):
        characterFrame.grid_forget()
        characterFrame.pack_forget()

    if(wantedPage == "history"):
        characterFrame.grid_forget()
        characterFrame.pack_forget()
        historyFrame.pack(side="bottom")