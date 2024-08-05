import tkinter as tk

class WeatherApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.frame1 = None
        self.frame2 = None
        self.master = master
        self.master.geometry("300x300")
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.create_frame1()
        self.create_frame2()

    def create_frame1(self):
        self.frame1 = tk.Frame(self, bg='red', width=150)
        self.frame1.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def create_frame2(self):
        self.frame2 = tk.Frame(self, bg='blue', width=150)
        self.frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

