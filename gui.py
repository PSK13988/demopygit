from tkinter import *

root = Tk()
root.title("Testing")
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button1.pack(side=LEFT, fill=X)
button2 = Button(bottomFrame, text="Button 2", fg="blue")
button2.pack(side=LEFT, fill=Y)

root.mainloop()
