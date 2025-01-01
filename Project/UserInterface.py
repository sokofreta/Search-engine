import tkinter as tk
import os

from ReversedIndexing import *

def DataDisplay() :
    data = PrettifyRI()
    given = entry.get()
    if given in data :
        label = tk.Label(root,text=given,justify="left")
        label.pack()


def UserInterface():
    entry = tk.Entry(root,textvariable="",font="Arial 25",fg="red")
    entry.pack(side="top")
    button = tk.Button(root,command=DataDisplay,text="CLICK ME YOU FUCKER!")
    button.pack()         
    root.mainloop()

#Shows the content of the News.
def NewsFilesContent() :
    files = os.listdir('News')
    for file in files :
         with open(f"News/{file}","r") as f :
            for line in f :
                data = line.split("~")[1].strip()
                print(data)
                w = tk.Label(root, text=data,height=1,width=50)
                w.pack()
            w = tk.Label(root, text="-----------------------------------------",height=2,width=50)
            w.pack()


def NewsTitles() :
    files = os.listdir("Titles")
    for file in files :
        with open(f"Titles/{file}","r") as f :
            for line in f :
                title = line 
                print(title)
                w = tk.Label(root, text=title,height=1,width=50)
                w.pack()
            w = tk.Label(root,text="-----------------------------------------",height=2,width=50)
            w.pack()



root = tk.Tk()
root.geometry("600x600")
entry = tk.Entry(root,textvariable="",font="Arial 25",fg="red")
entry.pack(side="top")
button = tk.Button(root,command=DataDisplay,text="CLICK ME YOU FUCKER!")
button.pack()         
root.mainloop()



if __name__ == "__main__" :
    UserInterface()