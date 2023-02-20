import tkinter

window = tkinter.Tk()
window.title("MY APP")
#window.geometry('600x600')
window.configure(background="yellow")

def buttonpress():
    print("button pressed")

label = tkinter.Label(window, text="HELLO KARTHIK HOW IS THE JOSH").pack(padx=20)
btn = tkinter.Button(window, text="PRESS ME",foreground="white",background="green",command=buttonpress).pack()
window.mainloop()
