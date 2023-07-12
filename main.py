import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MainWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title = "Tkinter Example"
        self.window.geometry("400x300")
        self.tabControl = ttk.Notebook(self.window)

        self.tab1 = AddTab(self.tabControl)
        self.tab2 = SubTab(self.tabControl)

        self.tabControl.add(self.tab1.get_frame(), text ='Addition')
        self.tabControl.add(self.tab2.get_frame(), text ='Subtraction')
        self.tabControl.pack(expand = 1, fill ="both", padx=20, pady=20)

        self.window.mainloop()
        
class AddTab:
        def __init__(self, master):
            self.master = master
            self.frame = ttk.Frame(self.master)
            self.frame.pack()
    
            self.label1 = ttk.Label(self.frame, text="First Value")
            self.label1.grid(row=0, column=0, sticky="w")
    
            self.entry1 = ttk.Entry(self.frame)
            self.entry1.grid(row=0, column=1, padx=5, pady=5)
    
            self.label1 = ttk.Label(self.frame, text="Second Value")
            self.label1.grid(row=1, column=0, sticky="e")
    
            self.entry2 = ttk.Entry(self.frame)
            self.entry2.grid(row=1, column=1, padx=5, pady=5)

            self.add_button = ttk.Button(self.frame,text=("Add"), command=self.add)
            self.add_button.grid(row=2, column=1,padx=10, pady=10, sticky="es")

        def add(self):
                value1 = self.entry1.get()
                value2 = self.entry2.get()
                
                if (value1.isnumeric and value2.isnumeric()) != True:
                    messagebox.showerror("Not Int!", message="please enter intger values")
                    return
                sum = int(value1) + int(value2)
                messagebox.showinfo("Result",f"{sum}")

        def get_frame(self):
            return self.frame
        

class SubTab:
        def __init__(self, master):
            self.master = master
            self.frame = ttk.Frame(self.master)
            self.frame.pack()
    
            self.label1 = ttk.Label(self.frame, text="First Value")
            self.label1.grid(row=0, column=0, sticky="w")
    
            self.entry1 = ttk.Entry(self.frame)
            self.entry1.grid(row=0, column=1, padx=5, pady=5)
    
            self.label1 = ttk.Label(self.frame, text="Second Value")
            self.label1.grid(row=1, column=0, sticky="e")
    
            self.entry2 = ttk.Entry(self.frame)
            self.entry2.grid(row=1, column=1, padx=5, pady=5)

            self.sub_button = ttk.Button(self.frame,text=("Sub"), command=self.sub)
            self.sub_button.grid(row=2, column=1,padx=10, pady=10, sticky="es")

        def sub(self):
                value1 = self.entry1.get()
                value2 = self.entry2.get()
                
                if (value1.isnumeric and value2.isnumeric()) != True:
                    messagebox.showerror("Not a number", message="Please enter numeric values..")
                    return
                
                res = int(value1) - int(value2)
                messagebox.showinfo("Result",f"{res}")

        def get_frame(self):
            return self.frame

MainWindow()