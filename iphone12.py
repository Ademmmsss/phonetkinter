
import pyttsx3
import tkinter as tk
from tkinter import *
import webbrowser as wb
import time
import pyautogui as p

print('IPHONE 12')
print('made by Leechongloz')


x = pyttsx3.init('sapi5')
x.setProperty('rate',165)
def speak(audio):
    x.say(audio)
    x.runAndWait()

def movie():
    wb.open_new('https://hurawatch.cc/home/')
    


def openyt():
    wb.open_new('https://www.youtube.com')
def wiki():
    wb.open_new('https://www.wikipedia.org')
def searchh():
    wb.open_new('https://www.google.com/search?q='+search.get())



def spam():
    def startbtn():
        time.sleep(4)
        for i in range(int(nombor.get())):
            p.typewrite(text.get())
            time.sleep(0.1)
            p.press('enter')
            time.sleep(1)
    w = Tk()
    w.geometry('400x200')
    w.resizable(False,False)
    w.title('Whatsapp Spammer')
    text= StringVar(w)
    nombor = StringVar(w)
    tk.Label(w,text='Berapa banyak nak spam:').place(x=10,y=10)
    tk.Entry(w, textvariable=nombor).place(x=155,y=10,width=25)
    tk.Label(w,text='Nak spam apa:').place(x=10,y=50)
    tk.Entry(w, textvariable=text).place(x=100,y=50,width=250)
    tk.Button(w, text='START', command=lambda:startbtn()).place(x=10,y=155)


    w.mainloop()

# making a screen
s = Tk()
s.resizable(False, False)

s.geometry('300x480')
s.title('Iphone 12')
s.configure(bg='black')
s.iconbitmap('C:\\Users\\Adam\\Downloads\\iconapple.ico')

tk.Label(s, text='LEECHONGLOZ', bg='yellow').place(x=100, y=10)
tk.Button(s, text='YOUTUBE', command=lambda: openyt()).place(x=10,y=50,height=50,width=70)
tk.Button(s, text='WIKIPEDIA', command=lambda: wiki()).place(x=110,y=50,height=50,width=70)
tk.Button(s, text='WS SPAM', command=lambda: spam()).place(x=210,y=50,height=50,width=70)
tk.Button(s, text='Movie', command=lambda: movie()).place(x=10,y=110,height=50,width=70)
search = StringVar()
sss = Entry(s, textvariable=search, justify=CENTER)
sss.place(x=30,y=400,width=230)
tk.Button(s, text='Search',command=lambda:searchh()).place(x=120,y=425)




s.mainloop()
