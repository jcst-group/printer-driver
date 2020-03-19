import tkinter as tk
from tkinter import ttk
from GrepData import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.frame_right_top = ttk.Frame(width=600, height=170)
        self.frame_center = ttk.Frame(width=600, height=400)

        #加工批次
        self.upTextLabel = ttk.Label(self.frame_right_top, text="初加工/采收批次")
        self.upTextLabel.grid(row=1, column=0,pady=10,sticky="e")
        self.queryCode = tk.StringVar()
        self.upEntry = ttk.Entry(self.frame_right_top, textvariable=self.queryCode, width=30)  # show="*" 可以表示输入密码
        self.upEntry.grid(row=1, column=1, padx=10, sticky="w")

        self.queryButton = ttk.Button(self.frame_right_top, command=self.query_data, text="查询")
        self.queryButton.grid(row=1, column=2)


        #包装净重
        self.packageText = ttk.Label(self.frame_right_top, text="包装净重")
        self.packageText.grid(row=2, column=0, pady=10, sticky="e")

        self.cb = ttk.Combobox(self.frame_right_top, width=20)
        #self.cb['values'] = ('Python', 'Swift', 'Kotlin')
        self.cb.grid(row=2, column=1, padx=10,sticky="w")

        # 追溯码
        self.sourceText = ttk.Label(self.frame_right_top, text="追溯码")
        self.sourceText.grid(row=3, column=0, pady=10, sticky="e")

        RadioButtonFrame = ttk.Frame(self.frame_right_top,width=20)
        RadioButtonFrame.grid(row=3, column=1, pady=10, sticky="w")
        self.intVar = tk.IntVar()
        books = ('全选', '取消全选')
        i = 1
        for book in books:
            ttk.Radiobutton(RadioButtonFrame,
                            text=book,
                            variable=self.intVar,  # 将Radiobutton绑定到self.intVar变量
                            command=self.change,  # 将选中事件绑定到self.change方法
                            value=i).pack(side="left", fill="y", padx=5, anchor="w")
            i += 1

        #创建打印按钮
        self.printText = ttk.Label(self.frame_right_top, text="打印选择")
        self.printText.grid(row=4, column=0, pady=10, sticky="e")
        self.PrintFrame = ttk.Frame(self.frame_right_top, width=20)
        self.PrintFrame.grid(row=4, column=1, pady=10, columnspan=2, sticky="w")

        self.printWater = ttk.Button(self.PrintFrame, text="打印水洗布")
        self.printWater.pack(side="left", padx=5, anchor="w")
        self.printThick = ttk.Button(self.PrintFrame, text="打印不干胶")
        self.printThick.pack(side="left", padx=5, anchor="w")



        #创建多选列表
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=15)
        self.vbar = ttk.Scrollbar(self.frame_center, orient="vertical",command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        #tree_date = ttk.Treeview(self,height=10)
        self.tree['columns'] = ['name', 'age', 'weight', 'number']
        self.tree.grid(row=4, column=0, columnspan=2, sticky="e")
        # 设置列宽度
        self.tree.column('name', width=100)
        self.tree.column('age', width=100)
        self.tree.column('weight', width=100)
        self.tree.column('number', width=300)

        # 添加列名
        self.tree.heading('name', text='姓名')
        self.tree.heading('age', text='年龄')
        self.tree.heading('weight', text='体重')
        self.tree.heading('number', text='工号')

        # 给表格中添加数据
        #self.tree.insert('', "end", values=('大豆', 21, '60kg', '3121211034'))
        self.tree.insert('', 1, values=('花生', 21, '54kg', '3121211033'))
        self.tree.insert('', 2,  values=('玉米', 21, '65kg', '3121211023'))
        self.tree.insert('', 3,  values=('土豆', 21, '34kg', '3121211053'))
        self.tree.insert('', 4,  values=('番茄', 21, '65kg', '3121211063'))
        self.tree.insert('', 6,  values=('高粱', 21, '64kg', '3121211073'))
        # self.tree.insert('', 7, values=('大豆', 21, '60kg', '3121211034'))
        # self.tree.insert('', 8, values=('花生', 21, '54kg', '3121211033'))
        # self.tree.insert('', 9, values=('玉米', 21, '65kg', '3121211023'))
        # self.tree.insert('', 10, values=('土豆', 21, '34kg', '3121211053'))
        # self.tree.insert('', 11, values=('番茄', 21, '65kg', '3121211063'))
        # self.tree.insert('', 12, values=('高粱', 21, '64kg', '3121211073'))
        # self.tree.insert('', 13, values=('大豆', 21, '60kg', '3121211034'))
        # self.tree.insert('', 14, values=('花生', 21, '54kg', '3121211033'))
        # self.tree.insert('', 15, values=('玉米', 21, '65kg', '3121211023'))
        # self.tree.insert('', 16, values=('土豆', 21, '34kg', '3121211053'))
        # self.tree.insert('', 17, values=('番茄', 21, '65kg', '3121211063'))
        # self.tree.insert('', 18, values=('高粱', 21, '64kg', '3121211073'))
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.vbar.grid(row=0, column=1, sticky="nse")
        self.tree.bind('<<TreeviewSelect>>', self.select_item)


        self.frame_right_top.grid(row=0, column=0, padx=30, pady=10)
        self.frame_center.grid(row=1, column=0, padx=4)

        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)

    def select_item(self, xx):
        #item = self.tree.selection()[0]
        iids = self.tree.selection()
        print(iids)
        #iids = list(iids)
        print(iids)
        # if item in iids:
        #     print("contain item")
        #     iids.remove(item)
        # else:
        #     print("no contain item")
        #     iids.append(item)
        #iids = tuple(iids)
        self.tree.selection_toggle(iids)

        # print(iids)
        # print(self.tree.item(item))
        # focus = self.tree.focus()
        # for i in iids:
        #     print(i)
        # print(item)
        # print(xx)
        # print(focus)

    def change(self):
        from tkinter import messagebox
        radioVal = self.intVar.get()
        if(radioVal == 1):
            print("if")
            #self.tree.item(item, tags='select')
            messagebox.showinfo(title=None, message=self.intVar.get())
        else:
            print("else")
            messagebox.showinfo(title=None, message=self.intVar.get())


    def query_data(self):
        from tkinter import messagebox
        queryCode = self.queryCode.get()
        queryCode = queryCode.strip()
        print(queryCode)
        gd = GrepData()
        if queryCode == None or queryCode =="":
            messagebox.showinfo(title=None, message="请输入批次编号")
        else:
            try:
                listData = gd.query_data(queryCode)
            except:
                messagebox.showinfo(title=None, message="网络出错,请重试")
                print("网络出错,请重试")
            else:
                self.filterData(listData)



    def filterData(self,listData):
        print(listData)
        cbvalue = self.cb.get()
        print("self.cb.get:".cbvalue)
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        weightDict = {}
        for i in range(0, len(listData)):
            item = listData[i]
            # print(item)
            weight = item["weight"]
            xx = weight in weightDict
            if xx == False:
                weightDict[weight] = i
            self.tree.insert('', i, values=(item["herbsName"], item["specis"], item["weight"], item["traceGroupId"]))
        print(self.cb['value'])
        print(weightDict)
        print("xx")
        self.cb['values'] = tuple(weightDict.keys())
        self.cb.bind("<<ComboboxSelected>>", self.filterData)

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()  # 生成主窗口
root.title("窗体测试程序")   # 窗体名称
root.geometry("700x570")   # 指定窗体大小
root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()





