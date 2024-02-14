from tkinter import *
import page2
import page1


class page3:
    def __init__(self, window):
        self.window = window
        self.window.title("Page 3")
        self.window.geometry("500x500")

        self.label = Label(self.window, text="Page 1")
        self.label.pack()

        self.button = Button(self.window, text="Go to Page 2", command=self.page2)
        self.button.pack()
        
        self.button = Button(self.window, text="Go to Page 1", command=self.page1)
        self.button.pack()
        
    def page2(self):
        win=Toplevel()
        page2.page2(win)
        # withdraw window
        self.window.withdraw()
        win.deiconify()
        
    def page1(self):
        win=Toplevel()
        page1.page1(win)
        # withdraw window
        self.window.withdraw()
        win.deiconify()
    


def page():
    window = Tk()
    page3(window)
    window.mainloop()

if __name__ == "__main__":
   page()


