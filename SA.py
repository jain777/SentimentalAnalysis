from typing import OrderedDict, SupportsComplex
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from textblob import TextBlob


engine = pyttsx3.init()

#Defining Function to get voice command

def check():


    global order 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)     #Listens the audio
        order = r.recognize_google(audio,language="en-in")


        #inserting a textare

    sen_analy()

def sen_analy():
    obj = TextBlob(order)
    sentiment=obj.sentiment.polarity


    if sentiment>0:
        engine.say("You seem quite positive")
        engine.runAndWait()

        l2.configure(text="Positive\nSentence\n:)")

    if sentiment==0:
        engine.say("You seem quite neutral")
        engine.runAndWait()

        l2.configure(text="Neutral\nSentence\n:(-_-)")

    else:
        engine.say("You seem quite negative")
        engine.runAndWait()

        l2.configure(text="Negative\nSentence\n:(")


#GUI

root = tk.Tk()
root.geometry("400x400")
root.title("WhySed")
root.configure(bg="cyan")
font=('verdana',35,'bold')
font2=('verdana',30,'bold')
l1=tk.Label(root,text="Test your voice note",bg = "black", fg = "white", font=font)
l1.place(x=100,y=10)

l2 = tk.Label(root,text=":)",bg="black",fg="white",font=font2)
l2.place(x =120,y=50)
b1=tk.Button(root,text="Speak",bg="blue",fg="white",command=check)
b1.place(x=50,y=220,height=50,width=400)


root.mainloop()





