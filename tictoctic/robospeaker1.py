# from cProfile import label
from cProfile import label
from email.mime import audio
import os
import gtts
# from winsound import PlaySound
from playsound import playsound
from gtts import gTTS
from tkinter import *
# check again

from django.forms import Textarea
from gtts import gTTS

language = 'en'
audio = 'speech.mp3'
audio = "texttospeech.mp3"

def speaktest():
    text = Inputtext.get()
    tggs = gTTS(text=text, lang='en')
    tggs.save(audio)
    os.system(" start audio")




if __name__ == "__main__":
    root = Tk()
    root.title("Roboseaker by Aditya Jyoti")
    root.geometry("900x200")
    Text = Label(root, text="welcome to RoboSpeaker 1.1 made by Aditya Jyoti",)
    Text.pack()
    sp = gTTS(text="welcome to RoboSpeaker 1.1 made by Aditya Jyoti", lang= language, slow=False)
    sp.save(audio)
    os.system(" start audio")
    # playsound(audio)
    speaker = os.system(f"say 'welcome to RoboSpeaker 1.1 made by Aditya Jyoti'")
    # speaker.pack()
    Text = Label(root, text="Enter what you want me to speaker:")
    Text.pack()
    title = StringVar()
    Inputtext = Entry(root, textvariable=title)
    Inputtext.pack()
    button = Button(root, text="Speak", command=speaktest)

    button.pack()
    root.mainloop()
