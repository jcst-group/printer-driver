import tkinter as tk
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.upframe = tk.Frame(self)
        self.midFrame = tk.Frame(self)
        self.upframe.pack(padx=10, pady=20, side="top")
        self.midFrame.pack(padx=10, pady=20, side="top")
        self.createUpFrame()

        #刷出包装净重
        self.midLeftFrame = tk.Frame(self.midFrame)
        self.midLeftFrame.pack(padx=10, side="left")

        self.midTextLabel = tk.Label(self.midLeftFrame, text="包装净重")
        self.midTextLabel.pack(side="left")

        self.cb = ttk.Combobox(self.midLeftFrame,width=20)
        self.cb['values'] = ('Python', 'Swift', 'Kotlin')
        self.cb.pack(padx=10, side="left")

        #刷出追溯码选择
        self.midMidLeftFrame = tk.Frame(self.midFrame)
        self.midMidLeftFrame.pack(padx=10, side="left")
        self.midSuyuanTextLabel = tk.Label(self.midMidLeftFrame, text="包装净重")
        self.midSuyuanTextLabel.pack(side="left")



        #右边内容刷新
        self.midRightFrame = tk.Frame(self.midFrame)
        self.midRightFrame.pack(padx=10, side="right")
        self.createMidRightFrame()



    def createUpFrame(self):
        self.upTextLabel = ttk.Label(self.upframe, text="初加工/采收批次")
        self.upTextLabel.pack(side="left")

        self.upEntry = ttk.Entry(self.upframe, width=30)  # show="*" 可以表示输入密码
        self.upEntry.pack(padx=10, side="left")

        self.queryButton = ttk.Button(self.upframe, text="查询")
        self.queryButton["command"] = self.say_hi
        # self.queryButton['bg'] = "blue"
        # button1.bind("<Button-1>", self.say_hi)
        self.queryButton.pack(padx=10, side="left", expand="yes")

    def createMidRightFrame(self):
        self.printWaterButton = ttk.Button(self.midRightFrame, text="打印水洗布")
        self.printWaterButton["command"] = self.say_hi
        self.printWaterButton.pack(side="top", ipady=5, fill="x")

        self.printStickButton = ttk.Button(self.midRightFrame, text="打印不干胶")
        self.printStickButton["command"] = self.say_hi
        self.printStickButton.pack(side="top", ipady=5, fill="x")


    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()  # 生成主窗口
root.title("窗体测试程序")   # 窗体名称
root.geometry("500x600")   # 指定窗体大小
root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()





