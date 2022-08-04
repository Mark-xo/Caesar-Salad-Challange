from ast import Delete
import random
import time,sys
from os import system, name
import tkinter as tk
from tkinter import *
from tkinter.font import Font

root=tk.Tk()
root.geometry("1280x606")
root.title("Caesar Salad")
root.grid()
bg = PhotoImage(file = "background.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)


count=0
LoadingFont=Font(family="VCR OSD Mono", size=30)
blank=tk.Label(root,text="",bg="#0b0c0b",fg="#69b183")
blank.pack(pady=12,padx=200,side=LEFT)
while(count<10):
    x=tk.Label(root, text='#',bg = "#0b0c0b",fg = "#69b183",font = LoadingFont)
    x.pack(pady=15,side=LEFT,padx =10)
    root.update() # allow window to catch up
    time.sleep(0.1)
    count += 1


labelb = Label( root, image = bg)
labelb.place(x = 0, y = 0)


myFont=Font(family="VCR OSD Mono", size=30)
label2 = Label( root, text = "CAESAR SALAD",bg = "#0b0c0b",fg = "#69b183",font = myFont)
label2.place(x = 520, y = 150)

myFont1=Font(family="VCR OSD Mono", size=15)
label3 = Label( root, text = "The Great Julius Caesar has presented his 1100 soldiers with a bowl of salad",bg = "#0b0c0b",fg = "#69b183",font = myFont1)
label3.place(x = 200, y = 220)

label4=Label(root,text="You have been given one of the bowl, can you solve the mystery and save the tux",bg="#0b0c0b",fg="#69b183",font=myFont1)
label4.place(x=185,y=250)
# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )





# a=random.randint(1,308)
# print(a)
# with open('salad.txt', 'r',encoding='utf-8') as f:
#     line=f.readlines()[a]
#     f.close()
#     w=line.split()[0]
#     print (w)
#     line=line.replace(w,'',1)
#     print (line)
#     # encrypt the line in caesar cipher
#     key = 12
#     cipher = ''
#     for char in line:
#         if char == ' ':
#             cipher += char
#         elif char.isupper():
#             cipher += chr((ord(char) + key - 65) % 26 + 65)
#         else:
#             cipher += chr((ord(char) + key - 97) % 26 + 97)
#     print (cipher)
#     ans=input('Enter the answer: ')


root.mainloop()