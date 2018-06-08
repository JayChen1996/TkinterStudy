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

'''
#按钮
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
'''


'''
#登录界面
import tkinter as tk

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #Entry 输入框
        self.username = tk.Entry(self)
        self.password = tk.Entry(self,show="*")
        self.login_btn = tk.Button(self,text='Login',command=self.print_login)
        self.clear_btn = tk.Button(self,text="Clear",command=self.clear_form)
        #pack 打包，塞进
        self.username.pack()
        self.password.pack()
        self.login_btn.pack(fill=tk.BOTH)
        self.clear_btn.pack(fill=tk.BOTH)

    def print_login(self):
        self.username.insert(tk.INSERT,"enhd")
        print("Username:{}".format(self.username.get()))
        print("Password:{}".format(self.password.get()))

    def clear_form(self):
        self.username.delete(0,tk.END)
        self.password.delete(0,tk.END)
        self.username.focus_set()

if __name__ == '__main__':
    app = LoginApp()
    app.mainloop()
'''

'''
#变量变化跟踪
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        # "w",当变量被写入
        # "r",当变量被读取
        # "u",当变量被删除  
        # 时调用show_message()函数
        self.var.trace("w",self.show_message)
        self.entry = tk.Entry(self,textvariable=self.var)
        self.btn = tk.Button(self,text="Clear",command=lambda:self.var.set(""))
        self.label = tk.Label(self)
        self.entry.pack()
        self.btn.pack()
        self.label.pack()

    def show_message(self,*args):
        value = self.var.get()
        # python的三目运算: true_part if condition else false_part
        # {},python的格式化字符串方法
        text = "Hello,{}".format(value) if value else ""
        # 改变label的方法
        self.label.config(text=text)

if __name__ == '__main__':
    app = App()
    app.mainloop()
'''

'''
#用正则表达式验证输入的正确性
import re
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #为了提高效率，把正则表达式编译成一个正则表达式对象
        self.pattern = re.compile("^\w{0,10}$")
        self.label = tk.Label(self,text="Enter your username")
        #一个python元组, 第一个元素是函数，第二、三个元素是函数参数,Entry会自动传递给函数
        vcmd = (self.register(self.validate_username),"%i","%P")
        #设置验证命令为vcmd,及不合法命令为print_error
        self.entry = tk.Entry(self,
                              validate="key",
                              validatecommand=vcmd,
                              invalidcommand=self.print_error)
        self.label.pack()
        self.entry.pack(anchor=tk.W,padx=10,pady=10)
    
    def validate_username(self,index,username):
        print("Modification at index "+index)
        return self.pattern.match(username) is not None

    def print_error(self):
        print("Invalid username character")


if __name__ == "__main__":
    app=App()
    app.mainloop()
'''

'''
#Spinbox和Scale的用法
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.spinbox = tk.Spinbox(self,from_=0,to=5)
        self.scale = tk.Scale(self,from_=0,to=5,
                              orient=tk.HORIZONTAL,
                              resolution=0.1)
        self.btn = tk.Button(self,text="Print values",command=self.print_values)
        self.spinbox.pack()
        self.scale.pack()
        self.btn.pack()

    def print_values(self):
        print("SpinBox:{}".format(self.spinbox.get()))
        print("Scale:{}".format(self.scale.get()))

if __name__ == "__main__":
    app = App()
    app.mainloop()
'''


import tkinter as tk

COLORS = [("Red","red"),("Green","green"),("Blue","blue")]

class ChoiceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.set("red")
        #list comprehension递推式构造列表
        self.buttons = [self.create_radio(c) for c in COLORS]
        for button in self.buttons:
            #anchor=tk.W 左对齐
            button.pack(anchor=tk.W,padx=10,pady=5)
        self.r = tk.Radiobutton(self,
                                text="test",
                                value="testvalue",
                                command=self.print_option,
                                variable=self.var)
        self.r.pack()

    def create_radio(self,option):
        text,value = option
        #Radiobutton的variable选项标志着一组互斥的单选框,variable相同就是互斥的单选框
        return tk.Radiobutton(self,text=text,value=value,
                              command=self.print_option,
                              variable=self.var)

    def print_option(self):
        print(self.var.get())

if __name__ == "__main__":
    app = ChoiceApp()
    app.mainloop()













