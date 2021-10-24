from tkinter import Tk, Entry
from tkinter import Button, Label

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title_label = Label(self, text="A simple calculator")
        self.title_label.pack()
        self.entry = Entry(self)
        self.entry.pack()
        self.entry.insert(0, "Enter numbers like 1 + 2")
        self.label = Label(self, text="")
        self.label.pack()
        self.button = Button(self, text="Compute", command=self.onclick)
        self.button.pack()

    def onclick(self):
        self.label.configure(text=str(eval(self.entry.get())))


root = Root()
root.mainloop()
