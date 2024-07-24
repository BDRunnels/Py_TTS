from gtts import gTTS
from tkinter import *
import os

#   Hard coded text for testing
# text = "Question!"
# output = gTTS(text=text, lang="en", slow=False)
# output.save("o.mp3")
#
# os.system("afplay o.mp3")

# read file aloud
# text = open("demo.txt", "r", encoding="utf-8").read()
# lang = "en"
#
# output2 = gTTS(text=text, lang=lang, slow=False)
# output2.save("fileoutput.mp3")
#
# os.system("afplay fileoutput.mp3")

# user input
root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()


def text_to_speech():
    text = entry.get()
    lang = "en"
    output = gTTS(text=text, lang=lang, slow=False)
    output.save("output.mp3")
    os.system("afplay output.mp3")


entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text="Speak", command=text_to_speech)
canvas.create_window(200, 230, window=button)

root.mainloop()
