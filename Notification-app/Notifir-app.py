from lib2to3.pytree import convert
from plyer import notification
from tkinter import *
from tkinter import messagebox
from functools import partial
from mac_notifications import client
from PIL import Image, ImageTk
import time

button_mode = True
def customize():
    global button_mode

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


if __name__ == "__main__":
    root = Tk()
    root.title("Notification app")
    root.geometry("500x300")
    img = Image.open("/Users/adityajyoti/Documents/Python/project/Notification-app/notify-label.png")
    img2 = ImageTk.PhotoImage(img)
    root.config(bg="#26242f")

    image = Label(root, image=img2 )
    image.pack()

    text = Label(root, text="Notify ", font=("poppins", 20), bg="#26242f")
    text.place(x=12, y=70)

    inputtext = Entry(root, width=40, font=( "poppins",13))
    inputtext.place(x=123, y=70)

    text1 = Label(root, text="Display Message", font=("poppins", 20),bg="#26242f")
    text1.place(x=12,y=120)

    inputtext1 = Entry(root, width=20, font=("poppins", 20))
    inputtext1.place(x=170,height=30, y=120)

    text2 = Label(root, text="Set Time", font=("poppins", 20, ),bg="#26242f")
    text2.place(x=12, y=175)

    # time
    inputtext2 = Entry(root, width=5, font=("poppins", 20))
    inputtext2.place(x=123, y=175)

    min = Label(root, text="min", font=("poppins", 20), bg="#26242f")
    min.place(x=200, y=180)

    button = Button(root, text="Set Notification", font=("poppins", 10, "bold"), fg="blue", bg="#528DFF", width=20,
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

    button1 = Button(root, image=convert_On, bd=0, bg="white", activebackground="white", command=customize)
    button1.place(x=50, y=230)

    root.mainloop()
