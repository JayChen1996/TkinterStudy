'''
from tkinter import *

root = Tk()
btn = Button(root,text="Click me!")
btn.config(command=lambda:print("Hello, Tkinter!"))
#padx padding_x,  pady padding_y
btn.pack(padx=120,pady=30)
root.title("My Tkinter app")
root.mainloop()
'''
'''
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(self,text="Click me!",command=self.say_hello)
        self.btn.pack(padx=120,pady=30)
    
    def say_hello(self):
        print("Hello Tkinter")

if __name__=="__main__":
    app=App()
    app.title("My Tkinter app")
    app.mainloop()
'''

import tkinter as tk

RELIEFS = [tk.SUNKEN,tk.RAISED,tk.GROOVE,tk.RIDGE,tk.FLAT]

class ButtonsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.img = tk.PhotoImage(file="python.gif")
        #compound决定图片处于文字的位置
        self.btn = tk.Button(
                       self,
                       text="Button with image",
                       image=self.img,
                       compound=tk.LEFT,
                       command=self.disable_btn)
        self.btns = [self.create_btn(r) for r in RELIEFS]
        self.btn.pack()
        for btn in self.btns:
            btn.pack(padx=10,pady=10,side=tk.LEFT)

    def create_btn(self,relief):
        return tk.Button(self,text=relief,relief=relief)

    def disable_btn(self):
        self.btn.config(state=tk.DISABLED)


if __name__ == '__main__':
    app = ButtonsApp()
    app.mainloop()





















