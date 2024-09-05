from tkinter import *
from tkinter import *
frame01 = Frame()
frame01.mainloop()


class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.myCanvas = Canvas(width=300, height=200, bg="blue")
        self.myCanvas.grid()
        self.myCanvas.create_oval(10, 10, 200, 100, fill="white")
        self.myCanvas.create_rectangle(10, 10, 200, 100, fill="blue")
        self.myCanvas.create_line(1, 1, 200, 200, arrow="first")
        my_font = ("Times", 25)
        self.myCanvas.create_text(1, 1, text="Hello World",
                                  width=70, fill="black", anchor="nw",
                                  justify="center", font=my_font)


frame02 = MyFrame()
frame02.mainloop()


class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=150, height=150, bg="white")
        self.myCanvas.grid()

        self.myCanvas.create_rectangle(10, 10, 20, 20, fill="red")
        self.myCanvas.create_rectangle(10, 30, 20, 40, fill="yellow")
        self.myCanvas.create_rectangle(10, 50, 20, 60, fill="blue")

        print("Finds all shapes")
        print(self.myCanvas.find_enclosed(0, 0, 30, 70))

        print("Finds middle shape")
        print(self.myCanvas.find_enclosed(0, 25, 30, 45))

        print("Finds no shapes")
        print(self.myCanvas.find_enclosed(0, 0, 1, 1))


frame02 = MyFrame()
frame02.mainloop()
