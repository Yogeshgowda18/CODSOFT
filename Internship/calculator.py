#import modules
from tkinter import *
class Calculator:
    def __init__(self, master):
        self.master = master

        #Add a name to our application
        master.title("Calculator")

        #Create a line where we display the equation
        self.equation=Entry(master, width=50, borderwidth=5)

        #Assign a position for the equation line in the grey application window
        self.equation.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

        #Execute the .creteButton() method
        self.createButton()

    def createButton(self):
        #We first create each button one by one with the value we want
        #Using addButton() method which is described below
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 =  self.addButton(9)
        b_add = self.addButton('+')
        b_sub = self.addButton('-')
        b_mult = self.addButton('*')
        b_div = self.addButton('/')
        b_clear = self.addButton('c')
        b_equal = self.addButton('=')

        #Arrange the buttons into lists which represent calculator rows
        row1=[b7,b8,b9,b_add]
        row2=[b4,b5,b6,b_sub]
        row3=[b1,b2,b3,b_mult]
        row4=[b_clear,b0,b_equal,b_div]

        #Assign each button to a particular location on the GUI
        r=1
        for row in [row1, row2, row3, row4]:
            c=0
            for buttn in row:
                buttn.grid(row=r, column=c, columnspan=1)
                c+=1
            r+=1
    def addButton(self,value):
        return Button(self.master, text=value, width=10, command = lambda: self.clickButton(str(value)))
    
    def clickButton(self, value):
        #Get the equation that's entered by the user
        current_equation=str(self.equation.get())
        
        #If user clicked "c", then clear the screen
        if value == 'c':
            self.equation.delete(-1, END)
        
        #If user clicked "=", then compute the answer and display it
        elif value == '=':
            answer = str(eval(current_equation))
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)
        
        #If user clicked any other button, then add it to the equation line
        else:
            self.equation.delete(0, END)
            self.equation.insert(0, current_equation+value)
if __name__=='__main__':
    root = Tk()
    my_gui = Calculator(root)
    root.mainloop()
