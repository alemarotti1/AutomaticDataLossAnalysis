from tkinter import *
import eel

#create a window using Eel and open "www/index.html"
def startWebView():
    eel.init('www/')
    eel.start('index.html')

# def startGUI():
#     root = Tk()
#     root.title("GUI")
#     root.geometry("1200x800")


#     # create a label
#     label = Label(root, text="Was there a data loss in this image?")
#     label.grid(row=0, column=1)

#     # create a button
#     button = Button(root, text="Yes", command=lambda: print("Yes"))
#     button.grid(row=1, column=0, padx=20, pady=10)

#     button = Button(root, text="Maybe", command=lambda: print("Maybe"))
#     button.grid(row=1, column=1, padx=20, pady=10)

#     button = Button(root, text="No", command=lambda: print("No"))
#     button.grid(row=1, column=2, padx=20, pady=10)

#     root.mainloop()

#     root.mainloop() #this will keep the window open until we close it


