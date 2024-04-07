from tkinter import *
import random

root = Tk()

root.title("Random List")
root.geometry("400x400")
root.configure(background = "snow")

ranlist = Label(root)
ranlistsort = Label(root)


def randoml():
    randomlist = random.sample(range(10, 30), 6)
    ranlist["text"] = "Your random list is " + str(randomlist)
    randomlist.sort()
    ranlistsort["text"] = "Your - sorted - list is " + str(randomlist)

btn=Button(root,text="Generate a random list.",command=randoml)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

ranlist.place(relx=0.5, rely=0.3, anchor=CENTER)
ranlistsort.place(relx=0.5, rely=0.2, anchor=CENTER)

root.mainloop()
 
