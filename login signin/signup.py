import ast
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Sign Up")
root.geometry("925x500+300+200")
root.config(bg="white")
root.resizable(False, False)

def signup():
    username = user.get()
    password = code.get()
    conform_password = compass.get()

    if password == conform_password:
        try:
            file = open("datasheet.txt","r+" )
            d = file.read()
            r = ast.literal_eval(d)

            dic2 ={username:password}
            r.update(dic2)
            file.truncate(0)
            file.close()

            file= open("datasheet.txt", 'w')
            w = file.write(str(r))
            messagebox.showinfo("Signup", "Sucessfully sign up")

        except:
            file = open("datasheet.txt", 'w')
            pp= str({username:password})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror('Invalid', "Both Password should match")



img = PhotoImage(file="/Users/adityajyoti/Documents/Python/project/login signin/login (1).png")
Label(root, image=img, bg='white').place(x=55, y=60)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=450, y=70)

heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white',font=('UI light',24,'bold'))
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

def on_enter2(e):
    compass.delete(0, 'end')

def on_leave2(e):
    name = compass.get()
    if name == "":
        compass.insert(0, 'Conform Password')

compass = Entry(frame, width=25, fg='black', border=0,bg='white',font=('UI light',11))
compass.place(x=30, y=220)
compass.insert(0, 'Conform Password')
compass.bind('<FocusIn>', on_enter2)
compass.bind('<FocusOut>', on_leave2)

Frame(frame, width=295, height=2, bg='black' ).place(x=25, y=247)



Button(frame, width=38, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=32, y=250)
lable = Label(frame, text="I have an account? ", fg='black', bg='white', font=("UI light",9))
lable.place(x=75, y=290)

sign_up = Button(frame, width=7, text='Sign in', bg='white', cursor='hand', fg='#57a1f8',border=0, font=("UI light",10), )
sign_up.place(x=199, y=290)

root.mainloop()