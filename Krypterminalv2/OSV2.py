import tkinter as tk # U MUST COMMENT ALMOST EVERY LINE OF OF UR CODE

googleExistance = True
terminalExistance = True
calculatorExistance = True
amyExistance = True
terminalPosition = 2
googlePosition = 3
amyPosition = 1
calculatorPosiion = 4
root = tk.Tk()
root.geometry('1000x600')
def hi3():
    print("hi")

c = tk.Canvas(root, height=600, width=1000, bg='lightblue')
l = c.create_rectangle(0, 550, 1000, 600, fill="black")
c.place(x=0, y=0)
Button1 = tk.Button(root, command=hi3)
photo = tk.PhotoImage(file="Calc.png")
Button1.config(image=photo, width=50, height=50)
Button1.place(x=10, y=545)
c.pack()

root.mainloop()