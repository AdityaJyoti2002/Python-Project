from cProfile import label
from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title("Login")
root.geometry('925x500+300+200')
root.config(bg = '#fff')
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    file= open("/Users/adityajyoti/Documents/Python/project/login signin/datasheet1.txt", 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())

    if username in r.keys() and password == r[username]:
        print("welcome to my channel")

    elif username!= 'aditya' and password!= '1234':
        messagebox.showerror("Invalid", "invlid username and password")
    
    elif username== 'aditya' and password!= '1234':
        messagebox.showerror("Invalid", "invlid password")

    elif username!= 'aditya' and password== '1234':
        messagebox.showerror("Invalid", "invlid username")

img = PhotoImage(file= "/Users/adityajyoti/Documents/Python/project/login signin/login.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=450, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white',font=('UI light',24,'bold'))
heading.place(x=110, y=5)

# username-----------------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0,bg='white',font=('UI light',11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black' ).place(x=25, y=107)
# username================================

# password=================================
def on_enter1(e):
    code.delete(0, 'end')

def on_leave1(e):
    name = code.get()
    if name == "":
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0,bg='white',font=('UI light',11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter1)
code.bind('<FocusOut>', on_leave1)

Frame(frame, width=295, height=2, bg='black' ).place(x=25, y=177)
# password=================================

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
lable = Label(frame, text="Don't have an account? ", fg='black', bg='white', font=("UI light",9))
lable.place(x=75, y=270)

sign_up = Button(frame, width=7, text='Sign up', bg='white', cursor='hand', fg='#57a1f8',border=0, font=("UI light",10), )
sign_up.place(x=199, y=270)
root.mainloop()