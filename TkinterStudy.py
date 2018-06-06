from tkinter import *

root = Tk()
btn = Button(root,text="Click me!")
btn.config(command=lambda:print("Hello, Tkinter!"))
#padx padding_x,  pady padding_y
btn.pack(padx=120,pady=30)
root.title("My Tkinter app")
root.mainloop()