from tkinter import *
import  page1




class page2:
    def __init__(self, window):
        self.window = window
        window.title("Page 2")
        window.geometry("500x500")

        self.label = Label(window, text="Page 2")
        self.label.pack()

        self.button = Button(window, text="Go to Page 1", command=self.page1) 
        self.button.pack()
        
    def page1(self):
        win=Toplevel()
        page1.page1(win)
        # withdraw window
        self.window.withdraw()
        win.deiconify()
    


def page():
    window = Tk()
    page2(window)
    window.mainloop()

if __name__ == "__main__":
   page()


