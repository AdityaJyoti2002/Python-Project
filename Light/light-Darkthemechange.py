from tkinter import *
from PIL import Image, ImageTk

from numpy import pad
button_mode= True

# Create function
def customize():
    global button_mode

    if button_mode:
        button.config(image=Off, bg="#26242f", activebackground="#26242f")
        root.config(bg="#26242f")
        image.config(image=convert_image2, bg="#26242f", width=300, height=300)
        button_mode = False
    else:
        button.config(image=On, bg="white", activebackground="white")
        root.config(bg="white")
        image.config(image=convert_image, bg="white", width=300, height=300)
        button_mode = True

if __name__ == "__main__":
    root = Tk()
    root.title("Toggle Switch")
    root.geometry("400x600")
    root.config(bg="white")
    # button_mode= True

    On = PhotoImage(file="/Users/adityajyoti/Documents/Python/project/Light/light.png")
    Off = PhotoImage(file="/Users/adityajyoti/Documents/Python/project/Light/dark.png")
    
    # Create Button
    button = Button(root, image=On, bd=0, bg="white", activebackground="white", command=customize)
    button.pack(padx=50, pady=50)
    
    # image resize
    photo = Image.open("/Users/adityajyoti/Documents/Python/project/Light/mode-light-icon-512x512-yuubs6qt.png")
    resize_image = photo.resize((300,300))
    convert_image = ImageTk.PhotoImage(resize_image)

    photo2 = Image.open("/Users/adityajyoti/Documents/Python/project/Light/moon.png")
    resize_image2 = photo2.resize((300,300))
    convert_image2 = ImageTk.PhotoImage(resize_image2)
    # End image resize
    # insert image
    image = Label(root, image=convert_image, width=300, height=300 , bg="white")
    image.pack()
    root.mainloop()