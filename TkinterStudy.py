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

'''
#单选按钮
# variable参数制定一组互斥的单选按钮
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
'''


'''
#复选框的用法
#复选框的值可以为数字或字符串，字符串可以用onvalue和offvalue参数指定
import tkinter as tk

class SwitchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.IntVar()
        self.var.set(1)
        self.strVar = tk.StringVar()
        self.strVar.set('off')
        self.cb = tk.Checkbutton(self,text="Active?",
                                  variable=self.strVar,
                                  command=self.print_value)
        self.cb.pack()
        
    def print_value(self):
        print(self.var.get())

if __name__ == "__main__":
    app = SwitchApp()
    app.mainloop()
'''

'''
#Listbox和pack()布局
#pack()布局中的side选项要参考上一个pack()的控件

import tkinter as tk

DAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
MODES = [tk.SINGLE,tk.BROWSE,tk.MULTIPLE,tk.EXTENDED]

class ListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #tk.Frame,部件
        self.frame = tk.Frame(self)
        #tk.Scrollbar 滚动条
        self.scroll = tk.Scrollbar(self.frame,orient=tk.VERTICAL)
        self.list = tk.Listbox(self.frame,yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.list.yview)
        self.frame.pack()
        #列表前面加星号，表示解包，将元素拆成一个一个的参数传入insert,可以用print(*DAY)查看
        self.list.insert(0,*DAYS)
        self.print_btn = tk.Button(self,
                                   text="Print selection",
                                   command=self.print_selection)
        #按钮列表
        self.btns = [self.create_btn(m) for m in MODES]
        #side 设置在frame中的对齐位置
        self.list.pack(side=tk.LEFT)
        #fill，值与side相关,side为Left或right，取Y，side为top或bottom，取X
        self.scroll.pack(side=tk.LEFT,fill=tk.Y)
        self.print_btn.pack(fill=tk.BOTH)
        for btn in self.btns:
            btn.pack(side=tk.LEFT,fill=tk.BOTH)

    def create_btn(self,mode):
        #config设置ListBox的键盘控制
        cmd = lambda:self.list.config(selectmode=mode)
        return tk.Button(self,command=cmd,text=mode.capitalize())

    def print_selection(self):
        #返回选中的项的索引
        selection = self.list.curselection()
        print([self.list.get(i) for i in selection])


if __name__ == "__main__":
    app = ListApp()
    app.mainloop()
'''


'''
#各种事件和控件的绑定
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        frame = tk.Frame(self,bg="green",
                         height=100,width=100)
        #bind绑定事件类型与函数,bind的第一个函数使用<modifier-type-detail>
        # type字段最重要,modifier和detail添加了一些信息
        #鼠标左键按下
        frame.bind("<Button-1>",self.print_event)
        #add参数的值决定了事件之前绑定的函数是被替换还是保留
        frame.bind("<Button-1>",self.print_type_entry,add='+')
        #双击鼠标左键
        frame.bind("<Double-Button-1>",self.print_event)
        #鼠标释放事件
        frame.bind("<ButtonRelease-1>",self.print_event)
        #鼠标按下且移动
        frame.bind("<B1-Motion>",self.print_event)
        #光标进入和离开frame部件的事件
        frame.bind("<Enter>",self.print_event)
        frame.bind("<Leave>",self.print_event)
        frame.pack(padx=50,pady=50)

        entry = tk.Entry(self)
        #获取焦点事件
        entry.bind("<FocusIn>",self.print_type_entry)
        #按键事件
        entry.bind("<Key>",self.print_key)
        entry.pack(padx=20,pady=20)

    def print_event(self,event):
        position="(x={},y={})".format(event.x,event.y)
        print(event.type,"event",position)

    def print_type_entry(self,event):
        print(event.type)

    def print_key(self,event):
        #构造元组的一种方式
        args=event.keysym,event.keycode,event.char
        print("Symbol:{},Code:{},Char:{}".format(*args))


if __name__=="__main__":
    app = App()
    app.mainloop()
'''

'''
#tkinter设置图标函数iconbitmap出错
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Tkinter App")
        self.iconbitmap('icons/python.ico')
        self.geometry("400x200+10+10")


if __name__ == "__main__":
    app = App()
    app.mainloop()
'''

'''
#Listbox和Scrollbar和Frame控件
import tkinter as tk

#继承Frame的子类
class ListFrame(tk.Frame):
    def __init__(self,master,items=[]):
        super().__init__(master)
        #Listbox控件
        self.list = tk.Listbox(self)
        #Scrollbar控件,注意滚动条控件和其他控件的结合,设置控件的属性
        self.scroll = tk.Scrollbar(self,orient=tk.VERTICAL,
                                    command=self.list.yview)
        #Scrollbar控件和Listbox控件结合
        self.list.config(yscrollcommand=self.scroll.set)
        self.list.insert(0,*items)
        #都是在Frame下的布局,所以都放左
        self.list.pack(side=tk.LEFT)
        self.scroll.pack(side=tk.LEFT,fill=tk.Y)


    def pop_selection(self):
        index = self.list.curselection()
        if index:
            value = self.list.get(index)
            self.list.delete(index)
            return value

    def insert_item(self,item):
        self.list.insert(tk.END,item)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        self.frame_a = ListFrame(self,months)
        self.frame_b = ListFrame(self)
        self.btn_right = tk.Button(self,text=">",command=self.move_right)
        self.btn_left = tk.Button(self,text="<",command=self.move_left)
        self.frame_a.pack(side=tk.LEFT,padx=10,pady=10)
        self.frame_b.pack(side=tk.RIGHT,padx=10,pady=10)
        self.btn_right.pack(expand=True,ipadx=5)
        self.btn_left.pack(expand=True,ipadx=5)

    def move_right(self):
        self.move(self.frame_a,self.frame_b)
    
    def move_left(self):
        self.move(self.frame_b,self.frame_a)

    def move(self,frame_from,frame_to):
        value=frame_from.pop_selection()
        if value:
            frame_to.insert_item(value)

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
'''

'''
#pack()布局的学习
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        label_a = tk.Label(self,text="Label A",bg="yellow")
        label_b = tk.Label(self,text="Label B",bg="orange")
        frame = tk.Frame(self)
        label_c = tk.Label(frame,text="Label C",bg="red")
        label_d = tk.Label(frame,text="Label D",bg="green")
        label_e = tk.Label(self,text="Label E",bg="blue")

        opts = {'ipadx':10,'ipady':10,'fill':tk.BOTH}

        label_a.pack(side=tk.TOP,**opts)
        label_b.pack(side=tk.TOP,**opts)
        label_c.pack(side=tk.LEFT,**opts)
        label_d.pack(side=tk.LEFT,**opts)
        frame.pack(side=tk.TOP,ipadx=0)
        label_e.pack(side=tk.TOP,**opts)


if __name__=="__main__":
    app = App()
    app.mainloop()
        
'''


'''
#grid布局

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        label_a = tk.Label(self,text="Label A",bg="yellow")
        label_b = tk.Label(self,text="Label B",bg="orange")
        label_c = tk.Label(self,text="Label C",bg="red")
        label_d = tk.Label(self,text="Label D",bg="green")
        label_e = tk.Label(self,text="Label E",bg="blue")

        #sticky选项表明widget的边界,没有sticky这个参数传入，那么控件就待在中间,nwse表示北西南东
        opts = {'ipadx':10,'ipady':10}#'sticky':'nwse'}
        #grid()函数设置位置
        label_a.grid(row=0,column=0,**opts)
        label_b.grid(row=1,column=0,**opts)
        label_c.grid(row=0,column=1,rowspan=2,**opts)
        label_d.grid(row=0,column=2,rowspan=2,**opts)
        label_e.grid(row=2,column=0,columnspan=3,**opts)


if __name__ == "__main__":
    app = App()
    app.mainloop()

'''

'''
#使用Place布局管理器

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        label_a = tk.Label(self,text="Label A",bg="yellow")
        label_b = tk.Label(self,text="Label B",bg="orange")
        label_c = tk.Label(self,text="Label C",bg="red")
        label_d = tk.Label(self,text="Label D",bg="green")
        label_e = tk.Label(self,text="Label E",bg="blue")

        #relwidth relheight决定控件大小
        #x,y决定控件绝对位置
        #anchor决定控件对齐方式
        #width,
        label_a.place(relwidth=0.25,relheight=0.25)
        #x=100和anchor=tk.N固定了左上角的位置,width和height决定了大小
        label_b.place(x=100,anchor=tk.CENTER,width=100,height=50)
        #tk.CENTER决定了位置
        label_c.place(relx=0.5,rely=0.5,anchor=tk.N,
                      relwidth=0.5,relheight=0.5)
        label_d.place(in_=label_c,anchor=tk.N+tk.W,
                      x=2,y=2,relx=0.5,rely=0.5,
                      relwidth=0.5,relheight=0.5)
        label_e.place(x=200,y=200,anchor=tk.S+tk.E,
                      relwidth=0.25,relheight=0.25)

if __name__ == "__main__":
    app = App()
    app.mainloop()
'''

'''
#LabelFrame的使用示例,grid和pack布局的结合示例
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        group_1 = tk.LabelFrame(self,padx=15,pady=10,text="Personal Information")
        group_1.pack(padx=10,pady=5)
        tk.Label(group_1,text="First name").grid(row=0)
        tk.Label(group_1,text="Last name").grid(row=1)
        tk.Entry(group_1).grid(row=0,column=1,sticky=tk.W)
        tk.Entry(group_1).grid(row=1,column=1,sticky=tk.W)

        group_2 = tk.LabelFrame(self,padx=15,pady=10,text="Address")
        group_2.pack(padx=10,pady=5)

        tk.Label(group_2,text="Street").grid(row=0)
        tk.Label(group_2,text="City").grid(row=1)
        tk.Label(group_2,text="ZIP Code").grid(row=2)

        tk.Entry(group_2).grid(row=0,column=1,sticky=tk.W)
        tk.Entry(group_2).grid(row=1,column=1,sticky=tk.W)
        tk.Entry(group_2).grid(row=2,column=1,sticky=tk.W)

        self.btn_submit = tk.Button(self,text="Submit")
        self.btn_submit.pack(padx=10,pady=10,side=tk.RIGHT)


if __name__ == "__main__":
    app = App()
    app.mainloop()
'''
        
'''
#zip函数
#enumerate函数
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        fields = ["First name","Last name","Phone","Email"]
        labels = [tk.Label(self,text=f) for f in fields]
        #下划线表示上一条语句的执行结果
        entries = [tk.Entry(self) for _ in fields]
        #zip函数 
        self.widgets = list(zip(labels,entries))
        self.submit = tk.Button(self,text="Print info",command=self.print_info)

        #enumerate 意为枚举,即遍历索引和元素
        for i,(label,entry) in enumerate(self.widgets):
            label.grid(row=i,column=0,padx=10,sticky=tk.W)
            entry.grid(row=i,column=1,padx=10,pady=5)

        self.submit.grid(row=len(fields),column=1,sticky=tk.E,padx=10,pady=10)

    
    def print_info(self):
        for label,entry in self.widgets:
            print("{}={}".format(label.cget("text"),entry.get()))


if __name__ == "__main__":
    app=App()
    app.mainloop()
'''








