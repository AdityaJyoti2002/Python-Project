from lib2to3.pytree import convert
from matplotlib.dates import FR
from plyer import notification
from tkinter import *
from tkinter import messagebox
from functools import partial
from mac_notifications import client
from PIL import Image, ImageTk
import time
# root = Tk()
root = Tk()
root.title("Notification App")
root.geometry("500x300")
root.config(bg="#26242f")
global button_mode

button_mode = True

def windows():
    def customize():
        global button_mode
        f3 = Frame()
        f3.place(x=0, y=0, width=500, height=300)

        if button_mode:
            button1.config(image=convert_Off, bg="#26242f", activebackground="#26242f")
            f3.config(bg="#26242f")

            # image.config(image=convert_image2, bg="#26242f", width=300, height=300)
            button_mode = False
        else:
            button1.config(image=convert_On, bg="white", activebackground="white")
            # inputtext.config(bg="white")
            f3.config(bg="white")
            # image.config(image=convert_image, bg="white", width=300, height=300)
            button_mode = True

    def get_details():
        f3 = Frame()
        f3.place(x=0, y=0, width=500, height=300)
        get_title = inputtext.get()
        get_message = inputtext1.get()
        get_set_time = inputtext2.get()

        if get_title == "" or get_message == "" or get_set_time == "":
            messagebox.showerror("Alert", "All feilds are required")
        else:
            int_time = int(float(get_set_time))
            min_to_sec = int_time * 60
            messagebox.showinfo("notifier set", "Set Notification ?")
            f3.destroy()
            time.sleep(min_to_sec)
            # notification.notify(title=get_title, message=get_message, app_name="Notifier", app_icon="ico.ico", toast=True, timeout=10)
            client.create_notification(
            title= get_title,
            subtitle= get_message,
            icon="/Users/adityajyoti/Documents/Python/project/Notification-app/ico.ico",
            action_button_str="Join zoom meeting",
            # action_callback=partial("join_zoom_meeting", conf_number=zoom_conf_number)
        )
# if __name__ == "__main__":
    f2 = Frame()
    f2.place(x=0, y=0, width=500, height=300)
    img = Image.open("/Users/adityajyoti/Documents/Python/project/Notification-app/notify-label.png")
    img2 = ImageTk.PhotoImage(img)
    # root.config(bg="#26242f")

    image = Label(f2, image=img2 )
    image.pack()

    text = Label(f2, text="Notify ", font=("poppins", 20), bg="#26242f")
    text.place(x=12, y=70)

    inputtext = Entry(f2, width=40, font=( "poppins",13))
    inputtext.place(x=123, y=70)

    text1 = Label(f2, text="Display Message", font=("poppins", 20),bg="#26242f")
    text1.place(x=12,y=120)

    inputtext1 = Entry(f2, width=20, font=("poppins", 20))
    inputtext1.place(x=170,height=30, y=120)

    text2 = Label(f2, text="Set Time", font=("poppins", 20, ),bg="#26242f")
    text2.place(x=12, y=175)

    # time
    inputtext2 = Entry(f2, width=5, font=("poppins", 20))
    inputtext2.place(x=123, y=175)

    min = Label(f2, text="min", font=("poppins", 20), bg="#26242f")
    min.place(x=200, y=180)

    button = Button(f2, text="Set Notification", font=("poppins", 10, "bold"), fg="blue", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
    button.place(x=170, y=230)
    # On = PhotoImage(file="/Users/adityajyoti/Documents/Python/project/Light/light.png")
    

    On = Image.open("/Users/adityajyoti/Documents/Python/project/Light/light.png")
    resize_On = On.resize((60,50))
    convert_On = ImageTk.PhotoImage(resize_On)

    Off = Image.open("/Users/adityajyoti/Documents/Python/project/Light/dark.png")
    resize_off = Off.resize((60,50))
    convert_Off = ImageTk.PhotoImage(resize_off)

    button1 = Button(f2, image=convert_On, bd=0, bg="white", activebackground="white", command=customize)
    button1.place(x=50, y=230)

def macos():
    def customize():
        global button_mode
        # f3 = Frame()
        # f3.place(x=0, y=0, width=500, height=300)

        if button_mode:
            button1.config(image=convert_Off, bg="#26242f", activebackground="#26242f")
            root.config(bg="#26242f")

            # image.config(image=convert_image2, bg="#26242f", width=300, height=300)
            button_mode = False
        else:
            button1.config(image=convert_On, bg="white", activebackground="white")
            # inputtext.config(bg="white")
            root.config(bg="white")
            # image.config(image=convert_image, bg="white", width=300, height=300)
            button_mode = True

    def get_details():
        # f3= Frame()
        # f3.place(x=0, y=0, width=500, height=300)
        get_title = inputtext.get()
        get_message = inputtext1.get()
        get_set_time = inputtext2.get()

        if get_title == "" or get_message == "" or get_set_time == "":
            messagebox.showerror("Alert", "All feilds are required")
        else:
            int_time = int(float(get_set_time))
            min_to_sec = int_time * 60
            messagebox.showinfo("notifier set", "Set Notification ?")
            root.destroy()
            time.sleep(min_to_sec)
            # notification.notify(title=get_title, message=get_message, app_name="Notifier", app_icon="ico.ico", toast=True, timeout=10)
            client.create_notification(
            title= get_title,
            subtitle= get_message,
            icon="/Users/adityajyoti/Documents/Python/project/Notification-app/ico.ico",
            action_button_str="Join zoom meeting",
            # action_callback=partial("join_zoom_meeting", conf_number=zoom_conf_number)
        )
# if __name__ == "__main__":
    f2 = Frame()
    f2.place(x=0, y=0, width=500, height=300)
    img = Image.open("/Users/adityajyoti/Documents/Python/project/Notification-app/notify-label.png")
    img2 = ImageTk.PhotoImage(img)
    # root.config(bg="#26242f")

    image = Label(f2, image=img2 )
    image.pack()

    text = Label(f2, text="Notify ", font=("poppins", 20), bg="#26242f")
    text.place(x=12, y=70)

    inputtext = Entry(f2, width=40, font=( "poppins",13))
    inputtext.place(x=123, y=70)

    text1 = Label(f2, text="Display Message", font=("poppins", 20),bg="#26242f")
    text1.place(x=12,y=120)

    inputtext1 = Entry(f2, width=20, font=("poppins", 20))
    inputtext1.place(x=170,height=30, y=120)

    text2 = Label(f2, text="Set Time", font=("poppins", 20, ),bg="#26242f")
    text2.place(x=12, y=175)

    # time
    inputtext2 = Entry(f2, width=5, font=("poppins", 20))
    inputtext2.place(x=123, y=175)

    min = Label(f2, text="min", font=("poppins", 20), bg="#26242f")
    min.place(x=200, y=180)

    button = Button(f2, text="Set Notification", font=("poppins", 10, "bold"), fg="blue", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
    button.place(x=170, y=230)
    # On = PhotoImage(file="/Users/adityajyoti/Documents/Python/project/Light/light.png")
    

    On = Image.open("/Users/adityajyoti/Documents/Python/project/Light/light.png")
    resize_On = On.resize((60,50))
    convert_On = ImageTk.PhotoImage(resize_On)

    Off = Image.open("/Users/adityajyoti/Documents/Python/project/Light/dark.png")
    resize_off = Off.resize((60,50))
    convert_Off = ImageTk.PhotoImage(resize_off)

    button1 = Button(f2, image=convert_On, bd=0, bg="white", activebackground="white", command=customize)
    button1.place(x=50, y=230)

    button1 = Button(f2,text="<", bd=0, bg="white", activebackground="white", command=back)
    button1.place(x=2, y=3)

def back():
    # root = Tk()
    # root.title("Notification App")
    # root.geometry("500x300")

    f1 = Frame()
    f1.place(x=0, y=0, width=500, height=300)

    button = Button(f1, text="MacOs", font=("poppins", 30), fg="blue", bg="red", width=15, command=macos)
    button.place(x=100, y=70)

    button = Button(f1, text="Windows", font=("poppins", 30), fg="blue", bg="red", width=15, command=windows)
    button.place(x=100, y=140)
back()
root.mainloop()