from tkinter import *
import webbrowser as wb
import wx
import wolframalpha
from espeakng import ESpeakNG as espeak
import wikipedia
import main as cmd

googleExistance = True
terminalExistance = True
calculatorExistance = True
amyExistance = True
terminalPosition = 2
googlePosition = 3
amyPosition = 1
calculatorPosiion = 4
app_id = "YUK7YW-67K6H83PRW"
client = wolframalpha.Client(app_id)

root = Tk()
root.geometry('1000x600')
root.title("Krypterminal")


def Application(Frame):
    """ Main class for calculator"""

    def __init__(self, master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create all the buttons for calculator. """
        # User input stored as an Entry widget.

        self.user_input = Entry(self, bg="#5BC8AC", bd=29,
                                   insertwidth=4, width=24,
                                   font=("Verdana", 20, "bold"), textvariable=self.UserIn, justify=RIGHT)
        self.user_input.grid(columnspan=4)

        self.user_input.insert(0, "0")

        # Button for value 7
        self.button1 = Button(self, bg="#98DBC6", bd=12,
                                 text="7", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                                 command=lambda: self.buttonClick(7))
        self.button1.grid(row=2, column=0, sticky=W)

        # Button for value 8
        self.button2 = Button(self, bg="#98DBC6", bd=12,
                                 text="8",  padx=35, pady=25,
                                 command=lambda: self.buttonClick(8), font=("Helvetica", 20, "bold"))
        self.button2.grid(row=2, column=1, sticky=W)

        # Button for value 9
        self.button3 = Button(self, bg="#98DBC6", bd=12,
                                 text="9",  padx=33, pady=25,
                                 command=lambda: self.buttonClick(9), font=("Helvetica", 20, "bold"))
        self.button3.grid(row=2, column=2, sticky=W)

        # Button for value 4
        self.button4 = Button(self, bg="#98DBC6", bd=12,
                                 text="4",  padx=33, pady=25,
                                 command=lambda: self.buttonClick(4), font=("Helvetica", 20, "bold"))
        self.button4.grid(row=3, column=0, sticky=W)

        # Button for value 5
        self.button5 = Button(self, bg="#98DBC6", bd=12,
                                 text="5",  padx=35, pady=25,
                                 command=lambda: self.buttonClick(5), font=("Helvetica", 20, "bold"))
        self.button5.grid(row=3, column=1, sticky=W)

        # Button for value 6
        self.button6 = Button(self, bg="#98DBC6", bd=12,
                                 text="6",  padx=33, pady=25,
                                 command=lambda: self.buttonClick(6), font=("Helvetica", 20, "bold"))
        self.button6.grid(row=3, column=2, sticky=W)

        # Button for value 1
        self.button7 = Button(self, bg="#98DBC6", bd=12,
                                 text="1",  padx=33, pady=25,
                                 command=lambda: self.buttonClick(1), font=("Helvetica", 20, "bold"))
        self.button7.grid(row=4, column=0, sticky=W)

        # Button for value 2
        self.button8 = Button(self, bg="#98DBC6", bd=12,
                                 text="2",  padx=35, pady=25,
                                 command=lambda: self.buttonClick(2), font=("Helvetica", 20, "bold"))
        self.button8.grid(row=4, column=1, sticky=W)

        # Button for value 3
        self.button9 = Button(self, bg="#98DBC6", bd=12,
                                 text="3",  padx=33, pady=25,
                                 command=lambda: self.buttonClick(3), font=("Helvetica", 20, "bold"))
        self.button9.grid(row=4, column=2, sticky=W)

        # Button for value 0
        self.button9 = Button(self, bg="#98DBC6", bd=12,
                                 text="0",  padx=33, pady=25,
                                 command=lambda: self.buttonClick(0), font=("Helvetica", 20, "bold"))
        self.button9.grid(row=5, column=0, sticky=W)

        # Operator buttons
        # Addition button
        self.Addbutton = Button(self, bg="#98DBC6", bd=12,
                                   text="+",  padx=36, pady=25,
                                   command=lambda: self.buttonClick("+"), font=("Helvetica", 20, "bold"))
        self.Addbutton.grid(row=2, column=3, sticky=W)

        # Subtraction button
        self.Subbutton = Button(self, bg="#98DBC6", bd=12,
                                   text="-",  padx=39, pady=25,
                                   command=lambda: self.buttonClick("-"), font=("Helvetica", 20, "bold"))
        self.Subbutton.grid(row=3, column=3, sticky=W)

        # Multiplication button
        self.Multbutton = Button(self, bg="#98DBC6", bd=12,
                                    text="*",  padx=38, pady=25,
                                    command=lambda: self.buttonClick("*"), font=("Helvetica", 20, "bold"))
        self.Multbutton.grid(row=4, column=3, sticky=W)

        # Division button
        self.Divbutton = Button(self, bg="#98DBC6", bd=12,
                                   text="/",  padx=39, pady=25,
                                   command=lambda: self.buttonClick("/"), font=("Helvetica", 20, "bold"))
        self.Divbutton.grid(row=5, column=3, sticky=W)

        # Equal button
        self.Equalbutton = Button(self, bg="#E6D72A", bd=12,
                                     text="=",  padx=100, pady=25,
                                     command=self.CalculateTask, font=("Helvetica", 20, "bold"))
        self.Equalbutton.grid(row=5, column=1, sticky=W, columnspan=2)

        # Clear Button
        self.Clearbutton = Button(self, bg="#E6D72A", bd=12,
                                     text="AC", font=("Helvetica", 20, "bold"), width=28, padx=7, command=self.ClearDisplay)
        self.Clearbutton.grid(row=1, columnspan=4, sticky=W)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer

        except SyntaxError as e:
            self.displayText("Invalid Syntax!")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")
def amy():
    class MyFrame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None, pos=wx.DefaultPosition, size=wx.Size(
                450, 100), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, title="Amy")
            panel = wx.Panel(self)
            my_sizer = wx.BoxSizer(wx.VERTICAL)
            lbl = wx.StaticText(panel,
                                label="Hello I am Amy Your new Digital Assistant. How can I help you?")
            my_sizer.Add(lbl, 0, wx.ALL, 5)
            self.txt = wx.TextCtrl(
                panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
            self.txt.SetFocus()
            self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
            my_sizer.Add(self.txt, 0, wx.ALL, 5)
            panel.SetSizer(my_sizer)
            self.Show()

        def OnEnter(self, event):

            input = self.txt.GetValue()
            input = input.lower()
            try:
                res = client.query(input)
                answer = next(res.results).text
                print(answer)
                espeak.synth("The answer is "+str(answer))
            except:
                try:
                    input = input.split(' ')
                    input = ' '.join(input[2:])
                    print(wikipedia.summary(input))
                except:
                    print("I don't know")

    if __name__ == "__main__":
        app = wx.App(True)
        frame = MyFrame()
        app.MainLoop()
def google():
    wb.open_new_tab('http://www.google.com')
def calc():
    calculator = Tk()
    calculator.title("Calculator")
    app = Application(calculator)
    # Make window fixed (cannot be resized)
    calculator.resizable(width=False, height=False)
    calculator.mainloop()
def terminal():
    def run():
        cmd1 = entry1.get()
        mytext = cmd.execCmd(cmd1)
        if cmd1 != None:
            label1['text'] = mytext
        

    root2 = Tk()
    root2.geometry('1000x600')
    root2.title("Terminal")
    root2.configure(background="black")

    mytext = None
    entry1 = Entry(root2)
    label1 = Label(root2, text=mytext, fg="white", bg="black")
    button1 = Button(root2, text="enter", foreground="white", background="black", command=run)
    
    entry1.grid(column=0, row=0)
    label1.grid(column=0, row=1)
    button1.grid(column=1, row=0)
    cmd.execCmd()
    root2.mainloop()

c = Canvas(root, height=600, width=1000, bg='lightblue')
l = c.create_rectangle(0, 550, 1000, 600, fill="black")
c.place(x=0, y=0)
Button1 = Button(root)
photo = PhotoImage(file= cmd.BP + "/Calc.png")
Button1.config(image=photo, width=45, height=45, foreground="black", background="black")
Button1.place(x=400, y=550)

Button2 = Button(root, command=google)
photo2 = PhotoImage(file=cmd.BP + "/Google.png")
Button2.config(image=photo2, width=45, height=45, foreground="black", background="black")
Button2.place(x=330, y=550)

Button3 = Button(root, command=terminal)
photo3 = PhotoImage(file=cmd.BP + "/terminal.png")
Button3.config(image=photo3, width=45, height=45, foreground="black", background="black")
Button3.place(x=260, y=550)

Button4 = Button(root, command=amy)
photo4 = PhotoImage(file=cmd.BP + "/Amy.png")
Button4.config(image=photo4, width=45, height=45, foreground="black", background="black")
Button4.place(x=190, y=550)

c.pack()

root.mainloop()
